# A module is just a Python file (.py) that contains definitions — functions, classes, or variables — that you can reuse in other files.
# You can use modules in other Python file by importing it.
# Basic syntax for importing modules and using functions inside the modules
# import file_name(without the .py) # Importing the whole file
# from file_name import function_name/class_name importing specific function/classes
# import file_name as alias_name #importing with an alias 
# file_name.function_name(parameters) #calling function of that file

## using dir/help
# dir: Lists all funcitons and variables in the module
# help: Gives Documentation

# example:
# import math
# print(dir(math))  # Lists all functions and variables in the module
# print(help(math)) # Gives the documentation

# We have created a file "greetings.py"
# Let us import and use functions from the file

from greetings import welcome,goodbye
print(welcome("Lam"))
print(goodbye("Lam"))
