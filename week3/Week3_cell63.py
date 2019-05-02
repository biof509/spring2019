ohe = OneHotEncoder()
sparse_matrix = ohe.fit_transform(boston[['SaleCondition', 'CentralAir_bool']])
sparse_matrix.todense()