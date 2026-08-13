#!/bin/bash

m=1
c=3*10^8
E=$(bc << EOF
$m*$c*$c
EOF
)
echo " Energy mass equivalent to: $E J"
