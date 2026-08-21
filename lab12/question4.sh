#!/bin/bash
echo "2 3 5 7" > nums.txt
read -ra numbers < nums.txt
echo "The numbers in the array are: ${numbers[@]}"

echo -n "Double of each numbers: "
for i in "${numbers[@]}"
do
	echo -n "$[$i * 2] "
done

echo
