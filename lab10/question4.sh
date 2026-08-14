#!/bin/bash

echo "Enter a number:"
read n

if [ $n -gt 0 ]; then
        echo "The number is positive"
elif [ $n -eq 0 ]; then
	echo "The number is zero"
elif [ $n -lt 0 ];then
        echo "The number is negative"
fi
