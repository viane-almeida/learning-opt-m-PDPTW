#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Main file, just reading the input instance file


__author__ = ["Flaviane Almeida"]
__organization__ = "Universitetet i Bergen"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "viane202@hotmail.com"
"""

import random
import time    
import sys

from src.settings import Settings
from src.instance_reader import InstanceReader
from src.solution import Solution
from src.solution_generator import SolutionGenerator


def main():

	if len(sys.argv) < 3:
		print('Error: missing command line execution arguments')
		print('')
		print('Usage: python3 main.py [input_file_path] [random_seed_index]')
		quit()

	input_path = sys.argv[1]
	seed_idx = sys.argv[2]

	my_settings = Settings()
	my_settings.init_random_number_gen(seed_idx)
	my_reader = InstanceReader()
	my_reader.read_instance(input_path)

	include_node_costs = True

	#solution1 = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6", logging=True)
	#feasible = solution1.is_feasible(logging=True)
	#if feasible:
		#print("The fleet cost of this solution is: " + str(solution1.fleet_cost(include_node_costs)))
		#print("The spotcharter cost of this solution is: " + str(solution1.spotcharter_cost()))
		#print("The total cost of this solution is: " + str(solution1.total_cost(include_node_costs)) + "\n")

	#else:
		#print("The given solution is not feasible")
    
	#solution2 = Solution(my_reader, "4 4 3 3 0 7 7 0 5 5 2 2 0 6 1 6 1", logging=True)
	#feasible = solution2.is_feasible(logging=True)
	#print("The fleet cost of this solution is: " + str(solution2.fleet_cost(include_node_costs)))
	#print("The spotcharter cost of this solution is: " + str(solution2.spotcharter_cost()))
	#print("The total cost of this solution is: " + str(solution2.total_cost(include_node_costs)) + "\n")

    # testing the solution generator
	fabric = SolutionGenerator(my_reader)


	############################################################################
	
	initial_solution = fabric.build_trivial_solution()

	best_found = initial_solution
	best_found_cost = initial_solution.total_cost()

	for i in range(my_settings.LOCAL_SEARCH_NUM_ITERATIONS):
		new_solution = fabric.local_search_operator(best_found)
		if new_solution.is_feasible():
			new_solution_cost = new_solution.total_cost()
			if (new_solution_cost < best_found_cost):
				best_found = new_solution
				best_found_cost = new_solution_cost
				print("Found a better incumbent solution of cost ", best_found_cost)
	
	############################################################################


	# clocking the execution time
	#clock_start = time.time()
	#
	#solution_pool = fabric.try_creating_n_random_solutions(10000)
	#best_found = fabric.report_best_solution_found(solution_pool)
	#
	#clock_end = time.time()
	#elapsed_time = clock_end - clock_start
	#
	#print('execution time: {:09.5f} seconds'.format(elapsed_time))
	#print(len(solution_pool), "feasible solutions")
	#if len(solution_pool) > 0:
	#	min_val = best_found[0]
	#	min_idx = best_found[1]
	#	print("best objective found =", min_val)
	#	print("solution:", solution_pool[min_idx].str_representation)



# guard, checking if we are executing this file from the terminal
if __name__ == "__main__":
    main()
