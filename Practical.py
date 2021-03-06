# 545 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:23:25 2022
'''This is the main python file to run the program. It pulls files from the source folder and online and writes to an
export file. It sets up agents, iterations and neighbourhoods based on the command line inputs and creates the GUI. It
calls the functions to eat, move and interact from the agentframework during each iteration and determines if new agents
are to be created. Version 1.0. MIT Licenced''
@author: rorygrindey
"""
import matplotlib
import random
import matplotlib.pyplot
import agentframework
import csv
import sys
import matplotlib.animation
import tkinter
import matplotlib.pyplot as plt
import requests
import bs4
matplotlib.use('TkAgg')

# This section imports x and y values for the agents from a website

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class": "y"})  # Gets list of y values
td_xs = soup.find_all(attrs={"class": "x"})  # Gets list of x values


# print(td_ys)
# print(td_xs)

# This section initates a run of the model by calling the update function for the number of iterations to form an animation

def Run():
    print("Run initiation")

    model_menu.entryconfig("Run Model", state="disabled")

    animation = matplotlib.animation.FuncAnimation(fig, Update, frames=gen_function(), repeat=False)
    # Run animation by calling update function with number of frames equal to the stopping condition staying true which it calls each time

    canvas.draw()  # Instead of .show, we use canvas.draw with TkInter

    # print("Draw canvas")


# This section is figure creation with a set size and axes chosen for the canvas/animation to be displayed in

fig = matplotlib.pyplot.figure(figsize=(7, 7))

ax = fig.add_axes([0, 0, 1, 1])

# Builds main menu window/GUI

root = tkinter.Tk()

root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)

# print("Building Menu")

root.config(menu=menu_bar)

model_menu = tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="Model", menu=model_menu)

model_menu.add_command(label="Run Model", command=Run)  # Calls run function (Defined above)

# This section import environment as a list

environment = []

f = open("in.csv", newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  # Can use delimiter= if delimiter isnt a comma. Nonnumeric converts
                                                      # number to float
for row in reader:  # a list of rows
    rowlist = []  # Blank list for the reading of each row (y direction)
    for value in row:  # a list of values, x direction
        rowlist.append(value)  # makes a list of the values
    environment.append(rowlist)  # adds the rows/values to environment list
f.close()  # Close file

# Allows for command line inputs:

num_of_iterations = int(sys.argv[1])  # First number input it the iterations ([0] is the file name)
num_agents = int(sys.argv[2])  # Second number is the number of agents
neighbourhood = int(sys.argv[3])  # Third number is the neighbourhood size
print("Variables: " + "Iterations: " + str(sys.argv[1]) + " Number of Agents (Sheep): " + str(sys.argv[2])
      + " Neighbourhood Size: " + str(sys.argv[3]))

# Below was used during testing to determine variable values
# num_of_iterations = 20
# num_agents = 10
# neighbourhood = 10

# Set up agents (variable)

agents = []  # Setting up the agent list
newagents = []  # A list for created agents

for i in range(num_agents):  # Loop until reaches number of agents. Appends to list as a list as y then x
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    # Assigns agents determined in the class to the agents list
    # ^^ Also passes environment list into agent's constructor
    # ^^ Now passes in the list of agents - to get their x you use agents[3].x (if you want the x of agent 3)

carry_on = True


def Update(frame_number):
    print("Update Function (Move, eat, share) " + str(frame_number))

    fig.clear()
    global carry_on

    # Ensures each agent/sheep moves, eats and shares each iteration. Does this loop number of times
    # (Random walks/eats/shares) for the number of iterations inputted (based on frame numbers)
    for i in range(num_agents):  # Loops until object number_agents to ensure each agent walks/eats/shares
        agents[i].move()
        agents[i].eat()  # Sheep eat the environment

        # Sharing function and this is the creation of new agents (Extra) but it does so anywhere in the environment
        # and draws them on (EXTRA):

        if agents[i].share_with_neighbours(neighbourhood) is True:
            x = random.randint(0, 299)
            y = random.randint(0, 299)
            newagents.append(agentframework.Agent(environment, agents, y, x))
            #  matplotlib.pyplot.scatter(agents[-1].x, agents[-1].y, color="White")  # Puts new agent on the plot
            print("New agent created at: " + str(x) + " " + str(y))

    if random.random() < 0.1:
        carry_on = False
        print("Stopping condition met")  # Stops program if a random number is less than 0.1

    # Showing environment background first and creates animation plot - ensures the environment isn't loaded for each
    # iteration hence faster
    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.imshow(environment)

    # Put points on to plot
    for i in range(num_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color="Red")

    for j in range(len(newagents)):
        matplotlib.pyplot.scatter(newagents[j].x, newagents[j].y, color="White")
        # print(i)

    # random.shuffle(agents) - Previous use of random shuffle of agent list
    # print(agents)


# matplotlib.pyplot.show() - No longer required as canvas is used

#  KNOWN ISSUE: Generator function can only be used once, hence disability of menu option. Provided code:
def gen_function(b=[0]):
    print("Open gen_function")

    a = 0
    global carry_on  # Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & carry_on:  # Program will keep running so long as there are iterations left and
                                                # carry_on hasn't been set to false
        yield a  # Returns control and waits next call.
        a = a + 1
    plt.savefig('Final_Plot.pdf')  # EXTRA: Saves final plot when program ends
    print("Program complete. Files Saved. PDF Output to source folder.")


# This section opens a csv to write the new environment to
output = open('environment.csv', 'w', newline='')
writer = csv.writer(output)
for row in environment:
    writer.writerow(row)
output.close()

tkinter.mainloop()
