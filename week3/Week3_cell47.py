# Imputation is a general technique for "guessing" appropriate missing values
# It could be implemented as a complex ML regression algorithm or a simple 'take an average' strategy.
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
imputer.fit_transform(boston[["LotFrontage"]])