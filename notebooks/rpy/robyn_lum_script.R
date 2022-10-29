
#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library("reticulate")

use_virtualenv(args[1])

library(Robyn)

dat <- read.csv("robyn_lum_input.csv")
data("dt_prophet_holidays")

robyn_object <- "robyn_lum.RDS"


InputCollect <- robyn_inputs(
   dt_input = dat
  ,dt_holidays = dt_prophet_holidays
  ,date_var = "DATE" # date format must be "2020-01-01"
  ,dep_var = "TP_LUMINOUS_SALES_VALUE" # there should be only one dependent variable
  ,dep_var_type = "revenue" # "revenue" (ROI) or "conversion" (CPA)
  ,prophet_vars = c( "trend",  "season",  "holiday")# "trend","season", "weekday" & "holiday"
  ,prophet_country = "MX" # input one country. dt_prophet_holidays includes 59 countries by default
  ,context_vars = c( "TP_LUMINOUS_AVG_PRICE",  "TP_COLGATE_NOAD_AVG_PRICE",  "TP_COMPETITORS_AVG_PRICE",  "TP_COMPETITORS_SALES_VALUE") # e.g. competitors, discount, unemployment etc
  ,paid_media_spends = c( "TV_LUMINOUS_SPEND",  "GL_LUMINOUS_SPEND",  "FB_LUMINOUS_SPEND",  "DV_LUMINOUS_SPEND") # mandatory input
  ,paid_media_vars = c( "TV_LUMINOUS_TRP",  "GL_LUMINOUS_IMPRESSIONS",  "FB_LUMINOUS_IMPRESSIONS",  "DV_LUMINOUS_IMPRESSIONS") # mandatory.
  # paid_media_vars must have same order as paid_media_spends. Use media exposure metrics like
  # impressions, GRP etc. If not applicable, use spend instead.
  ,window_start = "2018-01-22"
  ,window_end = "2022-02-21"
  ,adstock = "geometric"
  )

hyperparameters <- list(
   
   TV_LUMINOUS_SPEND_alphas = c(0.5,3), 
   TV_LUMINOUS_SPEND_gammas = c(0.3,1), 
   TV_LUMINOUS_SPEND_thetas = c(0,0.3), 
   
   GL_LUMINOUS_SPEND_alphas = c(0.5,3), 
   GL_LUMINOUS_SPEND_gammas = c(0.3,1), 
   GL_LUMINOUS_SPEND_thetas = c(0,0.3), 
   
   FB_LUMINOUS_SPEND_alphas = c(0.5,3), 
   FB_LUMINOUS_SPEND_gammas = c(0.3,1), 
   FB_LUMINOUS_SPEND_thetas = c(0,0.3), 
   
   DV_LUMINOUS_SPEND_alphas = c(0.5,3), 
   DV_LUMINOUS_SPEND_gammas = c(0.3,1), 
   DV_LUMINOUS_SPEND_thetas = c(0,0.3)
   )

plot_adstock(plot = FALSE)
plot_saturation(plot = FALSE)

InputCollect <- robyn_inputs(InputCollect = InputCollect, hyperparameters = hyperparameters)
print(InputCollect)

OutputModels <- robyn_run(
  InputCollect = InputCollect # feed in all model specification
  #, cores = NULL # default
  #, add_penalty_factor = FALSE # Untested feature. Use with caution.
  , iterations = 2000 # recommended for the dummy dataset
  , trials = 5 # recommended for the dummy dataset
  , outputs = FALSE # outputs = FALSE disables direct model output
)
