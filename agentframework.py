#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:45:03 2022

'''This framework enables the creation of agents and stores their attributes. It also contains the functions
for eating the environment, moving and interacting. Version 1.0. MIT Licenced'''

@author: rorygrindey
"""

import random

# Basic form of a class and constructor


class Agent():
    def __init__(self, environment, agents, y, x):  # Creation of agents, bringing in environment and agent list and x y coordinates

        if x is None:  # Only assigns a random x if the agent hasn't been assigned one from the online list (if there are more agents than values)
            self.x = random.randint(0, 299)  # Assigns a random x between 0 and 299 (This uses the entire environment)
            print("Random Used x")

        else:

            self.x = x

        if y is None:  # Only assigns a random y if the agent hasn't been assigned one from the online list
            self.y = random.randint(0, 299)  # Assigns a random y between 0 and 299 (This uses the entire environment)
            print("Random Used Y")

        else:

            self.y = y

        self.environment = environment  # means when the environment changes, it changes for all agents as its a mutable list
        self.agents = agents
        self.store = 0  # All start with a store of 0

    def move(self):

        # This function moves the agents/sheep by 1 in a direction dependent on a random number

        if random.random() < 0.5:

            self.y = (self.y + 1) % 300  # remainder means they move over the plot like a donut (300 as this is the size of the environment)

        else:

            self.y = (self.y - 1) % 300  # Changed from 100 based on axis size

        if random.random() < 0.5:

            self.x = (self.x + 1) % 300

        else:

            self.x = (self.x - 1) % 300

        # matplotlib.pyplot.scatter(self.x,self.y)
        # print(self.x,self.y)

    def eat(self):  # eat the environment in each move step (sheep)

        # Eats what is left of the environment if it is less than 10
        if self.environment[self.y][self.x] < 10:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

        # If environment value is greater than 10, agent only eats 10
        if self.environment[self.y][self.x] > 10:  # eats environment at its position
            self.environment[self.y][self.x] -= 10
            self.store += 10

        # If the store value is greater than 100, the agent/sheep throws it up back to add to the environment
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0

# Method/function to search for close neighbours and share resources with them. Also calls function to work out distance to other agents

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:  # Compares itself to every other agent. Each iteration this is called is a new agent
            distance = self.distance_between(agent)
            # print(distance)
            if distance <= neighbourhood:  # Only communicate if the sheep is within the neighbourhood set
                sum = self.store + agent.store  # Combine stores of self and 3rd party agent
                ave = sum / 2  # Get average of stores
                self.store = ave  # Commit the average of the store to each agent
                agent.store = ave
                # print("Sharing | Distance: " + str(distance) + " Average: " + str(ave))

                # EXTRA: Conditions for creating a new agent are a storage over 75 and a distance to the other agent below 10
                # Also resets store of each to 0

                # print(ave)

                if ave > 75 and distance < 10:
                    self.store = 0
                    agent.store = 0
                    return True

    def distance_between(self, agent):
        return (((self.x - agent.x) ** 2) + ((self.y - agent.y) ** 2)) ** 0.5  # Get euclidean distance between agents
