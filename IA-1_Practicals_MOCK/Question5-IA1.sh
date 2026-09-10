#!/bin/bash

function Arguments {
read -p "Enter a argument1:" $1
read -p "Enter a argument2:" $2
read -p "Enter a argument3:" $3
read -p "Enter a argument3:" $4

until [ ${Arguments[#]} -lt 5 ]
do
  echo " Argument1: $1"
  echo " Argument1: $2"
  echo " Argument1: $3"
  echo " Argument1: $4"
done

}
Arguments $1 $2 $3 $4 


