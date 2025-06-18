## Task 1: Learn about List comprehensions
# Example
squares = []
for i in range(1,6):
    squares.append(i*i)
print(squares)

# The above code can also be written as:
squares1 = [i**2 for i in range(1,6)]
print(squares1)

# Getting even numbers from a list
nums = [1,74,8,5,6,8,9,77,12,32,33,65,66,]
evens = [x for x in nums if x % 2 == 0]
print("The whole list:", nums)
print("The even numbers:", evens)

# Convert all strings to uppercase
names = ["sol","john", "joe", "don"]
upper_case = [name.upper() for name in names]
print("The names in upper case:",upper_case)
