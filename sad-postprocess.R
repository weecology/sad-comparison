library(progress)
library(dplyr)
library(ggplot2)
library(tidyr)
library(lme4)
library(magrittr)

ids = c("Actinopterygii", "Amphibia", "Arachnida", "bbs", "cbc", "Coleoptera", 
        "fia", "gentry", "mcdb", "naba", "Reptilia")
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
  cat("postprocessing: ", id, "\n")
  
  # Import spab data
  spab = read.csv(paste0("sad-data/chapter1/", id, "_spab.csv"), skip = 2, header = FALSE, stringsAsFactors = FALSE)
  colnames(spab) = c('site','year','sp','ab')
  
  # Log-likelihoods from Python
  results = read.csv(paste0("sad-data/", id, "_likelihood_results.csv"), stringsAsFactors = FALSE) %>% arrange(site)
  
  # Drop relative likelihoods and AICc weights; they'll need to be recomputed 
  # when the negative binomial values change below.
  # Then multiply the likelihoods by -2 to get deviances
  results = select(results, -matches("relative|AICc")) %>%
    mutate_each(funs(-2*.), matches("likelihood"))
  
  # Rename the columns to reflect change to deviance
  colnames(results) = gsub("likelihood", "deviance", colnames(results))
  
  # Start calculating negative Binomial deviances in R
  sites = spab %>% 
    group_by(site) %>% 
    summarize(S = n(), N = sum(ab)) %>% 
    filter(S > cutoff) %>%
    arrange(site) %>%
    extract2("site")
  
  stopifnot(all(sites == results$site))
  
  # Initialize an empty deviance vector
  nb_deviance = structure(rep(NA, length(sites)), names = sites)
  
  for (site in sites) {
    ab = spab[spab$site == site, "ab"]
    
    opt = optim(
      c(1, log(mean(ab))),
      function(par) {
        nb_nll(ab, par[1], par[2])
      },
      method = "BFGS"
    )
    
    p0 = dnbinom(0, size = exp(opt$par[1]), mu = exp(opt$par[2]), log = FALSE)
    
    # If p0 is too close to 1, we can get a severe loss of precision when 
    # we truncate the zeros off the distribution.
    # See https://github.com/weecology/macroecotools/issues/40
    # but note that the parameterization is different (size/mu versus size/prob)
    if (1 - p0 < 1E-10) {
      # Try a different optimizer and see if we get a value that's not stuck
      # near zero
      opt = optim(
        c(1, log(mean(ab))),
        function(par) {
          nb_nll(ab, par[1], par[2])
        },
        method = "Nelder-Mead"
      )
      
      p0 = dnbinom(0, size = exp(opt$par[1]), mu = exp(opt$par[2]), log = FALSE)
    }
    
    # Test again with the new values
    if (1 - p0 < 1E-10) {
      warning("p0 is too close to 1 in ", id, " site ", site)
    }
    
    
    # Save the deviance (2 * negative loog-likelihood)
    nb_deviance[as.character(site)] = 2 * opt$value
  }
  
  results$deviance_negbin = nb_deviance
  
  deviances = select(results, matches("deviance"))
  
  distribution_names = gsub(".*_", "", colnames(deviances))
  
  # Initialize AICc data with same shape as log_likelihoods and new column names
  AICcs = NA * deviances
  colnames(AICcs) = gsub("deviance", "AICc", colnames(AICcs))
  
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
    AICcs[ , i] = calculate_aicc(-1/2 * deviances[ , i], k = k[i], N = results$S)
  }
  
  # make sure that all site names are character vectors so they can be
  # fed to bind_rows with the same class
  out = cbind(id = id, results, AICcs, stringsAsFactors = FALSE)
  out$site = as.character(out$site)
  
  out
}

# Call the postprocessing function on all the data sets
deviance_list = lapply(ids, postprocess)
deviances = bind_rows(deviance_list)

is_dev = grepl("deviance", colnames(deviances))
is_AICc = grepl("AICc", colnames(deviances))

deviance_diff = deviances[, is_dev] - rowMeans(deviances[, is_dev])
deviance_diff_long = gather(deviance_diff, key = "distribution", value = "deviance")

AICc_diff = deviances[, is_AICc] - rowMeans(deviances[, is_AICc])
AICc_diff_long = gather(AICc_diff, key = "distribution", value = "AICc")

ggplot(deviance_diff_long, aes(x = distribution, y = deviance)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean deviance (lower is better)")

ggplot(AICc_diff_long, aes(x = distribution, y = AICc)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean AICc (lower is better)")


relative_likelihoods = exp(-deviance_diff / 2) / rowSums(exp(-deviance_diff / 2))
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
  coord_cartesian(ylim = c(0, 1), expand = FALSE) + 
  ylab("Relative likelihood (higher is better)")


ggplot(AICc_weight_long, aes(x = distribution, y = AICc_weight)) +
  geom_violin(bw = .01) +
  theme_bw() +
  coord_cartesian(ylim = c(0, 1), expand = FALSE) + 
  ylab("AICc weight (higher is better)")



# First past the post -----------------------------------------------------

# Proportion of sites where distribution X has the lowest AICc
table(apply(AICc_diff, 1, which.min)) %>%
  structure(names = colnames(AICc_weight)) %>% 
  divide_by(nrow(AICc_weight)) %>% 
  round(3)


get_names = function(x){
  factor(gsub("^[^_]+_", "", colnames(AICc_weight)))[x]
}

pdf("total-wins.pdf")
par(mar =  c(5, 5, 4, 2) + 0.1, mgp = c(3.5,1,0))
apply(AICc_diff, 1, which.min) %>%
  get_names() %>%
  table() %>% 
  barplot(ylab = "Number of wins", xlab = "Species abundance distribution",
          las = 1, space = 0)
dev.off()

pdf("wins-by-dataset.pdf", width = 13)
par(mar =  c(5, 5, 4, 2) + 0.1, mgp = c(3.5,1,0))
par(mfrow = c(3, 4))
for (df in deviance_list) {
  df %>%
    select(matches("AICc")) %>%
    apply(1, which.min) %>% 
    get_names() %>% 
    table() %>% 
    barplot(ylab = "Number of wins", xlab = "Species abundance distribution",
            las = 1, space = 0)
  title(df$id[[1]])
}
dev.off()
