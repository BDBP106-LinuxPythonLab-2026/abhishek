#/bin/bash
#
echo "Enter your filename:"
read file

if [ -e $file ];then
	echo "The file exists."
	exit 200
else 
	echo "The file is not exists."
	exit 201
fi
