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


""" IO module for parsing mPDPTW instances


__author__ = ["Flaviane Almeida"]
__organization__ = "Universitetet i Bergen"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "viane202@hotmail.com"
"""

class IO:
    """
    Class for input/output operations
    """

    def __init__(self):
        """
        Default constructor method, initializing attributes from an input instance
        """
        self.num_nodes = 0
        self.num_vehicles = 0
        self.num_calls = 0

        # information about each vehicle (index starts from 1! the '-1' here is just to fill space)
        self.vehicle_home_node = [-1]
        self.vehicle_starting_time = [-1]
        self.vehicle_capacity = [-1]
        self.vehicle_compatible_calls = [-1]   # some vehicles cannot transport some cargoes

        # information about each call (index starts from 1! the '-1' here is just to fill space)
        self.call_origin = [-1]
        self.call_destination = [-1]
        self.call_size = [-1]
        self.call_cost_not_transporting = [-1]
        self.call_pickup_lb = [-1]
        self.call_pickup_ub = [-1]
        self.call_delivery_lb = [-1]
        self.call_delivery_ub = [-1]

        # will hold a travel time matrix for each vehicle (after parsing the input)
        self.travel_time_matrix = []
        self.travel_cost_matrix = []

        # time (in hours) and cost (in euro) matrices (index: vehicle x call)
        self.load_time_matrix = []
        self.load_cost_matrix = []
        self.unload_time_matrix = []
        self.unload_cost_matrix = []


    def read_instance(self, file_name):
        
        i = 0
        for line in open(file_name):
            i = i+1

            # clear leading/trailing white space
            li = line.strip()

            # skip comment lines!
            if not li.startswith("%"):
                print(line)

            if (i > 10):
                return



input_file_name = "input/Call_7_Vehicle_3.txt"
# TO DO: read input file name from terminal

my_io = IO()
my_io.read_instance(input_file_name)
