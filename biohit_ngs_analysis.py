from Bio import Entrez
from Bio import SeqIO
import os
import pandas as pd
import numpy as np
from Bio.Blast.Applications import NcbiblastnCommandline
from multiprocessing import Pool
import multiprocessing
import matplotlib.pyplot as plt

sampling=1
query='p-IGH-10_Consensus.fa'

t=os.system(str(NcbiblastnCommandline(cmd='blastn', out='seq_d.csv', outfmt=10, query=query, db='16s', evalue=1 ,num_threads=multiprocessing.cpu_count() ,max_target_seqs=sampling)))
del t


df=pd.read_csv('seq_d.csv', header=None)

df[1].value_counts().plot(kind='pie')
plt.axis('equal')
plt.title('freq of bacteria')
plt.show()
plt.savefig('abcd.png')