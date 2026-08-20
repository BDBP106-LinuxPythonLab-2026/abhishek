#!/bin/bash

val1=Jayashree
val2=Nagesh
if [ $val1 > $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi
#Here the shell interprets > as output redirection, not as a string comparison operator

val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi
#Here \> is correctly interpreted as a string comparison operator
#since J comes before N alphabetically


