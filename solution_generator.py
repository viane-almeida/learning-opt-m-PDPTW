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


""" Random solution generator for the mPDPTW problem


__author__ = ["Flaviane Almeida"]
__organization__ = "Universitetet i Bergen"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "viane202@hotmail.com"
"""

from instance_reader import InstanceReader
from solution import Solution

import random

class SolutionGenerator:
    """
    Class for generating random mPDPTW solutions
    """

    def __init__(self,
                 input_instance: InstanceReader):
        """
        Default constructor method
        """
        self.instance = input_instance

        # some convenient aliases
        self.num_vehicles = input_instance.num_vehicles
        self.num_calls = input_instance.num_calls

        # TO DO: what else?


    def create_one_solution(self):
        """
        TO DO

        goal: generate one string such that:
                - it contains self.num_vehicles occurrences of '0'
                - it contains 2 occurrences of each number from 1 to self.num_calls, with no '0' between them
        """

        # 1. initialize num_vehicles empty lists
        calls_for_each_vehicle = []
        for i in range(self.num_vehicles + 1):
            calls_for_each_vehicle.append([])
        #print("list of calls: ", calls_for_each_vehicle)


        # 2. for i in 1,2...num_calls
        for i in range(1, self.num_calls + 1):
            # 2.1. choose a "random" vehicle (including the spot charter) from 1 to num_vehicles
            idx = random.randint(0,self.num_vehicles)
            #print("vehicle ", idx)
            
            # 2.2. add 'i' to a "random" position in the corresponding list
            v = calls_for_each_vehicle[idx]
            v.insert(random.randint(0, len(v)), i)
            #print("list of calls ", calls_for_each_vehicle)
            
            # 2.3. add 'i' to a "random" position in the corresponding list
            v.insert(random.randint(0, len(v)), i)
        #print("list of calls ", calls_for_each_vehicle)


        # 3. concatenate the lists with a '0' between them and convert to string

        for i in range(len(calls_for_each_vehicle)-1):
            calls_for_each_vehicle[i].append(0)
        #print("list of calls with zeros", calls_for_each_vehicle)

        res = sum(calls_for_each_vehicle, [])
        #print(res)

        sequence_of_calls = ' '.join(str(c) for c in res)
        #print("sequence of calls:", sequence_of_calls)

        return sequence_of_calls


    def try_creating_n_solutions(self, n: int):
        """
        TO DO
        """

        # try creating n solutions, return a list of the feasible ones (NB! as Solution objects, not strings)

        solutions = []
        
        for i in range(n):
            tmp = self.create_one_solution()

            solution = Solution(self.instance, tmp)

            if solution.is_feasible():
                solutions.append(solution)
            
        #print(solutions)
        
        return solutions

