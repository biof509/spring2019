# Downloading a data file from a remote repository
import urllib

URL = "https://dcc.icgc.org/api/v1/download?fn=/release_18/Projects/BRCA-US/protein_expression.BRCA-US.tsv.gz"
FILENAME = "brca_protein_expression.tsv.gz"

urllib.request.urlretrieve(URL, FILENAME)