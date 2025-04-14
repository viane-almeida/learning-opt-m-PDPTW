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
from src.search import Search


def main():

	if len(sys.argv) < 3:
		print('Error: missing command line execution arguments')
		print('')
		print('Usage: python3 main.py [input_file_path] [random_seed_index] [output_file_path - optional]')
		quit()

	input_path = sys.argv[1]
	seed_idx = sys.argv[2]
	if len(sys.argv) > 3:
		output_path = sys.argv[3]

	my_settings = Settings()
	my_settings.init_random_number_gen(seed_idx)
	my_reader = InstanceReader()
	my_reader.read_instance(input_path)

	#include_node_costs = True

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

	#############################################################################

	#trivial_solution = SolutionGenerator(my_reader)
	#cost_trivial_solution = trivial_solution.build_trivial_solution().total_cost()
    
	
	engine = Search(my_reader, my_settings)
	
	############################################################################

	print("\n:: RANDOM SEARCH ::")
	clock_start = time.time()
	solution, cost = engine.random_search(my_settings.RANDOM_SEARCH_NUM_TRIALS)
	print("best objective found: ", cost)
	print("solution: ", solution.str_representation)
	
	#print("\n:: LOCAL SEARCH ::")
	#clock_start = time.time()
	#solution, cost = engine.local_search()
	#print("best objective found: ", cost)
	#print("solution: ", solution.str_representation)

	#print("\n:: SIMULATED ANNEALING ::")
	#generator = SolutionGenerator(my_reader)
	#initial_solution = generator.build_trivial_solution()
	#clock_start = time.time()
	#solution, cost = engine.simulated_annealing(initial_solution)
	#print("best objective found: ", cost)
	#print("solution: ", solution.str_representation)
	
	############################################################################

	clock_end = time.time()
	elapsed_time = clock_end - clock_start
	print('execution time:\n{:09.5f} seconds'.format(elapsed_time))

	# write cost and execution time on a file
	if len(sys.argv) > 3:
		with open(output_path, "a") as output:
			output.write('{:09.5f}    \t{:09.5f}\n'.format(cost, elapsed_time))




# guard, checking if we are executing this file from the terminal
if __name__ == "__main__":
    main()
