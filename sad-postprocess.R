library(dplyr)
library(ggplot2)
library(tidyr)
library(magrittr)

if (!dir.exists("violins")) {
  dir.create("violins")
}

my_ggsave = function(name, plot, width = 4, height = 4, dpi = 400){
  ggsave(paste0("violins/", name), plot, width = width, height = height, dpi = dpi)
}

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

fancify = function(x){
  x = gsub("(deviance_)|(AICc_)", "", x)
  dict = c(logseries = "log-series", pln = "poisson\nlognormal", 
    negbin = "negative\nbinomial", zipf = "Zipf")
  for (i in 1:length(dict)) {
    x[x == names(dict)[i]] = dict[i]
  }
  x
}
fancify_names = function(df){
  colnames(df) = fancify(colnames(df))
  df
}

deviance_diff = (deviances[, is_dev] - rowMeans(deviances[, is_dev])) %>%
  fancify_names()
deviance_diff_long = gather(deviance_diff, key = "Distribution", value = "deviance")


AICc_diff = (deviances[, is_AICc] - rowMeans(deviances[, is_AICc])) %>%
  fancify_names()
AICc_diff_long = gather(AICc_diff, key = "Distribution", value = "AICc")

dev_plot = ggplot(deviance_diff_long, aes(x = Distribution, y = deviance)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean deviance (lower is better)")
my_ggsave(name = "deviance.png", dev_plot)


ll_plot = ggplot(deviance_diff_long, aes(x = Distribution, y = -deviance/2)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean log-likelihood")
my_ggsave(name = "loglik.png", ll_plot)

aic_plot = ggplot(AICc_diff_long, aes(x = Distribution, y = AICc)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean AICc (lower is better)")
my_ggsave(name = "aic.png", aic_plot)

relative_likelihoods = (exp(-deviance_diff / 2) / rowSums(exp(-deviance_diff / 2)))  %>%
  fancify_names()
relative_likelihoods_long = gather(relative_likelihoods, 
                                   key = Distribution, 
                                   value = relative_likelihood)



AICc_weight = (exp(-AICc_diff / 2) / rowSums(exp(-AICc_diff / 2))) %>%
  fancify_names()
AICc_weight_long = gather(AICc_weight, 
                                   key = Distribution, 
                                   value = AICc_weight) 


# Note: I had to tweak the bandwidth parameter for this plot, or zipf's splat at
# zero would be so wide that the other distributions would be invisible by comparison.
# A bandwidth much less than 0.01 on a 0-1 scale is probably undersmoothed anyway.
relative_plot = ggplot(relative_likelihoods_long, aes(x = Distribution, y = relative_likelihood)) +
  geom_violin(bw = .01) +
  theme_bw() +
  coord_cartesian(ylim = c(0, 1), expand = FALSE) + 
  ylab("Relative likelihood (higher is better)")
my_ggsave("relative.png", relative_plot)

weight_plot = ggplot(AICc_weight_long, aes(x = Distribution, y = AICc_weight)) +
  geom_violin(bw = .01) +
  theme_bw() +
  coord_cartesian(ylim = c(0, 1), expand = FALSE) + 
  ylab("AICc weight (higher is better)")
my_ggsave("weight.png", weight_plot)


# Likelihoods -------------------------------------------------------------

dev2lik = function(x){
  exp(x / -2)
}

mean(deviances$deviance_negbin - deviances$deviance_pln) / 2

round(mean(deviances$deviance_pln - deviances$deviance_logseries) / -2, 1)
round(mean(deviances$deviance_negbin - deviances$deviance_logseries) / -2, 1)

round(mean(deviances$deviance_pln - deviances$deviance_zipf) / -2, 1)
round(mean(deviances$deviance_negbin - deviances$deviance_zipf) / -2, 1)


dev2lik(mean(deviances$deviance_negbin - deviances$deviance_logseries))
dev2lik(mean(deviances$deviance_negbin - deviances$deviance_zipf))



# AICc weights ------------------------------------------------------------


median(AICc_weight$Zipf)
mean(AICc_weight$Zipf < .01)


median(AICc_weight$`negative\nbinomial`)
median(quantile(AICc_weight$`poisson\nlognormal`))

# First past the post -----------------------------------------------------

# Proportion of sites where distribution X has the lowest AICc
table(apply(AICc_diff, 1, which.min)) %>%
  structure(names = colnames(AICc_weight)) %>% 
  divide_by(nrow(AICc_weight)) %>% 
  round(3)


get_names = function(x){
  factor(gsub("^[^_]+_", "", fancify(colnames(AICc_weight))))[x]
}

png("total_wins.png", width = 1500, height = 1200, res = 300)
par(mar =  c(5, 5, 4, 2) + 0.1, mgp = c(3.5,1,0))
apply(AICc_diff, 1, which.min) %>%
  get_names() %>%
  table() %>% 
  barplot(ylab = "Number of wins", xlab = "Species abundance distribution",
          las = 1, space = 0)
dev.off()
  
winners_df = deviances %>% 
  by_row(~names(which.min(.x[ , grepl("AICc", names(.x))])), .to = "winner", .collate = "cols") %>% 
  group_by(id, winner) %>% 
  summarize(wins = n()) %>% 
  mutate(N = sum(wins)) %>% 
  mutate(panel = LETTERS[1 + (N < 1E3) + (N < 1E2)]) %>% 
  mutate(winner = fancify(winner))

library(dichromat)

ggplot(winners_df, aes(x = winner, y = wins, fill = factor(winner))) + 
  geom_bar(stat = "identity") +
  facet_wrap(~id, nrow = 4, scales = "free_y") + 
  cowplot::theme_cowplot() + 
  xlab("Species abundance distribution") + 
  ylab("Number of wins") + 
  scale_fill_manual(values = colorschemes$SteppedSequential.5[c(1, 6, 11, 16)],
                    guide = FALSE)
ggsave("wins-by-dataset.png", width = 11, height = 6)
