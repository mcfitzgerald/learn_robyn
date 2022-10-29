sim.data <- SimulateAMSS(
  time.n = time.n,
  nat.mig.params = nat.mig.params, media.names = c("tv", "search"), media.modules = c(
    `DefaultTraditionalMediaModule`,
    `DefaultSearchMediaModule`),
  media.params = list(params.tv, params.search), sales.params = sales.params)
