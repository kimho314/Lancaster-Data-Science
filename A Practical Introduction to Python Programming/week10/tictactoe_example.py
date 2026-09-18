def WhoWon(game):
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
            
    for i in range(3):
        for j in range(3):
            print("=== " + str(i) + ", " + str(j) + "===")
            count1, count2 = checkVertical(game,i,j) # count players' tokens vertically
            res = winner(count1,count2) # check who is winner
            print("1 ->" + str(res) + " " + str(count1) + " " + str(count2))
            if res==1 or res==2: # if result is either 1 or 2, then return the result
                return res
            count1, count2 = checkHorizontal(game,i,j) # count players' tokens horizontally
            res = winner(count1,count2) # check the winner
            print("2 -> " + str(res) + " " + str(count1) + " " + str(count2))
            if res==1 or res==2: # if result is either 1 or 2, then return the result
                return res
            count1, count2 = checkDiagonal(game,i,j) # count players' tokens diagonally
            res = winner(count1,count2) # check the winner
            print("3 -> " + str(res) + " " + str(count1) + " " + str(count2))
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


# game = [[2, 2, 0],
# [2, 1, 0],
# [2, 1, 1]]

# print(WhoWon(game))
	
# game = [[1, 2, 0],
# [2, 1, 0],
# [2, 1, 1]]

# print(WhoWon(game))

# game = [[1, 2, 0],
# [2, 1, 0],
# [2, 1, 2]]

# print(WhoWon(game))

# game = [[1, 2, 2],
# [2, 1, 1],
# [2, 1, 2]]

# print(WhoWon(game))

# game = [[1, 2, 1],
#        [1, 2, 1],
#        [2, 1, 2]]

# print(WhoWon(game))