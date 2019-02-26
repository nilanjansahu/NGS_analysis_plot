import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio import Entrez
import numpy as np
from multiprocessing import Pool
from collections import ChainMap
import pickle
import json
import csv
Entrez.email = 'nilanjansahu@gmail.com'
Entrez.api_key  = '6b4ea85903bed11cf463446c049c48777c08'
def taxo(d):
    a=[]
    a.append(d)
    b={}
    handle = Entrez.efetch(db="nucleotide", id=str(d), rettype="gb")
    records = SeqIO.parse(handle, "gb")
    writerr=open('taxo1.csv','a',newline='')
    write=csv.writer(writerr,delimiter=',',escapechar=' ', quoting=csv.QUOTE_NONE)
    for i,record in enumerate(records):
        a.append(record.annotations["taxonomy"])
        a.append(record.annotations["source"].split(' ')[1])
        a=np.concatenate(a,axis=None)
        print(len(a))
        write.writerow(a)
        b[d]=np.concatenate((record.annotations["taxonomy"],record.annotations["source"].split(' ')[1]),axis=None).flatten()
    writerr.close()
    return b

if __name__ == '__main__':
    nuc_record=[]
    df=pd.read_csv('taxo.csv', header=None)
    compare=df[0].values
    print(compare)
    with open('16S', "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            if record.id not in compare:
                nuc_record.append(record.id)
    nuc_record=np.unique(nuc_record)
    print(nuc_record)
    print(len(nuc_record))
    p=Pool(10)
    a=p.map(taxo,nuc_record)

    '''
    dump_dict = dict(ChainMap(*a))
    print(dump_dict)
    pickle.dump(dump_dict, open("acc_no_taxonomy.p", "wb"))
    #json.dump(dump_dict, open('result.json', 'w'))
    '''

