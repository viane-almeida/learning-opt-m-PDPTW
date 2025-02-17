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

def main():
	# TO DO: read input file name from terminal
	input_file_name = "input/Call_7_Vehicle_3.txt"

	my_reader = InstanceReader()
	my_reader.read_instance(input_file_name)

	include_node_costs = True

	solution1 = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6")
	feasible = solution1.is_feasible(logging=True)
	if feasible:
		print("The fleet cost of this solution is: " + str(solution1.fleet_cost(include_node_costs)))
		print("The spotcharter cost of this solution is: " + str(solution1.spotcharter_cost()))
		print("The total cost of this solution is: " + str(solution1.total_cost(include_node_costs)) + "\n")

	else:
		print("The given solution is not feasible")
	
	solution2 = Solution(my_reader, "4 4 3 3 0 7 7 0 5 5 2 2 0 6 1 6 1")
	feasible = solution2.is_feasible(logging=True)
	print("The fleet cost of this solution is: " + str(solution2.fleet_cost(include_node_costs)))
	print("The spotcharter cost of this solution is: " + str(solution2.spotcharter_cost()))
	print("The total cost of this solution is: " + str(solution2.total_cost(include_node_costs)) + "\n")

	solution3 = Solution(my_reader, "5 5 4 4 0 2 2 0 3 3 0 7 7 1 1")
	feasible = solution3.is_feasible(logging=True)
	if feasible:
		print("The fleet cost of this solution is: " + str(solution3.fleet_cost(include_node_costs)))
		print("The spotcharter cost of this solution is: " + str(solution3.spotcharter_cost()))
		print("The total cost of this solution is: " + str(solution3.total_cost(include_node_costs)) + "\n")

	else:
		print("The given solution is not feasible")

	
# guard, checking if we are executing this file from the terminal
if __name__ == "__main__":
    main()
