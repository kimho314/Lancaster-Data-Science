# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Date: 09/11/2021 #


# Reading and Writing to files

# Reading Files

# Using Open (Almost always avoid!)

myFile = open("data.txt", "r")
print(myFile.read())
myFile.close()

# Using With (Preferred Method); this ensures the file is automatically closed

with open("data.txt", "r") as myFile:
    print(myFile.read())

# Creating a file that doesn't exist

with open("My New File.txt", "w") as myNewFile:
    myNewFile.write("")

# Storing Dictionaries in Files

# Import JSON library (typically done at the top of a Python file!)
import json

#myDict = {"7": 1, 7: 2, 7.0: 3} # Handling Data types
myDict = {"Apple": 1.5, "Orange": 2.0, "Banana": 0.9}

with open("myDict.json", "w+") as jsonFile:
    json.dump(myDict, jsonFile)

with open("myDict.json", "r") as jsonFile:
    myDictLoaded = json.load(jsonFile)

print(myDict)
print(myDictLoaded)

# Storing other variables in Files

import pickle

myList= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open("myList.pkl", "wb") as pickleFile:
    pickle.dump(myList, pickleFile)

with open("myList.pkl", "rb") as pickleRead:
    myData = pickle.load(pickleRead)

print(myData) 

# Reading and Writing to Spreadsheets will be covered in our Term 2 course!

# Challenge 1 - Using our data file spend 5 minutes writing a script to create a dictionary of each word and the frequency

with open("data.txt", "r") as myFile:
    myData = myFile.read()

noLines = myData.replace("\n", " ").lower()
words = noLines.split(" ")
uniqueWords = set(words)
wordCounts = {}

for word in uniqueWords:
    wordCounts[word] = words.count(word)

print(wordCounts)

# Challenge 2 - Using our new dictionary spend 5 minutes storing it as a JSON file and then reload it into the script

with open("wordCounts.json", "w+") as jsonFile:
    json.dump(wordCounts, jsonFile)

with open("wordCounts.json", "r") as jsonFile:
    myDictLoaded = json.load(jsonFile)

print(myDictLoaded)

# Making a new folder

import os

if os.path.isdir("myFolder"):
    print("Folder Already Exists")
else:
    os.mkdir('myFolder')

# Get Script Directory

myRoot = os.path.abspath(os.path.dirname(__file__))
myPath = os.path.dirname(myRoot)

print(myRoot)
print(myPath)















