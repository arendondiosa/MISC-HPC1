#!/bin/bash

matrix_limits=(50 100 150 200 250 300 400 500 1000 2000)

iter=""

if [ $2 ]
then
    iter=$2
fi

for length in "${matrix_limits[@]}"
do
    python $1 $length $iter
done
