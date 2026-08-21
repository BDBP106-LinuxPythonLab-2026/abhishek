#!/bin/bash

read -p "Enter a number:" num
i=1
until [ $i -gt 15 ]
do
	echo "$num x $i = $((num*i))"
	((i+=1))
done

