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

from .instance_reader import InstanceReader
from .solution import Solution

import random
import copy

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

    def __convert_lists_to_string(self,
                                  lists: list[list]):
        """
        Auxiliary method to convert a list of lists representation of a solution
        into the string one (separated by 0s)
        """

        for i in range(len(lists)-1):
            lists[i].append(0)
        
        # gather the list of lists into a single list
        res = sum(lists, [])
        
        string_representation = ' '.join(str(c) for c in res)

        return string_representation


    def create_one_random_solution(self):
        """
        TO DO

        goal: generate one string such that:
                - it contains self.num_vehicles occurrences of '0'
                - it contains 2 occurrences of each number from 1 to self.num_calls, with no '0' between them
        """

        # 1. INITIALIZE NUM_VEHICLES EMPTY LISTS
        calls_for_each_vehicle = []
        for i in range(self.num_vehicles + 1):
            calls_for_each_vehicle.append([])
        #print("list of calls: ", calls_for_each_vehicle)


        # 2. FOR I IN 1,2...NUM_CALLS
        for i in range(1, self.num_calls + 1):
            # 2.1. choose a "random" vehicle (including the spot charter)
            idx = random.randint(0,self.num_vehicles)
            #print("vehicle ", idx)
            
            # 2.2. add 'i' to a "random" position in the corresponding list
            v = calls_for_each_vehicle[idx]
            v.insert(random.randint(0, len(v)), i)
            #print("list of calls ", calls_for_each_vehicle)
            
            # 2.3. add 'i' to a "random" position in the corresponding list
            v.insert(random.randint(0, len(v)), i)
        #print("list of calls ", calls_for_each_vehicle)


        # 3. CONCATENATE THE LISTS WITH A '0' BETWEEN THEM AND CONVERT TO STRING
        sequence_of_calls = self.__convert_lists_to_string(calls_for_each_vehicle)

        return sequence_of_calls


    def try_creating_n_random_solutions(self, n: int):
        """
        TO DO
        """

        # try creating n solutions, return a list of the feasible ones (NB! as Solution objects, not strings)

        solutions = []
        
        for i in range(n):
            tmp = self.create_one_random_solution()

            solution = Solution(self.instance, tmp)

            if solution.is_feasible():
                solutions.append(solution)
            
        #print(solutions)
        
        return solutions

    def report_best_solution_found(self,
                                   solutions: list[Solution]) -> int:
        """
        Returns a tuple containint the cost of the best solution in the given
        collection and the index of the corresponding solution the list.
        """

        if len(solutions) > 0:

            # will traverse the list and find the solution of mininum total cost
            min_val = solutions[0].total_cost()
            min_idx = 0

            for i in range(1, len(solutions)):
                tmp = solutions[i].total_cost()
                if tmp < min_val:
                    min_val = tmp
                    min_idx = i

            return (min_val, min_idx)

        else:
            return None



    def build_trivial_solution(self):

        """
        Returns a Solution object corresponding to the trivial solution where
        every call is outsourced
        """

        str_repr = ""
        for i in range(1, self.num_vehicles+1):
            str_repr += "0 "

        for i in range(1, self.num_calls+1):
            str_repr += str(i)
            str_repr += " "
            str_repr += str(i)
            str_repr += " "

        #print("initial solution as a string:", str_repr)
        return Solution(self.instance, str_repr)

    def one_reinsert_operator(self,
                              initial_solution: Solution):

        """
        Gets a Solution object, applies an 1-reinsert operator on it and returns
        a new Solution object
        """

        # create a copy of the argument solution using its list structures
        # NB! logical index starts from 1 (0-th item contains a -1)
        new_solution_list = copy.deepcopy(initial_solution.vehicles_call_sequence)
        new_solution_list.append( copy.deepcopy(initial_solution.calls_not_taken) )

        # 1. REMOVE 1 CALL (BOTH PICKUP AND DELIVERY)

        # choose a random non-empty vehicle (including the spotcharter)
        non_empty_vehicles = []
        for i in range(1, self.num_vehicles+2):
            if len(new_solution_list[i]) > 0:
                non_empty_vehicles.append(i)

        dice = random.randint(0, len(non_empty_vehicles)-1)
        chosen_vehicle = non_empty_vehicles[dice]

        # choose a random call from this vehicle and remove it
        dice = random.randint(0, len(new_solution_list[chosen_vehicle])-1)
        chosen_call = new_solution_list[chosen_vehicle][dice]

        # remove both calls from the chosen vehicle
        new_solution_list[chosen_vehicle].remove(chosen_call)
        new_solution_list[chosen_vehicle].remove(chosen_call)

        # 2. INSERT THE CHOSEN CALL IN A DIFFERENT VEHICLE
        new_vehicle = chosen_vehicle
        while new_vehicle == chosen_vehicle:
            dice = random.randint(1, self.num_vehicles+1)
            new_vehicle = dice

        current_len = len(new_solution_list[new_vehicle])
        if current_len == 0:
            new_solution_list[new_vehicle].append(chosen_call)
            new_solution_list[new_vehicle].append(chosen_call)
        else:
            idx = random.randint(0, current_len-1)
            new_solution_list[new_vehicle].insert(idx, chosen_call)
            idx = random.randint(0, current_len)
            new_solution_list[new_vehicle].insert(idx, chosen_call)

        # preparing the object to return: first we drop the dummy [-1]
        natural_list = new_solution_list[1:]
        
        #print("will return a Solution() from ", natural_list)

        # then get a string representation
        new_solution_as_a_string = self.__convert_lists_to_string(natural_list)

        return Solution(self.instance, new_solution_as_a_string)
