
for d in ./tomato_disease_dataset/*; do
	i=0;
	if ! [ "$d" == "./tomato_disease_dataset/file_rename.sh" ]
	then
		for f in $d/*; do 
			((i+=1));
			mv "$f" $d/$i.jpg
		done; 
		echo $i; 
		i=0;
	fi
done
