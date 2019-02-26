import os

for filename in os.listdir(os.curdir):
	if filename.find('.csv')!=-1:
		with open(os.path.join(os.curdir, filename), 'r') as original: 
			data = original.read()
		with open(os.path.join(os.curdir, filename), 'w') as modified: 
			modified.write("phylum,"+str(filename.split('.')[0])+"\n" + data)