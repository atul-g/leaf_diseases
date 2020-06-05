#before this use the file_rename.sh shell script to rename all files in
#proper numerical order.

import os
import shutil

os.mkdir('./train')
os.mkdir('./test')
cwd=os.getcwd()
for dir in os.listdir('./tomato_disease_dataset'):
	file_list=os.listdir(os.path.join(cwd,'tomato_disease_dataset', dir))
	ln=len(file_list)
	train=file_list[:int(ln*0.8)]
	test=[x for x in file_list if x not in train]
	
	#moving train files:
	os.mkdir(os.path.join(cwd,'train', dir))
	for f in train:
		shutil.move(os.path.join(cwd,'tomato_disease_dataset', dir, f),os.path.join(cwd, 'train', dir, f))
		
	#moving test files:
	os.mkdir(os.path.join(cwd,'test', dir))
	for f in test:
		shutil.move(os.path.join(cwd,'tomato_disease_dataset', dir, f),os.path.join(cwd, 'test', dir, f))
	
	
print("\nDone moving files\n")
