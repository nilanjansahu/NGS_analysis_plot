import pandas as pd
import matplotlib.pyplot as plt
from Bio import Entrez
from Bio import SeqIO
import numpy as np
import csv
from multiprocessing import Pool

Entrez.email = 'nilanjansahu@gmail.com'
Entrez.api_key  = '6b4ea85903bed11cf463446c049c48777c08'


def taxo(d):
    a=[]
    a.append(d.ravel())
    
    handle = Entrez.efetch(db="nucleotide", id=str(d[0]), rettype="gb")
    records = SeqIO.parse(handle, "gb")
    writerr=open('abcd.csv','a',newline='')
    write=csv.writer(writerr,delimiter=',',escapechar=' ', quoting=csv.QUOTE_NONE)
    for i,record in enumerate(records):
        a.append(record.annotations["taxonomy"])
        a.append(record.annotations["source"].split(' ')[1])
        a=np.concatenate(a,axis=None)
        print(len(a))
        write.writerow(a)

    writerr.close()

        

if __name__ == '__main__':
    
    df=pd.read_csv('seqd1.csv', header=None)

    df[1].value_counts().plot(kind='pie')
    fil = df[1].value_counts().reset_index().values

    print(fil[0][0])
    #print(freq)

    p=Pool(10)
    p.map(taxo,fil)
                        
    '''
    plt.axis('equal')
    plt.title('freq of bacteria')
    plt.show()
    '''