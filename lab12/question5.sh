#!/bin/bash
function divide {
	local a=$1
        local b=$2

        if  [ $b -eq 0 ]; then
                echo " the number is infinite"
                return
        fi

        local quotient=$(echo "scale=2 ; $a / $b" | bc)
	local remainder=$((a % b))

        echo "Quotient = $quotient"
        echo "Remainder = $remainder"
}
divide 10 3


