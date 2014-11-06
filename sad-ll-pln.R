library(VGAM)
library(poilog)

import_abundance = function(file_dir){
  # Read input file with columns site, year, sp, ab.
  input_file = read.csv(file_dir, colClasses = 'character',
                        header = F, comment.char = '#', col.names = c('site', 'year', 'sp', 'ab'))
  input_file$ab = as.numeric(input_file$ab)
  return(input_file)
}

get_pars_poilog = function(ab){
  pars = as.numeric(poilogMLE(ab, startVals = c(mu = mean(log(ab)), sig = sd(log(ab))))$par)
  return(pars)
}

log_lik_poilog = function(ab, pars){
  # Log-liklihood computed with dpoilog
  return(sum(log(dpoilog(ab, pars[1], pars[2]))))
}

log_lik_polono = function(ab, pars){
  return(sum(log(dpolono(ab, pars[1], pars[2]))))
}

get_lik_poilog_2vers = function(input_file, dataset_name, data_dir, cutoff = 9){
  # Computes the loglikelihood of Poisson lognormal for each site 
  # and write to file. Parameters are estimated with poilogMLE. 
  # Likelihood is calculated using 1. dpoilog and 2. dpolono.
  out_file = data.frame(site = character(0), likelihood_poilog = numeric(0), 
                        likelihood_polono = numeric(0), stringsAsFactors = F)
  irow = 1
  sites = sort(unique(input_file$site))
  for(site in sites){
    dat_site = input_file[input_file$site == site, ]
    N = sum(dat_site$ab)
    S = dim(dat_site)[1]
    if (S > cutoff){
      ab_site = as.numeric(dat_site$ab)
      pars_site = get_pars_poilog(ab_site)
      ll_poilog = log_lik_poilog(ab_site, pars_site)
      ll_polono = log_lik_polono(ab_site, pars_site)
      out_file[irow, 1] = site
      out_file[irow, 2] = ll_poilog
      out_file[irow, 3] = ll_polono
      irow = irow + 1
    }
  }
  out_name = paste(data_dir, dataset_name, '_ll_pln.csv', sep = '')
  write.csv(out_file, out_name, row.names = F, quote = F)
}