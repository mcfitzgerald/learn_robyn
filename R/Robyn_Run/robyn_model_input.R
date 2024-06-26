#!/usr/bin/env Rscript

library("reticulate")

use_virtualenv(virtualenv = "/Users/MikeFitzgerald/venvs/pydev", required = TRUE)

library(Robyn)

Sys.setenv(R_FUTURE_FORK_ENABLE="true")
options(future.fork.enable = TRUE)

dat <- read.csv("robyn_model_data.csv")

data("dt_prophet_holidays")

robyn_object <- "robyn_model.RDS"




InputCollect <- robyn_inputs(
   dt_input = dat
  ,dt_holidays = dt_prophet_holidays
  ,date_var = "Date" # date format must be "2020-01-01"
  ,dep_var = "Total_Sales_A" # there should be only one dependent variable
  ,dep_var_type = "revenue" # "revenue" (ROI) or "conversion" (CPA)
  #,prophet_vars = c( "trend",  "season",  "holiday")# "trend","season", "weekday" & "holiday" # nolint # nolint
  #,prophet_country = "US" # input one country. dt_prophet_holidays includes 59 countries by default
  ,context_vars = c( "Total_Sales_B") # e.g. competitors, discount, unemployment etc
  ,paid_media_spends = c( "tv_A",  "web_A") # mandatory input
  ,paid_media_vars = c( "tv_A",  "web_A") # mandatory.
  # paid_media_vars must have same order as paid_media_spends. Use media exposure metrics like
  # impressions, GRP etc. If not applicable, use spend instead.
  ,window_start = "2022-01-02"
  ,window_end = "2025-12-21"
  ,adstock = "geometric"
  )

hyperparameters <- list(
   tv_A_alphas = c(0.1, 5), # Increased range
   tv_A_gammas = c(0.1, 1), # Increased range
   tv_A_thetas = c(0, 0.5), # Increased range

   web_A_alphas = c(0.1, 5), # Increased range
   web_A_gammas = c(0.1, 1), # Increased range
   web_A_thetas = c(0, 0.5)  # Increased range
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
print(OutputModels)

OutputCollect <- robyn_outputs(
  InputCollect, OutputModels
  , pareto_fronts = 3
  # , calibration_constraint = 0.1 # range c(0.01, 0.1) & default at 0.1
  , csv_out = "pareto" # "pareto" or "all"
  , clusters = TRUE # Set to TRUE to cluster similar models by ROAS. See ?robyn_clusters
  , plot_pareto = TRUE # Set to FALSE to deactivate plotting and saving model one-pagers
  , plot_folder = robyn_object # path for plots export
)
print(OutputCollect)

ExportedModel <- robyn_save(
  robyn_object = robyn_object # model object location and name
  , InputCollect = InputCollect
  , OutputCollect = OutputCollect
)
print(ExportedModel)

save.image(file = "robyn_model.RData")