#!/bin/bash

echo  -n "Enter a number: "
read n

if [ $n -gt 90 ] && [ $n -le 100 ]; then
	echo " your grade is A"
elif [ $n -gt 80 ] && [ $n -le 90 ]; then
        echo " your grade is B"
elif [ $n -ge 70 ] && [ $n -le 80 ]; then
        echo " your grade is C"
elif [ $n -lt 70 ]; then
        echo " you are fail"

fi
