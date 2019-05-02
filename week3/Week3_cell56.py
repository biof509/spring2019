# a = (boston['1stFlrSF'] - boston['1stFlrSF'].mean()) / boston['1stFlrSF'].std()
# boston['1stFlrSF'].hist()
# boston.head()
## boston.total_sf.hist()
from sklearn.preprocessing import scale, StandardScaler, MinMaxScaler

scaler = StandardScaler()
print(scaler.fit_transform(boston[['1stFlrSF']]))
#scaled_size = pd.Series(scale(boston.total_sf))
#scaled_size.hist()
#scaled_size.mean()
#scaled_size.std(ddof=0)
#boston["normalized_total_sf"] = scaled_size