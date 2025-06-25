## TASK 1:
# Create a list of numbers: [5, 2, 9, 1, 7] or a random list :)
# Append a number
# Sort the list
# Pop the last item
# Reverse the list
# Print all intermediate steps

import random
# initialize with a list
numbers = []
i = 0
while i<5:
    num = random.randint(1,99)
    numbers.append(num)
    i+=1
print("The list of numbers:", numbers)
# Append with a number, lets say 5
numbers.append(5)
print("The new list after the number 5 has been added to the list", numbers)

# Sorting the list
numbers.sort()
print("The sorted list:", numbers)

#poping the last item
popped = numbers.pop()
print("The last item", popped)
print("The list after the last item was removed", numbers)

# Reverse the list
numbers.reverse()
print(" The list in reverse: ", numbers)

## TASK 2:
# Create a list of your 4 favorite movies
# Add one at the beginning
# Remove one from the end
# Use insert() to add one at index 2
# Print the final list

# Creating a list of my 4 Fav list
movies = ["Shawshank Redemption", "The Magnificent 7", "Its a Wonderful Life", "Avengers: Infinity War"]
print("My 4 Favourite movies:", movies)

# Add one at the beginning
movies.insert(0, "Batman Begins")
print("The new list after 1 movie has been added:", movies)

# Remove one from the end
movies.pop()
print("The new list after the last one has been removed",movies)

# Use insert() to add one at index 2 and printing the final list
movies.insert(2, "The Dark Knight")
print("The new list with The movie inserted at index 2", movies)