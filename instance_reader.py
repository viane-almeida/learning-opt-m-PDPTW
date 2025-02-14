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


""" InstanceReader module for parsing mPDPTW instances


__author__ = ["Flaviane Almeida"]
__organization__ = "Universitetet i Bergen"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "viane202@hotmail.com"
"""

class InstanceReader:
    """
    Class for handling the input instance file
    """

    def __init__(self):
        """
        Default constructor method, initializing attributes from an input instance
        """
        self.num_nodes = 0
        self.num_vehicles = 0
        self.num_calls = 0

        # information about each vehicle (index will start from 1!)
        self.vehicle_home_node = []
        self.vehicle_starting_time = []
        self.vehicle_capacity = []
        self.vehicle_compatible_calls = []   # some vehicles cannot transport some cargoes

        # information about each call (index will start from 1!)
        self.call_origin = []
        self.call_destination = []
        self.call_size = []
        self.call_cost_not_transporting = []
        self.call_pickup_lb = []
        self.call_pickup_ub = []
        self.call_delivery_lb = []
        self.call_delivery_ub = []

        # will hold a travel time/cost matrix FOR EACH VEHICLE (after parsing the input)
        self.travel_time_matrices = []
        self.travel_cost_matrices = []

        # time (in hours) and cost (in euro) matrices (index: vehicle x call)
        self.call_load_times_per_vehicle = []
        self.call_unload_times_per_vehicle = []
        self.call_load_costs_per_vehicle = []
        self.call_unload_costs_per_vehicle = []


    def read_instance(self, file_name):

        with open(file_name) as f:

            # 1. READ NUMBER OF NODES
            line = next(f)
            
            while line.startswith('%'):   # skip comment lines
                line = next(f)

            self.num_nodes = int(line)

            # 2. READ NUMBER OF VEHICLES
            line = next(f)

            while line.startswith('%'):
                line = next(f)

            self.num_vehicles = int(line)

            # 3. INITIALIZE OBJECT ATTRIBUTES WITH PROPER SIZE LISTS/MATRICES
            self.create_vehicle_structures()

            # 4. FOR EACH VEHICLE: SAVE HOME NODE, STARTING TIME, CAPACITY
            line = next(f)

            while line.startswith('%'):
                line = next(f)

            v = 1
            while v <= self.num_vehicles:

                line = line.strip()    #cuts any leading/trailing space
                line_info = line.split(',')   # list

                self.vehicle_home_node[v] = int(line_info[1])
                self.vehicle_starting_time[v] = int(line_info[2])
                self.vehicle_capacity[v] = int(line_info[3])

                # read next line
                line = next(f)
                v += 1

            # 5. READ NUMBER OF CALLS
            while line.startswith('%'):
                line = next(f)

            self.num_calls = int(line)

            # 6. INITIALIZE REMAINING OBJECT ATTRIBUTES WITH PROPER SIZE LISTS/MATRICES
            self.create_call_structures()

            # 7. READ A LIST OF CALLS THAT CAN BE TRANSPORTED USING EACH VEHICLE
            for v in range(1, self.num_vehicles+1):
                line = next(f)
                while line.startswith('%'):
                    line = next(f)
                line_info = line.split(',')

                # the first number is again the vehicle index, so we skip it
                for call in range(1,len(line_info)):
                    self.vehicle_compatible_calls[v].append(int(line_info[call]))

            # 8. READ INFORMATION ABOUT EACH CALL
            for c in range(1, self.num_calls+1):
                line = next(f)
                while line.startswith('%'):
                    line = next(f)
                line_info = line.split(',')

                self.call_origin[c] = int(line_info[1])
                self.call_destination[c] = int(line_info[2])
                self.call_size[c] = int(line_info[3])
                self.call_cost_not_transporting[c] = int(line_info[4])
                self.call_pickup_lb[c] = int(line_info[5])
                self.call_pickup_ub[c] = int(line_info[6])
                self.call_delivery_lb[c] = int(line_info[7])
                self.call_delivery_ub[c] = int(line_info[8])

            # 9. READ INFORMATION ABOUT TRAVEL TIME AND COSTS FOR EACH VEHICLE, AND EACH ORIGIN X DESTINATION PAIRS
            for i in range(1, self.num_nodes+1):
                for j in range(1, self.num_nodes+1):
                    for v in range(1, self.num_vehicles+1):
                        line = next(f)
                        while line.startswith('%'):
                            line = next(f)
                        line_info = line.split(',')

                        self.travel_time_matrices[v][i][j] = int(line_info[3])
                        self.travel_cost_matrices[v][i][j] = int(line_info[4])

            # 10. READ LOAD TIME AND COST, AS WELL AS UNLOAD TIME AND COSTS, FOR EACH VEHICLE X CALL PAIRS
            for v in range(1, self.num_vehicles+1):
                for c in range(1, self.num_calls+1):
                    line = next(f)
                    while line.startswith('%'):
                        line = next(f)
                    line_info = line.split(',')

                    self.call_load_times_per_vehicle[v][c] = int(line_info[2])
                    self.call_load_costs_per_vehicle[v][c] = int(line_info[3])

                    self.call_unload_times_per_vehicle[v][c] = int(line_info[4])
                    self.call_unload_costs_per_vehicle[v][c] = int(line_info[5])

        print("[IO] input instance file parsed successfully")


    def create_vehicle_structures(self):
        """
        Update first object attributes with lists of proper sizes
        NB! Padding all lists with a dummy "-1" to keep consistent indexing,
        e.g. vehicle_capacity[2] corresponds to vehicle #2,
        """
        self.vehicle_home_node = [-1] * (self.num_vehicles+1)
        self.vehicle_starting_time = [-1] * (self.num_vehicles+1)
        self.vehicle_capacity = [-1] * (self.num_vehicles+1)
        self.vehicle_compatible_calls = [-1] * (self.num_vehicles+1)

        self.vehicle_compatible_calls = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            self.vehicle_compatible_calls[i] = []


    def create_call_structures(self):
        """
        Update remaining object attributes with lists of proper sizes
        NB! Padding all lists with a dummy "-1" to keep consistent indexing,
        e.g. call_size[2] corresponds to call #2,
        """

        self.call_origin = [-1] * (self.num_calls+1)
        self.call_destination = [-1] * (self.num_calls+1)
        self.call_size = [-1] * (self.num_calls+1)
        self.call_cost_not_transporting =  [-1] * (self.num_calls+1)
        self.call_pickup_lb = [-1] * (self.num_calls+1)
        self.call_pickup_ub = [-1] * (self.num_calls+1)
        self.call_delivery_lb = [-1] * (self.num_calls+1)
        self.call_delivery_ub = [-1] * (self.num_calls+1)

        ########################################################################
        # one travel time matrix FOR EACH VEHICLE
        self.travel_time_matrices = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            # vehicle i gets a  num_nodes x num_nodes matrix
            self.travel_time_matrices[i] = [ [-1]*(self.num_nodes+1) for tmp in range(self.num_nodes+1) ]

        # one travel cost matrix FOR EACH VEHICLE
        self.travel_cost_matrices = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            # vehicle i gets a  num_nodes x num_nodes matrix
            self.travel_cost_matrices[i] = [ [-1]*(self.num_nodes+1) for tmp in range(self.num_nodes+1) ]

        ########################################################################
        # one list of call load times FOR EACH VEHICLE
        self.call_load_times_per_vehicle = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            # vehicle i gets a list of length num_calls+1
            self.call_load_times_per_vehicle[i] = [-1]*(self.num_calls+1) 

        # one list of call unload times FOR EACH VEHICLE
        self.call_unload_times_per_vehicle = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            # vehicle i gets a list of length num_calls+1
            self.call_unload_times_per_vehicle[i] = [-1]*(self.num_calls+1) 

        # one list of call load costs FOR EACH VEHICLE
        self.call_load_costs_per_vehicle = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            # vehicle i gets a list of length num_calls+1
            self.call_load_costs_per_vehicle[i] = [-1]*(self.num_calls+1) 

        # one list of call unload costs FOR EACH VEHICLE
        self.call_unload_costs_per_vehicle = [-1] * (self.num_vehicles+1)
        for i in range(1, self.num_vehicles+1):
            # vehicle i gets a list of length num_calls+1
            self.call_unload_costs_per_vehicle[i] = [-1]*(self.num_calls+1) 
