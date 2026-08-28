# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Edited By: Hanna Schmueck #
# Date: 12/10/2021 #
#Edit Date: 11/10/2022 #

# Testing a Print Function - Introduce Strings
print("Hello World")

# Writing a comment
print("Hello World")    # Prints "Hello World"

# Printing some Arithmetic
print("Addition", 2 + 2)
print("Subtraction", 2 - 1)
print("Division", 2 / 4)
print("Multiplication", 2 * 4)
print("Exponent (To the power of)", 2 ** 2)
print("Modulus (remainders)", 13 % 5)

# Float vs Int
print("Integer", 2*2)   # Whole number (without decimal places, even .0!)
print("Float", 2/4)     # Decimal (Even .0!)

# Storing my Data
my_number = 5
print("Variables", my_number)
print("Comparatives", 5 == 5)   # Remember 1x "=" is variable assignment, 2x "=" is comparative


# Applying some of these operations
# You're trying to summarise a chapter of a book, it's 57 pages, 4 of which are citations.
# It took you 10 minutes to read the first 6 pages and you're trying to figure out how long
# the rest of the chapter will probably take you.

# Define variables containing these values
pages = 57
citations = 4
pages_read = 6 # The variable name contains an underscore (otherwise python would interpret it as two entities)
time_spent = 10

# Define leftover pages
pages_to_read = pages-citations-pages_read
print("Pages to be read still", pages_to_read)

# Calculate reading speed in pages per minute
reading_speed = pages_read/time_spent
print("Reading speed per minute", reading_speed)

# Calculate and display remaining time in minutes.
time_left = pages_to_read / reading_speed

print("Minutes left in the chapter", time_left)


# Bonus: Pythagoras - a^2 + b^2 = c^2
# I have a right angled triangle where side a is 10cm and side b is 8cm, work out the length of the hypotenuse


# Define a and b
a = 10
b = 8

# Square a and b
a2 = a**2
b2 = b**2

# Sum the squares of a and b (a2 + b2)
c2 = a2 + b2

# Square root C2
c = c2 ** 0.5

# Print results
print("Hypotenuse", c)


# Conditionals
my_number = 10

if my_number == 10:
    print("Yes it does!")
else:
    print("No it does not!")

# Elif Conditionals
my_number = 5

if my_number == 10:
    print("Yes it does!")
elif my_number == 5:
    print("Nearly")
else:
    print("No it does not!")

# Bigger or Smaller?
my_number = 180

if my_number > 120:     # if my_number BIGGER_THAN 120 (smaller would be < symbol)
    print("That's big")
else:
    print("Mini")

# and Conditionals
sample = "test"

if sample == "test" and my_number == 180:
    print("That's a coincidence")

# or Conditionals
if sample == "test" or my_number == 5:
    print("At least one of these is True")

# not Conditionals
if not sample == "lemon":
    print("It's not a lemon")