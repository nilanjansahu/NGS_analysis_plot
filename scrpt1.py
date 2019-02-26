import os
import pandas as pd
df=pd.read_csv('PCA-3_labeled_phylum.csv')
for filename in os.listdir(os.curdir):
	if filename.find('.csv')!=-1:	
		df1=pd.read_csv(filename)
		df=df.merge(df1, left_on='phylum', right_on='phylum', how='outer')
df=df.transpose()
df.to_csv('out.csv',header=False)