import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
sns.set(style="ticks")

df = pd.read_csv('out.csv')
for e in list(df)[2::]:
    
    plt.figure()
    sns.stripplot(x='data', y=e, data=df, hue='unsupervised kmeans=3' , jitter=True,edgecolor='none') 
    
    
    plt.savefig(str(e))
    


