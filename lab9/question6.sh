#!/bin/bash

echo HOME=$HOME

echo "Calculation:"
bc << EOF
scale=5
23934/44343
EOF

echo "Files starting with D:"
ls "$HOME" | grep "D"

echo "Username in /etc/passwd:"
grep "$USER" /etc/passwd
