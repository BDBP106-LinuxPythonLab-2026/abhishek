#!/bin/bash

str=$1
if [ -n $str ]; then
        echo "string is not empty"
else
        echo "string is empty"
fi



str=$1
if [ -z $str ]; then
        echo "string is empty"
else
        echo "string is not empty"
fi

