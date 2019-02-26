import pandas as pd
import os
from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
import csv
def file_analysis_to_plot(file):
    
    df=pd.read_csv(file,header=None).values
    file_name=file.split('.')[0]
    #print(df)
    writerr=open(str(file+'.analysis.csv'),'a',newline='')
    write=csv.writer(writerr,delimiter=',',escapechar=' ', quoting=csv.QUOTE_NONE)
    for e in df:
        for j in range(int(e[1])):
            wr=[]
            wr.append(e[0])
            wr.append(e[2])
            wr.append(e[3])
            wr.append(e[4])
            write.writerow(wr)
    writerr.close()
    d_f=pd.read_csv(str(file+'.analysis.csv'), header=None)
    os.remove(str(file+'.analysis.csv'))
    os.mkdir(file_name)
    
    d_f[1].value_counts(normalize=True).to_csv(os.path.join(file_name,file_name+'_phylum.csv'),header=None)
    d_f[2].value_counts(normalize=True).to_csv(os.path.join(file_name,file_name+'_genus.csv'),header=None)
    d_f[3].value_counts(normalize=True).to_csv(os.path.join(file_name,file_name+'_species.csv'),header=None)
    
    

if __name__ == '__main__':
    files_to=np.loadtxt('files_to.txt',dtype=str)
    #print(files_to)
    p=Pool(20)
    a=p.map(file_analysis_to_plot,files_to)
    p.close()
