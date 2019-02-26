import pandas as pd
import os
import numpy as np
import csv
from multiprocessing import Pool
import math
from Bio import SeqIO
from Bio import Entrez
Entrez.email = 'nilanjansahu@gmail.com'
Entrez.api_key  = '6b4ea85903bed11cf463446c049c48777c08'
#def taxonomy_hit(file_name,):

def file_analysis(file):
    df=pd.read_csv('taxo.csv', header=None)
    df_file=pd.read_csv(file, header=None)
    fil = df_file[1].value_counts().reset_index().values
    #print(fil)
    writerr=open(str(file+'.analysis.csv'),'a',newline='')
    write=csv.writer(writerr,delimiter=',',escapechar=' ', quoting=csv.QUOTE_NONE)
    for j in fil:
        try:
            a=df[df[0]==str(j[0])].values[0]
            otus=' '.join(df_file[df_file[1]==str(j[0])][0].values)
            wr=[]
            wr.append(j.flatten())
            wr.append(otus)
            y=[x for x in a[1:] if x is not np.nan]
            #print(y)
            wr.append(y)
            wr=np.concatenate(wr,axis=None).flatten()
            #print(wr)
            write.writerow(wr)
        except:
            handle = Entrez.efetch(db="nucleotide", id=str(j[0]), rettype="gb")
            records = SeqIO.parse(handle, "gb")
            for i,record in enumerate(records):
                a=[]
                a.append(record.annotations["taxonomy"])
                a.append(record.annotations["source"].split(' ')[1])
                try:
                    otus=' '.join(df_file[df_file[1]==str(j[0])][0].values)
                except:
                    otus=' '
                wr=[]
                wr.append(j.flatten())
                wr.append(otus)
                wr.append(a)
                wr=np.concatenate(wr,axis=None).flatten()
                #print(wr)
                write.writerow(wr)
        
    writerr.close()

if __name__ == '__main__':
    '''
    files_to=np.loadtxt('files_to.txt',dtype=str)
    #print(files_to)
    p=Pool(10)
    a=p.map(file_analysis,files_to)
    
    for file in files_to:
    '''
    file_analysis('p-IGH-10_Consensus.fa.csv')
    