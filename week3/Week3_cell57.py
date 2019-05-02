scaler = MinMaxScaler()
print(scaler.fit_transform(boston[['1stFlrSF']]))