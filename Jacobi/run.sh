#!/bin/bash

num_threads=(1 2 4 8 16)

echo "Running $1"

if [ $3 == "gcc" ]
then
    $3 -fopenmp $1
elif [ $3 == "icc" ]
then
    $3 -qopenmp $1
else
    echo "No options found"
fi

for threads in "${num_threads[@]}"
do
    echo "Threads: $threads"
    for i in $(seq 1 $2)
    do 
        ./a.out $4 $4 $threads
    done
done