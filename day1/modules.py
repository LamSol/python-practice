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

# Lets built a small calculator module called calculato.py
# Let us import the module and use the functions

from calculator import add,sub,mul,div
a = float(input("Enter the first Number: "))
b = float(input("Enter the second number: "))

print("Sum:", add(a,b))
print("Difference:",sub(a,b))
print("Product", mul(a,b))
print("Division",div(a,b))

# There are also built in modules like random, datetime, os
# random random module is used to generate random items like numbers, item from list, etc
# datetime module is used to get the date and time
# os module is used for interacting with the operating System

# random:
import random
print(random.randint(1,10)) # Random integer between 1-10
print(random.random()) # Random float between 0.0 and 1.0
print(random.choice(['a','b','c','d'])) # Random item from list
print(random.sample(range(100),5)) # Random 5 unique values from 0-99

# Date Time:
from datetime import datetime, date, timedelta
now = datetime.now()
print("Current Date & Time: ", now)
print("Only Date: ", now.date())
print("Only time: ", now.time())

tomorrow = now + timedelta(days =1)
print("Tomorrow's date: ", tomorrow.date())

# Formatting:
print(now.strftime("%d-%m-%Y"))
