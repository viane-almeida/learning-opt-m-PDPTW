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


""" Search methods for the mPDPTW problem based on different mataheuristics 


__author__ = ["Flaviane Almeida"]
__organization__ = "Universitetet i Bergen"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "viane202@hotmail.com"
"""

from .instance_reader import InstanceReader
from .settings import Settings
from .solution import Solution
from .solution_generator import SolutionGenerator

import random
import copy
import math

class Search:
    """
    Class for metaheuristic-based algorithms for the mPDPTW solutions
    """

    def __init__(self,
                 input_instance: InstanceReader,
                 settings: Settings):
        """
        Default constructor method
        """
        self.instance = input_instance
        self.settings = settings

        # some convenient aliases
        self.num_vehicles = input_instance.num_vehicles
        self.num_calls = input_instance.num_calls


    def _report_best_solution_found(self,
                                    solutions: list[Solution]) -> int:
        """
        Auxiliary method, to use after the random search.
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
            return (None, None)


    def random_search(self,
                      n: int):
        """
        Try creating n solutions, and returns the best one of them (if any).
        """

        fabric = SolutionGenerator(self.instance)
        
        best_solution = Solution(self.instance, "")
        best_objective = math.inf

        for i in range(n):
            tmp = fabric.create_one_random_solution()

            solution = Solution(self.instance, tmp)

            if solution.is_feasible():
                cost = solution.total_cost()
                if cost < best_objective:
                    best_solution = solution
                    best_objective = cost

        return best_solution, best_objective


    def local_search(self):
        """
        TO DO: write this
        """

        fabric = SolutionGenerator(self.instance)

        initial_solution = fabric.build_trivial_solution()

        best_found = initial_solution
        best_found_cost = initial_solution.total_cost()
        
        for i in range(self.settings.LOCAL_SEARCH_NUM_ITERATIONS):
            new_solution = fabric.one_reinsert_operator(best_found)
            if new_solution.is_feasible():
                new_solution_cost = new_solution.total_cost()
                if (new_solution_cost < best_found_cost):
                    best_found = new_solution
                    best_found_cost = new_solution_cost
                    #print("Found a better incumbent solution of cost ", best_found_cost)

        return (best_found, best_found_cost)


    def simulated_annealing(self,
                            initial: Solution):
        """
        TO DO: write this!
        """

        generator = SolutionGenerator(self.instance)
        initial_solution = generator.build_trivial_solution()

        incumbent = initial_solution
        best_solution = initial_solution
        delta_W = [] 

        for w in range(self.settings.SA_FIRST_PHASE_NUM_ITERATIONS):
            new_solution = generator.one_reinsert_operator(incumbent)
            delta_E = (new_solution.total_cost() - incumbent.total_cost())
            if new_solution.is_feasible():
                if delta_E < 0:
                    incumbent = new_solution
                    if incumbent.total_cost() < best_solution.total_cost():
                        best_solution = incumbent  
                elif random.uniform(0,1) < self.settings.SA_FIRST_PHASE_ACCEPT_WORSE_PROB:
                    incumbent = new_solution
                    delta_W.append(delta_E)

        delta_avg = sum(delta_W)/len(delta_W)

        initial_temperature = (-delta_avg)/math.log(0.8)
        #print("initial temperature:", initial_temperature)

        alfa = ((self.settings.SA_FINAL_TEMPERATURE)/initial_temperature)**(1/9900)
        temperature = initial_temperature

        for i in range(self.settings.SA_FINAL_PHASE_NUM_ITERATIONS):
            new_solution = generator.one_reinsert_operator(incumbent)
            delta_E = new_solution.total_cost() - incumbent.total_cost()
            if new_solution.is_feasible():
                if delta_E < 0:
                    incumbent = new_solution
                    if incumbent.total_cost() < best_solution.total_cost():
                        best_solution = incumbent
                elif random.uniform(0,1) < math.exp(- delta_E / temperature):
                    incumbent = new_solution
            temperature = alfa * temperature
        #print("temperature:", temperature)

        
        return (best_solution, best_solution.total_cost())

