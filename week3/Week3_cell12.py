import pandas as pd

# Let's read with pandas
# Note that we do not even need to unzip the file before opening!
brca_data = pd.read_table(FILENAME, sep="\t")
brca_data.head(1)