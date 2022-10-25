# Chess Board
# Matthew Yacovone

#class Board():
    #"""
    #The configuration of the board.
    #"""
    #def __init__(self):
        #"""
        #Initializes the board per the standard chess rules.
        #"""
        
        #self.board = []
board = []

# Board Set-up
for i in range(8):
            #self.board.append(["x"] * 8)
    board.append([None] * 8)

# White Pieces
board[0][7] = "w#"
board[0][6] = "w4"
board[0][5] = "w?"
board[0][4] = "wK"
board[0][3] = "wQ"
board[0][2] = "w?"
board[0][1] = "w4"
board[0][0] = "w#"

for i in range (8):
    board[1][i] = "w^"
        
# Black Pieces
board[7][7] = "b#"
board[7][6] = "b4"
board[7][5] = "b?"
board[7][4] = "bK"
board[7][3] = "bQ"
board[7][2] = "b?"
board[7][1] = "b4"
board[7][0] = "b#"

for i in range (8):
    board[6][i] = "b^"

# Print Board
buffer = ""
for i in range(41):
    buffer += "*"
print(buffer)

for i in range(len(board)):
    divider = "|"
    for j in board[i]:
        if j == None:
            divider += "    |"
        elif len(j) == 2:
            divider += (" " + str(j) + " |")
    print(divider)
print(buffer)








