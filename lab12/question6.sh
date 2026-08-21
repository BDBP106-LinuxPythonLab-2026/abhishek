#!/bin/bash

function maximum {
	local a=$1
	local b=$2

	if [ $a -gt $b ]; then
		echo "Maximum number is: $a"
	else
		echo "Maximum number is: $b"
	fi
}
maximum 44 89



