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

#Board Set-up
for i in range(8):
            #self.board.append(["x"] * 8)
    board.append([None] * 8)

# White Pieces
board[7][0] = "w#"
board[6][0] = "w4"
board[5][0] = "w?"
board[4][0] = "wK"
board[3][0] = "wQ"
board[2][0] = "w?"
board[1][0] = "w4"
board[0][0] = "w#"

for i in range (8):
    board[i][1] = "w^"
        
# Black Pieces
board[7][7] = "b#"
board[6][7] = "b4"
board[5][7] = "b?"
board[4][7] = "bK"
board[3][7] = "bQ"
board[2][7] = "b?"
board[1][7] = "b4"
board[0][7] = "b#"

for i in range (8):
    board[i][6] = "b^"
print(board)                            
