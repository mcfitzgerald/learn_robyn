import rpy2.robjects as ro
from rpy2.robjects.packages import importr
base = importr('base')
utils = importr('utils')
#reticulate = importr('reticulate')
robyn = importr('Robyn')
#reticulate.use_virtualenv('/Users/MikeFitzgerald/Documents/Github/pi-robyn-mx/venv')
ro.globalenv['dat'] = utils.read_csv('robyn_lum_input.csv')
utils.data('dt_simulated_weekly')
base.source('robyn_lum_script.R')
ro.r('''
Sys.setenv(R_FUTURE_FORK_ENABLE="true")
options(future.fork.enable = TRUE)
''')
base.source('run_model.R')