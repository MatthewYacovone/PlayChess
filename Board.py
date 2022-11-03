# Chess Board
# Matthew Yacovone

class Board():
    """
    The configuration of the board.
    """
    def __init__(self):
        """
        Initializes the board per the standard chess rules.
        """
        
        self.board = []
    

        # Board Set-up
        for i in range(8):
            self.board.append([None] * 8)

        # White Pieces
        self.board[0][7] = "w#"
        self.board[0][6] = "w4"
        self.board[0][5] = "w?"
        self.board[0][4] = "wK"
        self.board[0][3] = "wQ"
        self.board[0][2] = "w?"
        self.board[0][1] = "w4"
        self.board[0][0] = "w#"
        
        for i in range (8):
            self.board[1][i] = "w^"
        
        # Black Pieces
        self.board[7][7] = "b#"
        self.board[7][6] = "b4"
        self.board[7][5] = "b?"
        self.board[7][4] = "bK"
        self.board[7][3] = "bQ"
        self.board[7][2] = "b?"
        self.board[7][1] = "b4"
        self.board[7][0] = "b#"
        
        for i in range (8):
            self.board[6][i] = "b^"
    
    def print_board(self):
        """
        Prints the current state of the board
        """
    
        buffer = ""
        for i in range(41):
            buffer += "*"
        print(buffer)

        for i in range(len(self.board)):
            divider = "|"
            for j in self.board[i]:
                if j.board == None:
                    divider += "    |"
                elif len(j.board) == 2:
                    divider += (" " + str(j.board) + " |")
            print(divider)
        print(buffer)








