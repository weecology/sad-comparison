library(progress)
library(dplyr)
library(ggplot2)
library(tidyr)
library(lme4)
library(magrittr)

id = "bbs"
cutoff = 9 # Copied from the Python processing code

# Import spab data
d = read.csv(paste0("sad-data/", id, "_spab.csv"), skip = 2, header = FALSE)
colnames(d) = c('site','year','sp','ab')

# Log-likelihoods from Python
ll = read.csv(paste0("sad-data/", id, "_likelihoods.csv")) %>% arrange(site)

# Negative Binomial Log-likelihoods in R
sites = d %>% 
  group_by(site) %>% 
  summarize(S = n(), N = sum(ab)) %>% 
  filter(S > cutoff) %>%
  arrange(site) %>%
  extract2("site")

stopifnot(all(sites == ll$site))

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

nb_ll = structure(rep(NA, length(sites)), names = sites)

pb = progress_bar$new(
  format = " [:bar] :percent eta: :eta",
  total = nrow(ll), clear = FALSE, width = 60
)

for (site in sites) {
  pb$tick()
  
  ab = d[d$site == site, "ab"]
    
  opt = optim(
    c(1, log(mean(ab))),
    function(par) {
      nb_nll(ab, par[1], par[2])
    }
  )
  
  nb_ll[as.character(site)] = -opt$value
}

ll$likelihood_negbin = nb_ll




ll_long = gather(ll, key = distribution, value = log_likelihood, -(1:3))
ll_long$S_center = ll_long$S - mean(ll_long$S)
ll_long$N_center = ll_long$N - mean(ll_long$N)

model = lmer(
  log_likelihood ~ S_center * distribution + N_center * distribution + (1|site), 
  data = ll_long
)

summary(model, cor = FALSE)


ll_diff = ll
ll_diff[ , -(1:3)] = ll[ , -(1:3)] - rowMeans(ll[ , -(1:3)])
ll_diff_long = gather(ll_diff, key = distribution, value = log_likelihood, -(1:3))


ggplot(ll_diff_long, aes(x = distribution, y = log_likelihood)) + 
  geom_hline(yintercept = 0) + 
  geom_violin() + 
  theme_bw() + 
  ylab("Deviation from mean log-likelihood")


relative_likelihoods = exp(ll_diff[ , -(1:3)]) / rowSums(exp(ll_diff[ , -(1:3)]))
relative_likelihoods_long = gather(relative_likelihoods, key = distribution, value = relative_likelihood)

# Note: I had to tweak the bandwidth parameter for this plot, or zipf's splat at
# zero would be so wide that the other distributions would be invisible by comparison.
# A bandwidth much less than 0.01 on a 0-1 scale is probably undersmoothed anyway.
ggplot(relative_likelihoods_long, aes(x = distribution, y = relative_likelihood)) +
  geom_violin(bw = .01) +
  theme_bw() +
  coord_cartesian(ylim = c(0, 1), expand = FALSE)

