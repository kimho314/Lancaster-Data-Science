# Note: For this week's code, you might have to comment some lines out when running the script.
# Also, please make sure you don't save the contents of the data.zip to your current directory until you are hinted to do so.

# Try and break this program
# Division calculator
print("Enter two numbers, and I'll give you the quotient.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# One of the ways to break the code could be trying to divide by 0
# print(5/0)

# To get around ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# Another way to break the code could be entering strings rather than intergers/floats.
print(int("abc")/int("efg"))

# To get around ValueError:
try:
    print(19/0)
except ZeroDivisionError:
    print("You can't turn a string into an interger!")


# Another example of code breaking is trying to open a file that doesn't exist

filename = 'jane_eyre.txt'
try:
    with open(filename) as book:
        contents = book.read()
except FileNotFoundError:
    msg = f"Sorry, the file you have tried to read {filename} does not exist."
    print(msg)

# You can also let this code fail silently 
filename = 'jane_eyre.txt'
try:
    with open(filename) as book:
        contents = book.read()
except FileNotFoundError:
    pass

# Might be helpful to keep a log of what the prblem is
filename = 'jane_eyre.txt'
try:
    with open(filename) as book:
        contents = book.read()
except Exception as x:
    print(x)


# To do the next part of the lecture, please download, extract and save the contents of data.zip to your current working directory.
# Analysing text - what if the file exists and you're want to do something with it, e.g. counting the number of words it contains?
filename = 'jane_eyre.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file you have tried to read {filename} does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# Challenge 1 - can you think of how we can embed this program in a function？

# Challenge 2  - can you think of how we can execute this program so it returns the word count of the other files in the data folder?




