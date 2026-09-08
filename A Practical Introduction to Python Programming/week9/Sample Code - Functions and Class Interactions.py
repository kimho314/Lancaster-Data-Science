# COMPILE Learning Course Material #
# Course: A Practical Introduction to Python Programming #
# Institution: Lancaster University #
# Author: Samuel Hollands #
# Date: 07/12/2021 #

from myClass import personalDetails # Import Class stored in myClass.py

sam = personalDetails("Sam", "07/12/2021")
print(sam.name) # Print variable name stored in the personalDetails class stored in sam variable
print(sam.birthday) # Print variable birthday stored in the personalDetails class stored in sam variable

from myClass import * # Import all classes from file

car = vehicle("Blue", "Jeep")
print(car.type)

# Now I want to move the car to a different location

car.move(forward=5, right=3) # Run the move function inside of the vehicle class
print(car.location)

# Add in another vehicle

iceCream = IceCreamTruck("Poka Dots", "Ice Cream Truck")

print(isinstance(iceCream, vehicle)) # Is our class an instance of another class
print(iceCream.type)

# Battleships

from myClass import battleShips # Import the battleShips class

myGame = battleShips("Sam", 10, 10) # Create an instance of battleships
myGame.generateShips(10) # Generate the ships

print(myGame.board)

myGame.checkHit([3, 5]) # Try some hits
myGame.checkHit([5, 5]) # Try some hits
myGame.checkHit([7, 5]) # Try some hits
myGame.checkHit([9, 5]) # Try some hits
myGame.checkHit([1, 5]) # Try some hits

print(myGame.board) # Show the board

# Full 2 Player Game:

playerOne = battleShips("Sam", 10, 10) # Generate an instance of the game
playerTwo = battleShips("Meg", 10, 10) # Generate an instance of the game

playerOne.generateShips(1) # Generate the number of ships for each board
playerTwo.generateShips(1) # Generate the number of ships for each board

winStatus = False # Create winStatus variable

print("Player One", playerOne.board) # Cheating if you want to see where the ships are (for testing purposes of course!)
print("Player Two", playerTwo.board) # Cheating if you want to see where the ships are (for testing purposes of course!)

while winStatus == False: # While loop so long as no one has won
    for playerTurn in (playerOne, playerTwo):
        print(playerTurn.username, "Your Turn!")
        coordinates = input("Type in two numbers separated by a comma for the coordinates you want to hit!\n")
        coordinates = [int(x) for x in coordinates.split(",")] # Change inputted coordinates into a list of 2 integers
        playerTurn.checkHit(coordinates) # Make the hit on the players board
        if playerTurn.winState == True: # Check if the player has won
            winStatus = True # Change win status to true
            print(f"Congratulations {playerTurn.username} You Win!")
            break # Break out of loops as someone has won







