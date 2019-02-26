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
    writerr=open(str(file+'.analysis_fro.csv'),'a',newline='')
    write=csv.writer(writerr,delimiter=',',escapechar=' ', quoting=csv.QUOTE_NONE)
    for j in fil:
        try:
            a=df[df[0]==str(j[0])].values[0]
            #otus=' '.join(df_file[df_file[1]==str(j[0])][0].values)
            wr=[]
            wr.append(j.flatten())
            #wr.append(otus)
            y=[x for x in a[1:] if x is not np.nan]
            #print(y)
            cde='|'.join(list(y))
            wr.append(cde)
            
            wr=np.concatenate(wr,axis=None).flatten()
            #print(wr)
            write.writerow(wr)
        except:
            handle = Entrez.efetch(db="nucleotide", id=str(j[0]), rettype="gb")
            records = SeqIO.parse(handle, "gb")
            for i,record in enumerate(records):
                
                a=record.annotations["taxonomy"]
                print(str(j[0])+','+','.join(a))
               
                wr=[]
                wr.append(j.flatten())
                #wr.append(otus)
                dsf='|'.join(a)
                wr.append(dsf)
                wr=np.concatenate(wr,axis=None).flatten()
                print(wr)
                print(len(wr))
                write.writerow(wr)
                
        
    writerr.close()

if __name__ == '__main__':
    files_to=np.loadtxt('files_to.txt',dtype=str)
    print(files_to)
    p=Pool(20)
    p.map(file_analysis,files_to)
    p.close()
    
    #file_analysis('p-IGH-10_Consensus.fa.csv')
        

