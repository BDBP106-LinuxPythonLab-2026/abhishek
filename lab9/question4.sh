#!/bin/bash
echo $0
name=$1
age=$2

echo 'The first argument is: '$1
echo 'The second argument is: '$2

echo 'The number of arguments passed to this script: '$#
echo 'The list of arguments passed to this script: '$@

#we can store the arguments in an array by enclosing $@ within ()
listofarg=($@)
#Recall elements like other array
echo ${listofarg[2]}
