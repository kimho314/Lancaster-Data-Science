#!/usr/bin/env python
# coding: utf-8

# Imagine I have a lot of numbers I want Python to crunch.
# I could write each of these equations like below, but it's very time consuming!

# 278475842579 - 23473472834823 =
# 373257465325873- 83457848743 = 
# 35443245 - 238438734783 = 
# 375637 - 1058573 = 
# 26465573 -2637382 = 
# ...etc.

# Since I am repeating the same "actions", over and over again, this can be be generalised as a FUNCTION.


# Example 1 - Simple subtraction of two numbers, as seen previously.
# The arguments here are positional arguments, i.e., ordering matters!
def subtract_two_numbers(num1, num2):
    """Add up the two numbers passed in as arguments and return the sum"""
    difference = num1 - num2
    print(difference)


subtract_two_numbers(3, 5)


# To avoid this easy mistake, we can explicitly tell Python which parameter each argument should be.
# When Python reads the function call, it knows to store the argument '3' in the parameter num1 and the argument '5' in num2. 
subtract_two_numbers(num1=3, num2=5)



# Going back to the pizza example
def createPizza(topping1, topping2, size):
    '''Makes a pizza with the toppings specified as arguments.'''
    message = f"Making a pizza that is {size} inches with {topping1} and {topping2}!"
    print(message)
    
createPizza('extra cheese', 'ham', 12)
# msg = createPizza('extra cheese', 'ham', 12)
# print(msg)


# Now, what if we want to save these arguments? We want to interact with these arguments
# <br>For instance, we might want to save the information for records-keeping.</br> 

# In this example, I want to save the string that is produced by the function. 
def createPizza(topping1, topping2, size):
    '''Makes a pizza with the toppings specified as arguments.'''
    message = f"Making a pizza that is {size} inches with {topping1} and {topping2}!"
    return message

msg = createPizza('extra cheese', 'ham', 12)
print(msg)


# Note: executing the function does not mean printing it! 
# So it is normal that we don't see it in our terminal.
# Compare "return message" vs "print message"
# Illustrate by comparing saving the function as variable and printing that variable

# In this example, I want to save the toppings and size information as a list.
def createPizza(topping1, topping2, size):
    '''Makes a pizza with the toppings specified as arguments.'''
    return [topping1, topping2, size]

ls = createPizza('extra cheese', 'ham', 12)
print(ls)


# Another example
def writeAddress(house_number, street_name, city):
    '''Return a formatted address.'''
    address = house_number + " " + street_name + ", " + city
    return address.title()

writeAddress("4", "privet drive", "surrey")



# Question - Do you have to return something? No
# Question - Can you have an empty function? Yes
# Say, you are working on something else and want to come back to complete the function.
# Use pass


def createPizza(topping1, topping2, size):
    pass
# Nothing happens but we've avoided getting an error when running empty code.
# Nothing is returned here either and that's okay!


# ## Passing arbitrary number of arguments - *args ##

# Sometimes, it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to.

## Take the pizza example again ##
# This time the size is given to be 12inches, so we set the argument to be 12 in our function declaration.
# As with anything in Python... we can be imaginative and use positional arguments with arbitrary arguments!

def createPizza(*toppings, size=12):
    '''Print out the topping(s) that customers requested.'''
    print(toppings)

createPizza('Ham and Pineapple', 'margherita', 'pepperoni')
createPizza('margherita')


def describe_pizza(*toppings):
    """Describes the pizza we are about to make."""
    print("\nMaking a pizza with the following topping(s):")
    for topping in toppings:
        print("- " + topping)

describe_pizza('Ham and Pineapple', 'margherita', 'pepperoni')
describe_pizza('margherita')



# ## Passing arbitrary number of arguments - **kwargs ##


# **kwargs works just like *args, only that it accepts named arguments (or key-value pairs.)

# Example of users providing information

def user(firstname, lastname, **kwargs):
    userProfile = {}
    userProfile['Forename'] = firstname
    userProfile['Surname'] = lastname

    ## we also know the user will be providing other information as key-value pairs...
    ## ...but we don't know what kind of information they will put in.

    for key, value in kwargs.items():
        userProfile[key] = value

    return userProfile

person = user('Maggie', 'Mi', allergies='eggs', dietary_requirements='None', frequentCustomer='No', loyalty_scheme='No')
print(person)


## A note on recusion

# Recursion means iteration. 
# A function is recursive, if the body of function calls the function itself...until the condition for recursion is true. 
# AKA a termination condition. 

def fact(n):
  """ Function to find factorial of a number, n"""
  if n == 1:
    return 1
  else:
    return (n * fact(n-1))

print ("3! = ",fact(3))