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


""" Solution module for representing a candidate solution to the mPDPTW


__author__ = ["Flaviane Almeida"]
__organization__ = "Universitetet i Bergen"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "viane202@hotmail.com"
"""

from instance_reader import InstanceReader

class Solution:
    """
    Class for representing a mPDPTW solution
    """

    def __init__(self):
        """
        Default constructor method, represents a void object
        """
        # TO DO: think what to do here
        self.vehicles_num_calls_taken = []
        self.vehicles_call_sequence = []
        self.vehicles_node_routes = []


    def __init__(self,
                 input_instance: InstanceReader,
                 short_solution_form: str):
        """
        Constructor building an object from a string representing a solution.
        The string format is as follows:
        sequence of calls taken by vehicle 1
        '0'
        sequence of calls taken by vehicle 2
        '0'
        ...
        sequence of calls taken by vehicle v
        '0'
        sequence of calls taken by spot charters

        Example 1: In "0 2 2 0 1 5 5 3 1 3 0 7 4 6 7 4 6", vehicle 1 doesn't
        take any call, vehicle 3 takes calls 1,5 and 3, while 7,4,6 are taken by
        spot charters.

        Example 2: In "4 4 3 3 0 7 7 0 5 5 2 2 0 6 1 6 1", only calls 6 and 1 
        are taken by spot charters.
        """

        # saves the reference to the input instance object
        self.instance = input_instance

        self.vehicles_num_calls_taken = [-1] * (self.instance.num_vehicles+1)
        self.calls_not_taken = []

        # a list containing: a list of pickup and delivery calls for each vehicle
        self.vehicles_call_sequence = [-1] * (self.instance.num_vehicles+1)
        
        # a list containing: a list with the sequence of nodes visited for each vehicle
        self.vehicles_node_routes = [-1] * (self.instance.num_vehicles+1)

        ########################################################################
        # 1. BREAK THE GIVEN STRING BY VEHICLES
        short_solution_form.strip()

        # break string into lists of calls per vehicle
        broken = short_solution_form.split('0')
        print("reading solution from: ")
        print(broken)

        for v in range(self.instance.num_vehicles):
            tmp = broken[v].strip().split()

            # vehicles index starts from 1
            self.vehicles_call_sequence[v+1] = [int(x) for x in tmp]

        ########################################################################
        # 2. THE STRING ENDS (AFTER LAST ZERO) WITH THE SPOT CHARTED CALLS
        tmp = broken[self.instance.num_vehicles].strip().split()
        self.calls_not_taken = [int(x) for x in tmp]

        ########################################################################
        # 3. NUMBER OF CALLS TAKEN
        for v in range(1,self.instance.num_vehicles+1):
            l = self.vehicles_call_sequence[v]
            self.vehicles_num_calls_taken[v] = int(len(l)/2)

        ########################################################################
        # 4. FIND VISITED NODES BY THE SEQUENCE OF CALLS TAKEN BY EACH VEHICLE
        for v in range(1, self.instance.num_vehicles+1):

            # mask flagging nodes already visited in the route
            visited = [False] * (self.instance.num_nodes+1)

            # home node of vehicle (starting position)
            home = self.instance.vehicle_home_node[v]
            self.vehicles_node_routes[v] = [int(home)]

            # iterate over nodes corresponding to call pickup/delivery
            for c in self.vehicles_call_sequence[v]:
                if(visited[c] == False):
                    visited[c] = True
                    self.vehicles_node_routes[v].append(self.instance.call_origin[c])
                else:
                    self.vehicles_node_routes[v].append(self.instance.call_destination[c])


        print("routes of each vehicle:")
        print(self.vehicles_node_routes[1:])


    def fleet_cost(self, include_node_costs=True):
        """
        Evaluate the first sum in the objective function (own fleet)
        If the argument is False, we do not include the load/unload costs at
        each node.
        """
        fleet = 0.0

        # costs from the routes traveled by the fleet vehicles
        for v in range(1, self.instance.num_vehicles+1):

            route_size = len(self.vehicles_node_routes[v])

            # mask flagging calls already taken in the route (is it pickup or delivery)
            pickup = [True] * (self.instance.num_calls+1)

            # 1. TRAVELING COST
            # if route_size == 1, this vehicle stays at its home node
            # otherwise, we compute and add the travel costs of each leg in the route
            if (route_size > 1):
                for i in range(route_size-1):
                    source = self.vehicles_node_routes[v][i]
                    dest = self.vehicles_node_routes[v][i+1]

                    #print("cost from " + str(source) + " to " + str(dest) )
                    leg_cost = self.instance.travel_cost_matrices[v][source][dest]
                    fleet += leg_cost
                    #print("leg_cost = " + str(leg_cost))

                    # 2. PICKUP/DELIVERY COSTS (NOT INCLUDED IF THE ARGUMENT IS FALSE)
                    if include_node_costs:

                        # get which call we are handling
                        c = self.vehicles_call_sequence[v][i]

                        if pickup[c] == True:   # pickup
                            
                            #print("cost of pickup of call #" + str(c))
                            #print(self.instance.call_load_costs_per_vehicle[v][c])
                            fleet += self.instance.call_load_costs_per_vehicle[v][c]
                            pickup[c] = False

                        else:                    # delivery
                            #print("cost of delivery of call #" + str(c))
                            #print(self.instance.call_unload_costs_per_vehicle[v][c])
                            fleet += self.instance.call_unload_costs_per_vehicle[v][c]
        return(fleet)


    def spotcharter_cost(self):
        """
        Evaluate the second sum in the objective function (spot charter)
        """
        spotcharter = 0.0

        # costs from the calls not taken (hence, used spot charter)
        for c in self.calls_not_taken:
            spotcharter += self.instance.call_cost_not_transporting[c]

        # each call not taken appears twice in the input string
        spotcharter = spotcharter/2

        return(spotcharter)


    def total_cost(self, include_node_costs=True):
        """
        Evaluate objective function corresponding to this solution.
        If the argument is False, we do not include the load/unload costs at
        each node.
        """
        
        return(self.fleet_cost(include_node_costs) + self.spotcharter_cost())
