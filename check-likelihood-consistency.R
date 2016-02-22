# This script imports the (log) likelihood data file, the AICc weights data file,
# and the relative likelihood data file, then compares them to make sure they're
# consistent with one another and with the degrees of freedom vector k.
# Any inconsistencies should trigger an error when the script is run.
# It should be called from check.py


id = commandArgs(TRUE)

make_filename = function(id, value) {
  paste0("sad-data/", id, value)
}

likelihoods = read.csv(make_filename(id, "_likelihoods.csv"))
AICc = read.csv(make_filename(id, "_dist_test.csv"))
relative = read.csv(make_filename(id, "_relative_L.csv"))

k = c(logseries = 1, pln = 2, negbin = 2, geometric = 1, zipf = 1)
S = AICc$S

# First three columns should match for all three csvs ---------------------
stopifnot(
  all(likelihoods[, 1:3] == AICc[, 1:3])
)
stopifnot(
  all(likelihoods[, 1:3] == relative[, 1:3])
)


# Remove the first three columns from all three ---------------------------

likelihoods = likelihoods[ , -c(1:3)]
AICc = AICc[ , -c(1:3)]
relative = relative[ , -c(1:3)]


# relative likelihood -----------------------------------------------------

my_relative = exp(likelihoods) / rowSums(exp(likelihoods))

stopifnot(
  all.equal(my_relative, relative, check.attributes = FALSE)
)


# AICc weights ------------------------------------------------------------

calculate_aicc = function(ll, k, N){
  2 * k - 2 * ll + 2 * k * (k + 1) / (N - k - 1)
}

my_aicc = sapply(
  1:ncol(likelihoods),
  function(i){
    calculate_aicc(
      likelihoods[[i]],
      k = k[i],
      N = S
    )
  }
)
my_delta_aicc = my_aicc - apply(my_aicc, 1, min)


my_aicc_weights = exp(-1/2 * my_delta_aicc) / rowSums(exp(-1/2 * my_delta_aicc))

stopifnot(
  all.equal(my_aicc_weights, as.matrix(AICc), check.attributes = FALSE)
)

cat("  no problems found with likelihood consistency from ", id, "\n")
