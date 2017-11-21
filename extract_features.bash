#!/bin/bash

for f in *.jpg; 
do 
    echo $f; 
    python2 ../extract_features.py $f >> ../$1; 
done
