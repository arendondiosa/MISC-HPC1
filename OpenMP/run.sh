#!/bin/bash

num_threads=(1 2 4 8 16)

echo "Running $1"
gcc -fopenmp $1

for threads in "${num_threads[@]}"
do
    echo "Threads: $threads"
    for i in $(seq 1 $2)
    do 
        ./a.out $threads
    done
done