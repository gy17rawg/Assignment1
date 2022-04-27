# Assignment 1 - Agent Based Model

# BACKGROUND

This assignment is designed to intoduce the Python programming language by building a model through various weeks of development and increasing complexity. The idea is that there is a user interface created with TKinter, an imported environment (environment.csv) which is displayed using matplotlib and then animated showing the agents (a simple way to imagine them is sheep) moving and eating/nibbling their way across the environment. Reproduction is possible by agents. The final environment after the number of chosen interations is then outputted to environment.csv and a pdf saved of the final plot.

The program is run through command prompt (PC) or terminal (Mac). It should be noted this program has been developed and tested on a Mac through terminal, hence instructions will primarily focus on Mac use but with additional details on Windows use, although there may be some unexpected differences.

# CONTENTS

Licence - This program is licenced with an MIT licence and can be accessed in the GitHub library
Practical.py - The main model file where the lists are set up, libraries imported, GUI created, files imported and exported and animation controlled/created
README.md
agentframework.py - This framework is where the agents are set up alongside functions for moving, eating and sharing resources (in reality, sharing the eaten environment)
environment.csv - The environment output after eating, values 0 to 255
in.csv - The environment input with values from 0 to 255

# RUNNING THE PROGRAM & EXPECTATIONS

1) Download all code from the Assignment 1 GitHub repository then extract. Code > Download Zip > Extract All
2) Open terminal with the extracted folder as directory (Mac > 'New Terminal at Folder' ¦ Windows > Type cmd then enter into address bar while in the chosen folder)
3) Type 'python Practical.py' followed by: Number of iterations, number of agents, neighbourhood size (the maximum distance for communication between agents to occur) (With a space at the beginning and in between each) e.g. python Practical.py 10 20 10 
4) The variables will be displayed in the command line
5) The model window will open, select Model > Run Model
6) The model will run (it will say so in command prompt) and show the animation by iterating the chosen number of times (Starting at 0)
7) The iteration number will be printed in the command prompt
8) If conditions are met for new agents, it will state when and where they are created and display as white dots
9) If stopping conditions are met, it will state this and the program will stop running
10) When the program has finished running, the final plot will be output as a PDF into the original folder where extraction occurred in step 1

# TESTING

Testing was conducted throughout using PyCharm CE's debugger, variable watcher and simple print statements. Some statements remain in the code commented out but others remain for user guidance such as the iteration step, variables inputted, when functions are called and the end of the program.

# KNOWN ISSUES/FURTHER DEVELOPMENT

- The model can only be run once before having to be closed and reopened due to the generator function being exhausted (Hence disabling of Run Model on menu)
- There is no use for the environment output - it could easily be used as an input in further models
- New agents can't currently move/eat/share with neighbours

# WEBSITE

See https://gy17rawg.github.io/
