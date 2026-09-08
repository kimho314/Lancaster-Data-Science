# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Date: 02/11/2021 #
# Edited By: Hanna Schmueck #
#Edit Date: 31/10/2022 #


# List Recap

myShopping = ["Apples", 5, "Grapes", 10, "Lemons", 5]
fruits = myShopping[::2]
prices = myShopping[1::2]

print(fruits, prices)

# Create a set of unique values
# Sets, like lists, are used to store multiple items in one variable. Their key characterisitcs are:
# that it contains only unique items, it is unindexed, its items are unchangeable, and it is unordered.
# (You can add new items, but once added they cannot be changed.)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
myList = set(myList)  # Convert to set
print(myList)

myList = list(myList)  # Convert back to list
print(myList)

# Dictionaries
# Dictionaries are also used to store multiple items in one variable, but they have a special shape. Dictionaries
# contain unique keys which are assigned values (these don't have to be unique).  Their key characterisitcs are:
# that they contain only unique keys, are changeable, and are ordered (since Python 3.7).

myShopping = {"Apples": 5, "Grapes": 10, "Lemons": 5}
applePrice = myShopping["Apples"]
# Keys can be most data types

# Different data types are not equal

myDataTypes = {2: "Hello", "2": "Goodbye"}
print(myDataTypes[2], myDataTypes["2"])

# Get all keys from dictionary

keyNames = myShopping.keys()
print(keyNames)
keyNames = list(myShopping.keys())  # to make into a list
print(keyNames)

# Get all values from dictionary

dictValues = list(myShopping.values())
print(dictValues)

# Get all keys with values from dictionary (i.e. the complete dictionary).

dictTuples = list(myShopping.items())
print(dictTuples)

# Iterating dictionaries

# Create a tuple
# Tuples are unordered and unchangeable (you cannot add or remove items from them later)!
# Duplicate values are allowed and they are indexed.

myTuple = ("Apple", 5)

# To get tuples
for fruit in myShopping.items():
    print(fruit)

# To split tuples

for fruit, price in myShopping.items():
    print(fruit, price)

# Case Study - Indexing

sentence = "I went to the park to buy some milk and the milk was very cold"
words = sentence.split(" ")
print(words)
wordsIndexed = dict(enumerate(words))  # Convert a numbered list of items into a dictionary
print(wordsIndexed)
indexedWords = {}

for index, word in wordsIndexed.items():
    if word in indexedWords.keys():
        indexedWords[word] += [index]
    else:
        indexedWords[word] = [index]

print(indexedWords)

# Challenge 1 - spend 5 minutes writing a script that prints the words directly before and after the word Milk

for index in indexedWords["milk"]:
    print(words[index - 1:index + 2])

# Challenge 2 - Spend 3 minutes making this more robust, so if our word is the first or last work in our dictionary
# it doesn't break

for index in indexedWords["cold"]:
    lower = index - 1
    upper = index + 2
    if lower < 0:
        lower = 0
    if upper >= len(words):
        upper = len(words)
    print(words[lower:upper])

# Extra - List Comprehensions

# Standard For Loop
myList = []
for number in range(10):
    myList.append(number * 2)

# Identical List Comprehension
listComp = [number * 2 for number in range(10)]
print(listComp)

# Standard Fibonacci
fib = [0, 1]
for value in range(998):
    nextValue = fib[-1] + fib[-2]
    fib += [nextValue]

# List Comprehension Fibonacci

fib = [0, 1]
fibComp = [fib.append(fib[-1] + fib[-2]) for value in range(998)]

# Always consider readability, it's not "good code" if the code is made deliberately obtuse to look complex
