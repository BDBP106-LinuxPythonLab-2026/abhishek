#!/bash/bin

#Example of -e
echo "Enter filename:"
read file
if [ -e $file ]; then
	echo "File exist"
else 
	echo "File does not exist"
fi

#Example of -s
if [ -s  Heart.csv ]; then
        echo "File is non empty"
else
        echo "File is empty"
fi

#Example of -f
if [ -f Heart.csv ]; then
	echo "file is regulatory file"
else
	echo "file is not regulatory file"
fi
