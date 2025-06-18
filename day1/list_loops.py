#Task 1: Learning how to create list
# Creating the List of few songs and printing them

songs = ["Oceans", "Way Maker","Who you Say I am", "Reckless Love", "10000 Reasons"] 
for song in songs: 
	print(song) 

#Task 2: Print Even numbers from 1 to 10 
numbers = list(range(1,11)) 
i = 0 
while i < len(numbers):
	if numbers[i]%2==0:
		print(numbers[i])
	i+= 1

# Task 2: Indexing
#Basic List
colour = ["red", "blue", "green"]

#Mixed types
details = ["Lam",25,True]

print(colour[0]) # red
print(colour[1]) # blue

# Task 3: Slicing

numbers_1 = [10,20,30,40,50,60]
print(numbers_1)
print("For [1:4]:") 
print(numbers_1[1:4])
print("For [:3]:")
print(numbers_1[:3])
print("For [3:]:")
print(numbers_1[3:])
print("For [-3:]:")
print(numbers_1[-3:])
print("For steps of 2:")
print(numbers_1[::2])

# Some more slicing and printing using List of 5 football players:
football = ["Messi","C.Ronaldo","Casilas", "Iniesta", "Sol"]
print("Players inside the list:")
print(football)
print("The first player:")
print(football[0])
print("The last player:")
print(football[-1])
print("The middle 3 players using slicing:")
print(football[1:-1])

# Task 4: Learning list methods
# Lets take a list, fruits with apple and banana as the initiative list and use different methods on this

fruits= ["apple", "banana"]
print("This is the list of fruits before any method was mentioned:", fruits)

# 1. Append: Using append lets us app items to the list at the end.
fruits.append("mango")
print("This is the list after 'mango' was appended", fruits)

# 2. Insert: Insert add item at specific position
# syntax: insert(index, item)

# inserting orange at location 1 (location starts from 0,1,2...)
fruits.insert(1,"orange")
print("The output after inserting orange at location 1:", fruits)

# 3. pop: Removes and returns the last items
# The pop method removes the last item on the list and then returns it. 
# We can then print or store this in a variable
# syntax 1: list_name.pop()
# syntax 2: list_name.pop(index) --> This remove the item at specific position

last_item = fruits.pop()
print("The item that was popped: ", last_item)
print("The list after the method pop was called", fruits)
item_pos_2 = fruits.pop(1)
print("The item at 2nd position: ", item_pos_2)
print("The list after the item at 2nd position was removed:", fruits)

# 4. remove: We can remove item with specific values
# This method removes the item mentioned from the list.
# If there are multiple items with the same name. Only the first item with the name is removed.
# syntax: list_name.remove(item)

# Let us remove banana from the list
fruits.remove("banana")
print("The list after banana is removed:", fruits)

# 5. sort: We can sort a list of numbers using this method
# syntax: list_name.sort()
# Let us create a list, "numberss" that contains 5 random numbers

import random # for genrating random numbers
numberss = [] #declaring the list
i=0
while (i<5):
	num = random.randint(1,30)
	numberss.append(num)
	i+=1
print("Let us Generate a random numbers list: ", numberss)
numberss.sort()
print("The list after it has been sorted:", numberss)

# Reverse: We can also reverse the order
# syntax: list_names.reverse()
numberss.reverse()
print("The same list reversed", numberss)

# clear: We can empty the list with this method
# syntax: list_name.clear()

# For this method let us use the fruits list which contained only apple at this point.
fruits.clear()
print("The list, 'fruits' after it has been emptied", fruits)
