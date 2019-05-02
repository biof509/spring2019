import sqlalchemy as sa
# Connect to UCSC genomic database
engine = sa.create_engine('mysql+pymysql://genome@genome-mysql.cse.ucsc.edu/hg38', poolclass=sa.pool.NullPool)
# select 3 SNPs from Chromosome Y
pd.read_sql("SELECT * FROM snp147Common WHERE chrom='chrY' LIMIT 3", engine)