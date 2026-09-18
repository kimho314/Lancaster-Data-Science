def DrawBoard(m):
    if m <= 0: # raise an exception when zero or negative interger income
        raise Exception("m must be a positive integer")
    line1 = " ---" # keeps " ---" pattern 
    line2 = "|   " # keeps "|   " pattern
    row = ""
    for i in range(m): # iterate m times
        for j in range(m): # print " ---" m times 
            row += line1
        row += " \n"
        for j in range(m): # print "|   " m times 
            row += line2
        row += "|\n"
    for i in range(m): # print " ---" m times on the bottome of the board
        row += line1
    print(row)

DrawBoard(3)