# Task 1: Learning about functions: 
# Defining and Calling functions

def greet(name):
    return f"Hello, {name}!"

print(greet("Lam"))

# Function without Parameters
def say_hello():
    print("Hello there!")

say_hello()  # Output: Hello there!

# *args is used for undefined number of arguments passed in a function

def add_nos(*args):
    return sum(args)

print(add_nos(1,5,6))
print(add_nos(2,3,5,6,4,3,8,5,12))

# **kwargs is used when you're not sure how many keyword arguments will be passed.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Lam", age = 20, city = "Bengaluru", gender = "male")

# Lambda functions: A lambda is a small, one-line function with no name.
# Basic syntax: lambda arguments: expression
# *lambda* is the keyword
# *argument* is like the parameter list(can be zero or more)
# *expression* is the single value it returns(## no return keyword is needed)

square = lambda a: a*a
print(square(4))

# 2
greet = lambda a: f"hello {a}!"
print(greet("Lam"))

# Lets practice more lambda functions:
# Length of a word
# Write a lambda function that takes a string and returns its length.
# ✅ Example: "hello" → 5

len_extrct = lambda a : len(a)
print(len_extrct("Words"))

# Check if a number is even
# Write a lambda that returns True if a number is even, otherwise False.
# ✅ Example: 4 → True, 5 → False

chk_even = lambda a : a % 2 == 0
print(chk_even(6))

# Get the last character of a string
# ✅ Example: "Lam" → "m"

lst_char = lambda a : a[-1] if a else "Empty"
print(lst_char("Lam"))

# Sort a list of names by length using lambda
# names = ["John", "Elizabeth", "Amy", "Max"]
# # Result → ['Amy', 'Max', 'John', 'Elizabeth']

nam = ["John", "Elizabeth", "Amy", "Max"]
sort_lst = sorted(nam, key = lambda name: len(name))

print(sort_lst)

# Use map with lambda to square a list of numbers
# lambda x: x ** 2 → This is the function to apply (squaring each number)
# numbers → This is the list to apply the function to
# map() returns a special map object, so we convert it to a list with list() to see the results.
numbers = [3,5,6,7,2,8]
squared = map(lambda a: a*a, numbers)
print(list(squared))