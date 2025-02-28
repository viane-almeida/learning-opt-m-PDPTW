#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MIT License
# 
# Copyright (c) 2025 Phillippe Samer
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


""" Unit test example

__author__ = ["Phillippe Samer"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Phillippe Samer"
__email__ = "samer@uib.no"
__status__ = "Prototype"
"""

import unittest
import pytest

from src.instance_reader import InstanceReader
from src.solution import Solution

class TestSolution(unittest.TestCase):

    def test_initialization(self):
        input_file_name = "input/Call_7_Vehicle_3.txt"
        my_reader = InstanceReader()
        my_reader.read_instance(input_file_name)

        solution = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6")

        assert True

    def test_costs(self):
        input_file_name = "input/Call_7_Vehicle_3.txt"
        my_reader = InstanceReader()
        my_reader.read_instance(input_file_name)

        solution = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6")

        fleetcost = solution.fleet_cost()
        spotchartercost = solution.spotcharter_cost()
        totalcost = solution.total_cost()

        assert(fleetcost == 564414)
        assert(spotchartercost == 1306958)
        assert(totalcost == 1871372)

    def test_feasibility(self):
        input_file_name = "input/Call_7_Vehicle_3.txt"
        my_reader = InstanceReader()
        my_reader.read_instance(input_file_name)

        solution1 = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6")
        assert(solution1.is_feasible() == True)

        solution2 = Solution(my_reader, "4 4 3 3 0 7 7 0 5 5 2 2 0 6 1 6 1")
        assert(solution2.is_feasible() == True)

        solution3 = Solution(my_reader, "5 5 4 4 0 2 2 0 3 3 0 7 7 1 1")
        assert(solution3.is_feasible() == False)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
