from sklearn.datasets import fetch_20newsgroups
emails = fetch_20newsgroups(subset='train', categories=['sci.med'], shuffle=True, random_state=0)
print("Number of documents", len(emails.data))
print("Beginning of the first document", emails.data[0][:500])