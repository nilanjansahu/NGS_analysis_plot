from Bio.Blast.Applications import NcbiblastnCommandline
#file list provided in abcd array
abcd=['PCA-3_labeled.fa','p-IGH-12_labeled.fa','p-IGH-18_labeled.fa','P-IGH-2_labeled.fa','P-IGH-9_labeled.fa','PCA-5_labeled.fa','p-IGH-13_labeled.fa','p-IGH-19_labeled.fa','P-IGH-4_labeled.fa','p-IGH-10_Consensus.fa','p-IGH-14_labeled.fa','P-IGH-1_labeled.fa',' P-IGH-6_labeled.fa','P-IGH-10_labeled.fa','p-IGH-15_labeled.fa','p-IGH-20_labeled.fa','P-IGH-7_labeled.fa','P-IGH-11_labeled.fa','p-IGH-16_labeled.fa','p-IGH-21_labeled.fa','P-IGH-8_labeled.fa']
for a in abcd:
	sampling=1
	query=a
	outl=str(a+'.csv')
	t=os.system(str(NcbiblastnCommandline(cmd='blastn', out=outl, outfmt=10, query=query, db='16s', evalue=1 ,num_threads=multiprocessing.cpu_count() ,max_target_seqs=sampling)))
	del t


 
    