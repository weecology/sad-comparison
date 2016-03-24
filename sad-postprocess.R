library(progress)
library(dplyr)
library(ggplot2)
library(tidyr)
library(lme4)
library(magrittr)

ids = c("bbs", "mcdb")
cutoff = 9 # Copied from the Python processing code

# Negative binomial negative log-likelihood, truncated to exclude 0
nb_nll = function(x, log_size, log_mu) {
  size = exp(log_size)
  mu = exp(log_mu)
  
  # Consider using log==TRUE and lower.tail==FALSE here, as opposed to
  # log(1-p0) below
  p0 = dnbinom(0, size = size, mu = mu, log = FALSE)
  
  full_ll = dnbinom(x, size = size, mu = mu, log = TRUE)
  
  -sum(full_ll - log(1 - p0))
}

calculate_aicc = function(ll, k, N){
  2 * k - 2 * ll + 2 * k * (k + 1) / (N - k - 1)
}

postprocess = function(id){
  # Import spab data
  spab = read.csv(paste0("sad-data/", id, "_spab.csv"), skip = 2, header = FALSE)
  colnames(spab) = c('site','year','sp','ab')
  
  # Log-likelihoods from Python
  results = read.csv(paste0("sad-data/", id, "_likelihood_results.csv")) %>% arrange(site)
  
  # Drop relative likelihoods and AICc weights; they'll need to be recomputed 
  # when the negative binomial values change below.
  results = select(results, -matches("relative|AICc"))
  
  # Negative Binomial Log-likelihoods in R
  sites = spab %>% 
    group_by(site) %>% 
    summarize(S = n(), N = sum(ab)) %>% 
    filter(S > cutoff) %>%
    arrange(site) %>%
    extract2("site")
  
  stopifnot(all(sites == results$site))
  
  nb_ll = structure(rep(NA, length(sites)), names = sites)
  
  for (site in sites) {
    ab = spab[spab$site == site, "ab"]
    
    opt = optim(
      c(1, log(mean(ab))),
      function(par) {
        nb_nll(ab, par[1], par[2])
      }
    )
    
    nb_ll[as.character(site)] = -opt$value
  }
  
  results$likelihood_negbin = nb_ll
  
  log_likelihoods = select(results, matches("likelihood"))
  
  distribution_names = gsub(".*_", "", colnames(log_likelihoods))
  
  # Initialize AICc data with same shape as log_likelihoods and new column names
  AICcs = NA * log_likelihoods
  colnames(AICcs) = gsub("likelihood", "AICc", colnames(AICcs))
  
  k = sapply(
    distribution_names,
    function(name){
      switch(
        name,
        logseries = 1,
        pln = 2, 
        negbin = 2,
        zipf = 1,
        NA
      )
    }
  )  
  
  for (i in 1:ncol(AICcs)) {
    AICcs[ , i] = calculate_aicc(log_likelihoods[ , i], k = k[i], N = results$S)
  }
  
  cbind(id = id, results, AICcs)
}

# Call the postprocessing function on all the data sets
ll_list = lapply(ids, postprocess)

ll = do.call(rbind, ll_list)

is_lik = grepl("likelihood", colnames(ll))
is_AICc = grepl("AICc", colnames(ll))

ll_diff = ll[, is_lik] - rowMeans(ll[, is_lik])
ll_diff_long = gather(ll_diff, key = "distribution", value = "log_likelihood")

AICc_diff = ll[, is_AICc] - rowMeans(ll[, is_AICc])
AICc_diff_long = gather(AICc_diff, key = "distribution", value = "AICc")

ggplot(ll_diff_long, aes(x = distribution, y = log_likelihood)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean log-likelihood")

ggplot(AICc_diff_long, aes(x = distribution, y = AICc)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean AICc")


relative_likelihoods = exp(ll_diff) / rowSums(exp(ll_diff))
relative_likelihoods_long = gather(relative_likelihoods, 
                                   key = distribution, 
                                   value = relative_likelihood)

AICc_weight = exp(-AICc_diff / 2) / rowSums(exp(-AICc_diff / 2))
AICc_weight_long = gather(AICc_weight, 
                                   key = distribution, 
                                   value = AICc_weight)

# Note: I had to tweak the bandwidth parameter for this plot, or zipf's splat at
# zero would be so wide that the other distributions would be invisible by comparison.
# A bandwidth much less than 0.01 on a 0-1 scale is probably undersmoothed anyway.
ggplot(relative_likelihoods_long, aes(x = distribution, y = relative_likelihood)) +
  geom_violin(bw = .01) +
  theme_bw() +
  coord_cartesian(ylim = c(0, 1), expand = FALSE)


ggplot(AICc_weight_long, aes(x = distribution, y = AICc_weight)) +
  geom_violin(bw = .01) +
  theme_bw() +
  coord_cartesian(ylim = c(0, 1), expand = FALSE)
