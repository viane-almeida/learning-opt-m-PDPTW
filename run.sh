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

# Experiment for random search
num_runs=10
output_file="output_rs.txt"  # standard output, with solution etc.
xp_file="xp_rs.txt"          # only two columns: objective and running time

# Experiment for local search
#num_runs=10
#output_file="output_ls.txt"  # standard output, with solution etc.
#xp_file="xp_ls.txt"          # only two columns: objective and running time

# Experiment for simulated annealing
#num_runs=10
#output_file="output_sa.txt"  # standard output, with solution etc.
#xp_file="xp_sa.txt"          # only two columns: objective and running time

idx=1
for path in "${all_instances[@]}";
do
    for (( run=1; run<=num_runs; run++ ));
    do
        timestamp=$(date)
        echo "[$timestamp] instance $idx/${#all_instances[@]}:  $path  [run $run]"
        echo "[$timestamp] instance $idx/${#all_instances[@]}:  $path  [run $run]" >> "$output_file"

        # capture terminal output to file
        #output=$(python3 main.py  $path  $run  $xp_file  >> "$output_file" 2>&1)
        
        # leave standard output to the terminal
        output=$(python3 main.py  $path  $run  $xp_file)
        echo "$output"
    done

    ((++idx))
done

