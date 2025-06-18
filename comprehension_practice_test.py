# Create a list of squares of even numbers between 1 and 20
# Given fruits = ['apple', 'banana', 'mango', 'kiwi'], make a new list of fruits with more than 5 letters
# From nums = [5, -1, 7, -3, 0], create a list of only the positive numbers
# Squares of odd numbers
# Filter words starting with 's'
# Extract digits from a string
# Multiply all numbers by 10
# Remove vowels from a string
# List of (number, square) tuples
# Flatten a 2D list
# Reverse each word in a sentence
# Filter only strings from a mixed list
# Replace negatives with 0

# Create a list of squares of even numbers between 1 and 20
squares = [x**2 for x in range(1,20) if x % 2 == 0]
print(squares)

# Given fruits = ['apple', 'banana', 'mango', 'kiwi'], make a new list of fruits with more than 5 letters
fruits = ['apple', 'banana', 'mango', 'kiwi']
new_fruits = [x for x in fruits if len(x)>5]
print(new_fruits)

# From nums = [5, -1, 7, -3, 0], create a list of only the positive numbers
nums = [5, -1, 7, -3, 0]
new_nums = [x for x in nums if x >0]
print(new_nums)

# Squares of odd numbers
square_odd = [x**2 for x in nums if x % 2 != 0]
print(square_odd)


# Filter words starting with 's'
words = ["sun", "moon", "sky", "star", "stone", "cloud"]
words_s = [x for x in words if x.startswith("s")]
print(words_s)

# Extract digits from a string
text = "abc123def456"
digits = [ch for ch in text if ch.isdigit()]
print(digits)

# Multiply all numbers by 10
# Lets use the num list from above
mul_10 = [x*10 for x in nums]
print(mul_10)

# Remove vowels from a string
text = "Justasmalltowngirl"
vowels = "aeiouAEIOU"
no_vowels = [c for c in text if c not in vowels]
print(no_vowels)

# List of (number, square) tuples
# Lets take the nums list for this one
num_sq_tuple = [(x,x*x) for x in nums]
print(num_sq_tuple)

# Flatten a 2D list
# Using nested list comprehension(or loop within a loop type situation)
matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
print(flat)

# Reverse each word in a sentence
sentence = "This world is not my home"
reverse_sen = [word[::-1] for word in sentence.split()]
print(reverse_sen)
rev_sentence = ' '.join(word[::-1] for word in sentence.split())
print(rev_sentence)

# Filter only strings from a mixed list
mixed = ["apple", 42, "banana", True, "cherry"]
only_strings = [x for x in mixed if isinstance(x,str)]
print(only_strings)

# Replace negatives with 0
# lets consider nums again

replc_neg = [x if x>=0 else 0 for x in nums]
print(replc_neg)