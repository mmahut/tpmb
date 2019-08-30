#!/usr/bin/env bash 
echo Updating from $1 to $2
./control.py $1
./control.py $2
