# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Date: 26/10/2021 #
# Edited By: Hanna Schmueck #
#Edit Date: 21/10/2022 #

# Lists

five = 5
myList = [0, 1, 2, 3, 4, 5] # Lists can be used to store multiple values
myList = [False, 1, "2", 3.0, "four", five] # Every data type can be stored inside of a list, including variables
myList = [[1, 2, 3], [4, 5, 6]] # Lists can also be 'nested'; basically lists inside of other lists

# List Indexing

myList = ["Apple", "Pear", "Lime", "Banana"]

myPear = myList[1] # How to get an item by index value, remember Python (like most programming languages) starts counting from 0 not 1!

mySelection = myList[1:3] # Selecting a range of objects from a Python list

myLast = myList[-1] # Get the last item in a list regardless of list size

myLength = len(myList) # Gets the length of myList as an integer

myRange = range(myLength) # Creates an iterable object that contains every countable whole number between 0 and myLength excluding the last value; range(3) == 0, 1, 2

addValue = myList.append("Grapes") # Identical functions written differently
# OR
addValue = myList += ["Grapes"]	# Identical functions written differently

del myList[1] # Removes item at index
myList.pop(1) # Removes item at a specific index and returns the remaining list
myList.remove("Apple") # Removes the first instance of a value from the list (Not index)

myList[::2] # return every other number
myList[::-1] # reverse list
myList[1::3] # Offset

enumerate(myList) # Append index values to each item
[1,2,3,4,5].sort(reverse=False)	# Sort, use reverse to invert

# Challenge - Split this list into two lists, one containing prices and the other containing each item

myList = ["Apple", 5, "Pear", 10, "Banana", 6, "Grapes", 8]

fruits = myList[::2]
prices = myList[1::2]

# While Loops

x = 5
while x != 0:
	x -= 1
	print(x)

# For Loops

for item in myList:
	print("Item:", item)

# Factorial

myNum = 5

factorial = myNum

for num in range(1, myNum):
	factorial *= num

# Challenge 2 - Make a loop to calculate triangular numbers, rather than 5! = 5*4*3*2*1, 5Tri = 5+4+3+2=1

myNum = 5

triangle = myNum

for num in range(myNum):
	triangle += num

# Nice to know: While loop instead of for loop; it's possible but generally unnecessary

myNum = 5
result = 0

while myNum != 0:
	result += myNum
	myNum -= 1