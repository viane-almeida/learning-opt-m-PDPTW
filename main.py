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

from instance_reader import InstanceReader
from solution import Solution
from solution_generator import SolutionGenerator

import random
import time    

def main():
	# TO DO: replace this by ten big primes and a choice of which one to use
	"""
	2442263587
	2919079211
	1192607393
	9848162447
	3646538963
	3964742447
	9781856377
	6414435113
	8693967211
	2581330943
	"""
	USE_EPOCH_AS_SEED = True

	# TO DO: read input file name from terminal

	epoch_time = int(time.time())
	if USE_EPOCH_AS_SEED:
		random.seed(epoch_time)
	else:
		random.seed(8693967211)

	input_file_name = "input/Call_7_Vehicle_3.txt"

	my_reader = InstanceReader()
	my_reader.read_instance(input_file_name)

	include_node_costs = True

	solution1 = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6", logging=True)
	feasible = solution1.is_feasible(logging=True)
	if feasible:
		print("The fleet cost of this solution is: " + str(solution1.fleet_cost(include_node_costs)))
		print("The spotcharter cost of this solution is: " + str(solution1.spotcharter_cost()))
		print("The total cost of this solution is: " + str(solution1.total_cost(include_node_costs)) + "\n")

	else:
		print("The given solution is not feasible")
	
	solution2 = Solution(my_reader, "4 4 3 3 0 7 7 0 5 5 2 2 0 6 1 6 1", logging=True)
	feasible = solution2.is_feasible(logging=True)
	print("The fleet cost of this solution is: " + str(solution2.fleet_cost(include_node_costs)))
	print("The spotcharter cost of this solution is: " + str(solution2.spotcharter_cost()))
	print("The total cost of this solution is: " + str(solution2.total_cost(include_node_costs)) + "\n")

	solution3 = Solution(my_reader, "5 5 4 4 0 2 2 0 3 3 0 7 7 1 1", logging=True)
	feasible = solution3.is_feasible(logging=True)
	if feasible:
		print("The fleet cost of this solution is: " + str(solution3.fleet_cost(include_node_costs)))
		print("The spotcharter cost of this solution is: " + str(solution3.spotcharter_cost()))
		print("The total cost of this solution is: " + str(solution3.total_cost(include_node_costs)) + "\n")

	else:
		print("The given solution is not feasible")

	# TO DO: organize the code in this main function

	# testing the solution generator
	fabric = SolutionGenerator(my_reader)
	#solution = fabric.create_one_solution()
	solution_pool = fabric.try_creating_n_solutions(10000)
	if len(solution_pool) > 0:
		best_objective_found = min([x.total_cost(include_node_costs) for x in solution_pool])
	else:
		best_objective_found = '-'
	print(len(solution_pool), ", best_objective_found = ", best_objective_found)
	
# guard, checking if we are executing this file from the terminal
if __name__ == "__main__":
    main()
