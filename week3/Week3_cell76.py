# For every document we count word ocurrence:

from sklearn.feature_extraction.text import CountVectorizer
emails_in_ML_format = CountVectorizer().fit_transform(emails.data)
print(emails_in_ML_format.shape)