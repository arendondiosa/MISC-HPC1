#!/bin/bash

matrix_limits=(1 10 100)

iter=""

echo $iter

if [ $2 ]
then
    iter=$2
fi

for length in "${matrix_limits[@]}"
do
    python $1 $length $iter
done
