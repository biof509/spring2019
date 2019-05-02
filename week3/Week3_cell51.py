# boston.head()
boston["total_sf"] = boston["1stFlrSF"] + boston["2ndFlrSF"]
boston.head()