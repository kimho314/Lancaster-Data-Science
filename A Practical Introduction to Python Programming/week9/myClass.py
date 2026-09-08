# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Date: 07/12/2021 #

class personalDetails:
    def __init__(self, name, birthday): # Init method, function that runs on class initialisation
        self.name = name # Store name parameter as as a class-wide variable
        self.birthday = birthday # Store birthday parameter as as a class-wide variable

class vehicle:
    def __init__(self, colour, type, location=[0, 0]):
        self.colour = colour
        self.type = type
        self.location = location

    def move(self, forward=0, backwards=0, left=0, right=0):
        # Additional Work
        xDirection = left + right # Calculate xDirection movement
        yDirection = forward + backwards # Calculate yDirection movement

        self.location[0] += xDirection # Add xDirection movement to the X coordinate stored inside of self.location
        self.location[1] += yDirection # Add yDirection movement to the X coordinate stored inside of self.location

class IceCreamTruck(vehicle): # Inherit vehicle class within IceCreamTruck
    pass # Dummy value following a colon to respect Python syntax

import numpy as np # Import numpy with the alias np
from random import randint # Import the randint function from the random library

class battleShips: # Create battleships class

    winState = False # Create variable to determine if an individual has won

    def __init__(self, username, height, length):
        self.username = username
        self.height = height
        self.length = length
        self.board = np.zeros((height, length)) # Generate 2D matrix of zeroes as our plain

    def generateShips(self, numberOfShips):
        self.numberOfShips = numberOfShips # Get the number of ships wanted on the board as an argument

        shipsPlaced = 0

        while shipsPlaced != self.numberOfShips: # Generate ships by checking for placements which already exist
            randomX, randomY = randint(0, self.height-1), randint(0, self.length-1)
            location = self.board[randomX][randomY] # Get random coordinates
            if location == 0:
                self.board[randomX][randomY] = 1 # Change coordinate value to a 1
                shipsPlaced += 1

    def checkHit(self, Axes):
        if self.board[Axes[0]][Axes[1]] == 1: # Check if the guessed location is a ship location
            self.numberOfShips -= 1 # Minus 1 from the number of ships
            self.board[Axes[0]][Axes[1]] = 2 # Set state of a destroyed ship to 2
            print(f"Boom, you got a hit! {self.numberOfShips} Remaining")
            if self.numberOfShips == 0:
                self.winState = True # If there are no ships left set the win state to True
        else:
            print("You did nothing but make a big splash!")







