# This script tests two things:
#
# 1) Does sad-comparisons.py produce the correct values for site, N, and S
# 2) Do the negative binomial likelihoods match expectations (e.g. are they in the correct order
#    and approximately correct)
#
# If the script runs without errors, then it didn't find any mistakes
#
# It should be called from check.py


id = commandArgs(TRUE)

suppressPackageStartupMessages(
  library(dplyr, verbose = FALSE, quietly = TRUE)  
)


d = read.csv(paste0("sad-data/", id, "_spab.csv"), skip = 2, header = FALSE)
colnames(d) = c('site','year','sp','ab')
ll = read.csv(paste0("sad-data/", id, "_likelihoods.csv")) %>% arrange(site)

cutoff = 9 

my_df = d %>% 
  group_by(site) %>% 
  summarize(S = n(), N = sum(ab)) %>% 
  filter(S>cutoff) %>%
  arrange(site)


# Assert that site, S, N match expectations
stopifnot(all(my_df == ll[ , c("site", "S", "N")]))


# Negative binomial negative log-likelihood, truncated to exclude 0
nb_nll = function(x, log_size, log_mu) {
  size = exp(log_size)
  mu = exp(log_mu)
  
  p0 = dnbinom(0, size = size, mu = mu, log = FALSE)
  full_ll = dnbinom(x, size = size, mu = mu, log = TRUE)
  
  # Would have better numerical precision if I used logs throughout, but this is
  # good enough as a quick check
  -sum(full_ll - log(1 - p0))
}

my_ll = structure(rep(NA, nrow(my_df)), names = my_df$site)


for (site in my_df$site) {
  ab = d[d$site == site, "ab"]
  
  opt = optim(
    c(1, log(mean(ab))),
    function(par) {
      nb_nll(ab, par[1], par[2])
    }
  )
  
  my_ll[as.character(site)] = -opt$value
}


# Assert that the negative binomial likelihoods from the Python code match 
# expectations
# Numerical tolerance is a bit lax, but I attribute that to minor differences in
# which negative binomial parameter values were found by the optimizer for the 
# MLE, rather than to differences in the log-likelihood code.
stopifnot(all.equal(my_ll, ll$likelihood_negbin, check.attributes = FALSE, tol = 1E-5))


cat("  no problems found with output from ", id, "\n")
