#!/usr/bin/env bash 
echo Updating from $1 to $2
./updatefw.py $1
./updatefw.py $2
