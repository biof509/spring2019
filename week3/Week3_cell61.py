from sklearn.preprocessing import OneHotEncoder, LabelBinarizer

lb = LabelBinarizer()
lb.fit_transform(['yes', 'yes', 'no', 'no'])          