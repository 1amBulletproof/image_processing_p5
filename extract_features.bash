#!/bin/bash

for f in *.jpg;
do
    python2 ../extract_features.py $f >> ../$1 ;
done;
