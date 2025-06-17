#Task 1: List of few songs
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
