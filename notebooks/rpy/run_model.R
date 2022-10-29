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