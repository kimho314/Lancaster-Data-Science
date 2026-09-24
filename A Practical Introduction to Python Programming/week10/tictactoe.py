class TicTacToe:
    turn=0
    size=0
    game = []

    def __init__(self, size):
        self.size = size
        for i in range(size):
            nested = [0] * size
            self.game.append(nested)    

    def DrawBoard(self):
        m = self.size
        game = self.game
        if m <= 0: # raise an exception when zero or negative interger income
            raise Exception("m must be a positive integer")
        line1 = " ---" # keeps " ---" pattern 
        line2 = "|" # keeps "|   " pattern
        row = ""
        for i in range(m): # iterate m times
            for j in range(m): # print " ---" m times 
                row += line1
            row += " \n"
            for j in range(m): # print "|   " m times
                row += line2
                if game[i][j] == 1:
                    row += ' X '
                elif game[i][j] == 2:
                    row += ' O '
                else:
                    row += '   '
            row += "|\n"
        for i in range(m): # print " ---" m times on the bottome of the board
            row += line1
        print(row)

    def WhoWon(self):
        game = self.game
        size = self.size
        def checkVertical(game,y,x): # count player1's tokens and player2's tokens vertically
            count1=0
            count2=0
            if game[y][x] == 1:
                count1 += 1
            if game[y][x] == 2:
                count2 += 1

            for i in range(1,3): # move the position to the upper side
                newY = y+i
                newX = x
                if newY<0 or newX<0 or newY>=3 or newX>=3:# if the poisition is out of boudary skip it
                    continue
                if game[newY][newX]==game[y][x] and count1>0: # if the value is 1, increase count1 by 1
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0: # if the value is 2, increase count2 by 1
                    count2+=1
            for i in range(1,3): # move the position to the down side
                newY = y-i
                newX = x
                if newY<0 or newX<0 or newY>=3 or newX>=3: # if the position is out of boundary skip it
                    continue
                if game[newY][newX]==game[y][x] and count1>0: # if the value is 1, increase count1 by 1
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0: # if the value is 2, increase ocunt2 by 1
                    count2+=1
            return [count1,count2] # return count1 and count2
        
        def checkHorizontal(game,y,x): # count player1's tokens and player2's tokens horizontally
            count1=0
            count2=0
            if game[y][x] == 1:
                count1+=1
            if game[y][x] == 2:
                count2+=1

            for i in range(1,3): # move to right side
                newY = y
                newX = x+i
                if newY<0 or newX<0 or newY>=3 or newX>=3: # if position is out of boundary skip it
                    continue
                if game[newY][newX]==game[y][x] and count1>0: # if the value is 1, increase count1 by 1
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0: # if the value is 2, increase count2 by 1
                    count2+=1
            for i in range(1,3): # move to left side
                newY = y
                newX = x-i
                if newY<0 or newX<0 or newY>=3 or newX>=3: # if the position is out of boundary skip it
                    continue
                if game[newY][newX]==game[y][x] and count1>0: # if the value is 1, increase count1 by 1
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0: # if the value is 2, increase count2 by 1 
                    count2+=1
            return [count1,count2] # return count1 and count2
        
        def checkDiagonal(game,y,x): # count player1's tokens and player2's tokens
            count1=0
            count2=0
            if game[y][x] == 1:
                count1+=1
            if game[y][x] == 2:
                count2+=1

            for i in range(1,3): # move to right-down side
                newY = y+i
                newX = x+i
                if newY<0 or newX<0 or newY>=3 or newX>=3: # if the position is out of boundary skip it
                    continue
                if game[newY][newX]==game[y][x] and count1>0: # if the value is 1, increase count1 by 1
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0: # if the value is 2, increase count2 by 1
                    count2+=1
            for i in range(1,3): # move to left-upper side
                newY = y-i
                newX = x-i
                if newY<0 or newX<0 or newY>=3 or newX>=3:
                    continue
                if game[newY][newX]==game[y][x] and count1>0:
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0:
                    count2+=1
            if count1==3 or count2==3:
                return [count1,count2]
            
            count1=0
            count2=0
            if game[y][x] == 1:
                        count1+=1
            if game[y][x] == 2:
                        count2+=1
            for i in range(1,3): # move to right-upper side
                newY = y-i
                newX = x+i
                if newY<0 or newX<0 or newY>=3 or newX>=3:
                    continue
                if game[newY][newX]==game[y][x] and count1>0:
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0:
                    count2+=1
            for i in range(1,3): # move to left-down side
                newY = y+i
                newX = x-i
                if newY<0 or newX<0 or newY>=3 or newX>=3:
                    continue
                if game[newY][newX]==game[y][x] and count1>0:
                    count1+=1
                if game[newY][newX]==game[y][x] and count2>0:
                    count2+=1
            return [count1,count2]
        
        def winner(count1,count2): # check who is winnder between player1 and player2
            if count1 == 3:
                return 1
            elif count2 == 3:
                return 2
            else:
                return 3
                
        for i in range(size):
            for j in range(size):
                count1, count2 = checkVertical(game,i,j) # count players' tokens vertically
                res = winner(count1,count2) # check who is winner
                
                if res==1 or res==2: # if result is either 1 or 2, then return the result
                    return res
                count1, count2 = checkHorizontal(game,i,j) # count players' tokens horizontally
                res = winner(count1,count2) # check the winner
                
                if res==1 or res==2: # if result is either 1 or 2, then return the result
                    return res
                count1, count2 = checkDiagonal(game,i,j) # count players' tokens diagonally
                res = winner(count1,count2) # check the winner
                
                if res==1 or res==2: # if result is either 1 or 2, then return the result
                    return res
        count0=0
        for i in range(3):
            for j in range(3):
                if game[i][j]==0:
                    count0+=1
        if count0 == 0:
            return 3
        else:
            return 0

    def play(self):
        game = self.game
        turn = self.turn
        self.DrawBoard()

        while True:
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
            else:
                continue

            self.DrawBoard() # print the game board

            winner = self.WhoWon()
            if winner == 1 or winner == 2 or winner == 3:
                if winner == 1:
                    print("Player 1 wins!")
                elif winner == 2:
                    print("Player 2 wins!")
                else:
                    print("Draw!")
                break
           
            turn += 1   # increase turn by 1


if __name__ == "__main__":
    game = TicTacToe(3)
    game.play()
