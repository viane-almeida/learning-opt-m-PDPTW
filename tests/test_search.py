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


""" Unit test corresponding to the Search module

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
from src.settings import Settings
from src.solution import Solution
from src.solution_generator import SolutionGenerator
from src.search import Search

class TestSearch(unittest.TestCase):

    def test_local_search(self):

        input_file_name = "input/Call_7_Vehicle_3.txt"
        seed_idx = 2

        my_reader = InstanceReader()
        my_reader.read_instance(input_file_name)

        my_settings = Settings()
        my_settings.init_random_number_gen(seed_idx)
        
        engine = Search(my_reader, my_settings)
        engine.local_search()

        assert True


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
