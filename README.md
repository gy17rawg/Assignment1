# Assignment 1 - Agent Based Model

# BACKGROUND

This assignment is designed to intoduce the Python programming language by building a model through various weeks of development and increasing complexity. The idea is that there is a user interface created with TKinter, an imported environment (environment.csv) which is displayed using matplotlib and then animated showing the agents (a simple way to imagine them is sheep) moveing and eating/nibbling their way across the environment. The final environment after the number of chosen interations is then outputted to environment.csv.

The program is run through command prompt (PC) or terminal (Mac). It should be noted this program has been developed and tested on a Mac through terminal, hence instructions will primarily focus on Mac use but with additional details on Windows use, although there may be some unexpected differences.

# CONTENTS

Licence - This program is licenced with an MIT licence and can be accessed in the GitHub library
Practical.py - The main model file where the lists are set up, libraries imported, GUI created, files imported and exported and animation controlled/created
README.md
agentframework.py - This framework is where the agents are set up alongside functions for moving, eating and sharing resources (in reality, sharing the eaten environment)
environment.csv - The environment output after eating, values 0 to 255
in.csv - The environment input with values from 0 to 255

# RUNNING THE PROGRAM & EXPECTATIONS

1) Download all code from the Assignment 1 GitHub repository. Code > Download Zip > Extract All
2) Open terminal with the extracted folder as directory (Mac > 'New Terminal at Folder' ¦ Windows > Type cmd then enter into address bar while in the chosen folder)
3) Type 'python Practical.py' followed by: Number of iterations, number of agents, neighbourhood size (With a space at the beginning and in between each)
4) The variables will be displayed in the command line
5) The model window will open, select Model > Run Model
6) The model will run (it will say so in command prompt) and show the animation by iterating the chosen number of times (Starting at 0)
7) The iteration number will be printed in the command prompt
8) It will say when the model has finished

# ISSUES/FURTHER DEVELOPMENT

- The update function is called right at the beginning so prints with iteration 0 twice
- There is no use for the environment output - it could easily be used as an input in further models

# WEBSITE

See https://gy17rawg.github.io/
