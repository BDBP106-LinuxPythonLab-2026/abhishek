#!/bin/bash

echo "Enter your filename:"
read filename
if [ -e $filename ]; then
	echo "File exists."
     if  [ -x $filename ];then
        echo "File is executable"
     else
        echo "File is not executable"
fi
else
	echo "File does not exists."
fi

