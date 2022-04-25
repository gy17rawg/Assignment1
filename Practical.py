
#545 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:23:25 2022

@author: rorygrindey
"""
import matplotlib
matplotlib.use('TkAgg')
import random
import operator 
import matplotlib.pyplot
import agentframework
import csv
import sys
import matplotlib.animation
import tkinter
import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) #Gets list of y values
td_xs = soup.find_all(attrs={"class" : "x"}) #Gets list of x values
#print(td_ys)
#print(td_xs)

def Run():
    
    print("Run initiation")
    
    animation = matplotlib.animation.FuncAnimation(fig, Update, frames=num_of_iterations, repeat=False) #Run animation by calling update function with number of frames equal to the stopping condition staying true which it calls each time
    
    canvas.draw() #Instead of .show, we use canvas.draw with TkInter

    print("Draw canvas")



fig = matplotlib.pyplot.figure(figsize=(7,7))

ax = fig.add_axes([0,0,1,1])

#Builds main menu window

root = tkinter.Tk()

root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)

print("Building Menu")

root.config(menu=menu_bar)

model_menu = tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="Model", menu=model_menu)

model_menu.add_command(label="Run Model", command=Run)

#Import environment

environment=[] 

f=open("in.csv",newline='')
reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC) #Can use delimiter= if delimiter isnt a comma. Nonnumeric converts number to float
for row in reader: #a list of rows
    rowlist=[] #Blank list for the reading of each row (y direction)
    for value in row: #a list of values, x direction
        rowlist.append(value) #makes a list of the values
    environment.append(rowlist) #adds the rows/values to environment list
f.close #Close file

agents=[] #Setting up the agent list

#Used with command line:
    
#num_of_iterations=int(sys.argv[1]) #First number input it the iterations ([0] is the file name)
#num_agents=int(sys.argv[2]) #Second number is the number of agents
#neighbourhood=int(sys.argv[3]) #Third number is the neighbourhood size
#print("Variables: " + str(sys.argv))

num_of_iterations=30
num_agents=30
neighbourhood=20


#Set up agents (variable)

for i in range(num_agents): #Loop until reaches number of agents. Appends to list as a list as y then x
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents, y, x)) #Assigns random agents determined in the class to the agents list
    #^^ Also passes environment list into agent's constructor
    #^^ Now passes in the list of agents - to get their x you use agents[3].x (if you want the x of agent 3)
    
carry_on = True


def Update(frame_number):

    print("Update Function (Move, eat, share)")    

    fig.clear()
    global carry_on

    #Random walks

    #for iteration in range(num_of_iterations): #Does loop number of times (Random walks/eats/shares) until the object num_of_iterations
    for i in range(num_agents): #Loops until object number_agents to ensure each agent walks/eats/shares
        agents[i].move()
        agents[i].eat() #Sheep eat the environment
        agents[i].share_with_neighbours(neighbourhood)
    
    #if random.random() < 0.1:
            #carry_on = False
            #print("stopping condition")
    
    #Showing environment background first and creates animation plot
    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.imshow(environment)   
    
    #Put points on
    for i in range(num_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
        print(i)
    #random.shuffle(agents) #Random shuffle of agent list
    #print(agents)

#Then show the entire picture
#matplotlib.pyplot.show()

    
#for k in range(num_agents):
    #matplotlib.pyplot.scatter(agents[k].x,agents[k].y) #plot x (col 1) then y (col 2)
#matplotlib.pyplot.show() #shows the movement of sheep, number of moves depends on iterations and you can see the eating which occurred. The point is the final position of the sheep

def gen_function(b = [0]):
    
    print("Test gen_function")
    
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a += 1

output=open('environment.csv','w',newline='')
writer=csv.writer(output)
for row in environment:
    writer.writerow(row)
output.close


tkinter.mainloop()





