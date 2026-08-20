#!/bin/bash

#1
var1="Testing"
var2="testing"

#2
if [ $var1 \> $var2 ]; then

#3
	echo "var1 is greater than var2"
else
	echo "var1 is lesser than var2"
fi

#4
echo -e "$var1\n$var2" > teststringfile

#5
sort teststringfile
#The if string comparison and sort can use different ordering rules for uppercase/lowercase characters depending on the shell
#Small alphabets>Capital alphabets    

