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

	solution = Solution(my_reader, "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6")


if __name__ == "__main__":
    main()
