#!/bin/bash
# Getting the username of the logged_in_user
logged_in_user=$(whoami)
# Checking if the user is logged in
if [ -n "$logged_in_user" ]; then
     echo "The logged_in_user is: $logged_in_user"
else
     echo "User is not logged in"
fi
