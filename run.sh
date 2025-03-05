#!/bin/bash

# Initialize the all_instances array with the file paths
all_instances=(
    "./input/Call_7_Vehicle_3.txt"
    "./input/Call_18_Vehicle_5.txt"
    "./input/Call_35_Vehicle_7.txt"
    "./input/Call_80_Vehicle_20.txt"
    "./input/Call_130_Vehicle_40.txt"
    "./input/Call_300_Vehicle_90.txt"
)

# Experiment for Assignment #2
num_runs=10
output_file="xp2.out"

idx=1
for path in "${all_instances[@]}";
do
    for (( run=1; run<=num_runs; run++ ));
    do
        timestamp=$(date)
        echo "[$timestamp] instance $idx/${#all_instances[@]}:  $path  [run $run]"
        echo "[$timestamp] instance $idx/${#all_instances[@]}:  $path  [run $run]" >> "$output_file"

        output=$(python3 main.py  $path  $run  >> "$output_file" 2>&1)
        echo "$output"
    done

    ((++idx))
done

