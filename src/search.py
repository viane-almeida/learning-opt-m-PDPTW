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

        # ONDE SE LE NewSolution <= operator(Incumbent) A GENTE FAZ
        #YYY = generator.one_reinsert_operator(XXX)