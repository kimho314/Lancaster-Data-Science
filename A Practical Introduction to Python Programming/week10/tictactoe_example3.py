turn=0 # indicates who is turn
game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]] # indicates game board

while True:
    print(game) # print the game board
    player = turn%2 + 1 # calculates what player's turn is
    command = input(f"Player {player} move: ") # input commands which indicates y,x
    
    if command == 'q': # if a user types 'q' then exit the game
        break
    y,x = command.strip().split(",") # split string command into y,x 
    y=int(y)
    x=int(x)
    y-=1
    x-=1
    if game[y][x] == 0: # if value of position is 0, then mark player's token
        if player == 1:
            game[y][x]=1
        else:
            game[y][x]=2
    turn += 1   # increase turn by 1