#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:45:03 2022

@author: rorygrindey
"""

import random

#Basic form of a class and constructor

class Agent():
    def __init__(self, environment,agents, y, x): #Creation of agents, bringing in environment list
        
        if (x==None):
                self.x = random.randint(0,99)
                print("Random Used x")
                
        else:
                
            self.x = x
        
        if (y==None):
                self.y = random.randint(0,99)
                print("Random Used y")
                
        else:
                
            self.y = y
            
        self.environment=environment #means when the environment changes, it changes for all agents as its a mutable list
        self.agents=agents
        self.store=0
        
        
    def move(self):
        
        if random.random() < 0.5:
            
            self.y = (self.y + 1) % 100 #remainder means they move over the plot like a donut
            
        else:
            
            self.y = (self.y - 1) % 100 #Change 100 based on axis size
            
            
        if random.random() < 0.5:
            
            self.x = (self.x + 1) % 100
            
        else:
            
            self.x = (self.x - 1) % 100
            
        
        #matplotlib.pyplot.scatter(self.x,self.y)
        #print(self.x,self.y)


    def eat(self): #eat what is left of the environment in each move step (sheep)
        
    #Eats what is left if less than 10
        if self.environment[self.y][self.x]<10:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x]-self.environment[self.y][self.x]
                    
        if self.environment[self.y][self.x]>10: #eats environment at its position if the value is greater than 10. Gets that location in the environment list
            self.environment[self.y][self.x]-=10
            self.store += 10
        
        if self.store >100:
            self.environment[self.y][self.x]+=self.store
            self.store=0
        
    def share_with_neighbours(self, neighbourhood): #Method/function to search for close neighbours and share resources with them. Should work out distance to other agents
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance<=neighbourhood: #Only communicate if the sheep is within the neighbourhood set
                sum = self.store+agent.store
                ave=sum/2
                self.store=ave
                agent.store=ave
                #print("Sharing | Distance: " + str(distance) + " Average: " + str(ave))
                
    def distance_between(self,agent): 
        return (((self.x-agent.x)**2)+((self.y-agent.y)**2))**0.5       
    