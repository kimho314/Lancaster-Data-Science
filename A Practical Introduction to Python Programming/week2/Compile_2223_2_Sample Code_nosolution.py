# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Date: 19/10/2021 #
# Edited By: Hanna Schmueck #
#Edit Date: 18/10/2022 #


# Strings

# Print a string
print("Hello World")

# Strings and Integers are NOT the same datatype - 
# for a value to be identical it has to not only have the same value, it also has to be the same datatype.

print(1 == "1")     # False
print(1 == 1.0)     # True
print(1 == True)   # True
print("1" == True)  # False

# We can convert data types using the following functions
# WARNING: Never name a variable after a Python function like "print", this will break the function

# Common (Need to remember)
a = int(1)   # Integer (Whole number)
b = str(1)  # String (Series of characters)
c = float(1)    # Float (Decimal)

# Less Common (Nice to remember)
d = list((1, 2, 3))     # List (List of items)
e = bool(1)     # Boolean (True/False)

# Very Uncommon (Probably the result of Googling for a solution)
f = dict(number=1)   # Dictionary (Array in most languages)
g = tuple([1, 2, 3])      # Tuple

# Taking User Input

userInput = input("Type in a message\n")     # Takes user input given in the terminal - ALWAYS A STRING
print(userInput)

# 3 Minute Challenge, given all the things we've learned so far, write a script to take in 2 numbers and multiply them

num1 = input("Type in a number\n")     # Takes user input given in the terminal
num2 = input("Type in a number\n")     # Takes user input given in the terminal

print(int(num1)*int(num2))  # Remember to convert values to Int before multiplying

# Never trust user input, the following example is an example of what not to do

# userCode = input("Type in some python\n")
# exec(userCode)  # NEVER use this

# String Operations

originalValue = "Hello World"
helloLancaster = originalValue.replace("World", "Lancaster")    # Replace all values in a string
words = originalValue.split(" ")    # Split string by a delimiter into a list
formatString1 = f"My Example: {originalValue}"  # These examples are identical just stylistically different
formatString2 = "My Example: {}".format(originalValue)  # These examples are identical just stylistically different
name = "John"

# 3 Minute Challenge, print the statement "Hello John" just by modifying the variables above

originalValue = originalValue.replace(" World", "")
answer = f"{originalValue} {name}"
print(answer)

# More String Operations

exampleText = "hello world"
print(exampleText)
capitalised = exampleText.capitalize()  # Convert First Character to Caps
print(capitalised)
titled = exampleText.title()    # Convert First Character of each "words" to caps and remaining "words" to lowercase
print(titled)
upperCase = exampleText.upper()     # Convert full string to caps
print(upperCase)
lowerCase = exampleText.lower()     # Convert full string to lower case
print(lowerCase)
swappedCase = exampleText.swapcase()     # Flips case of every character
print(swappedCase)

# Boolean Functions

letter = "A"
letter.isupper()    # Return true if ALL characters are upper case
letter.islower()    # Return true if ALL characters are lower case
word = "Lancaster"
word.startswith('L') # Return true if string starts with given string
word.endswith('L') # Return true if string ends with given string
