class Game:
    def __init__(self, board_size, who_starts = 'x'):
        self.board_size = board_size
        self.board = self._create_board()
        self.whose_turn_is_it = who_starts
    
    def _create_board(self):
        row = []
        board = []
        for _ in range(self.board_size):
            row.append(None)

        for _ in range(self.board_size):
            board.append(row.copy())
        return board
    
    
    def _create_horizon_line(self):
        s = "  "
        for i in range(self.board_size):
            s += " ---"
        
        s += " "
    
        return s


    def _create_vertical_line(self, row_number):
        row = self.board[row_number]
        
        s = chr(65 + row_number) + " "

        for i in range(self.board_size):
            if row[i] == 1:
                s += "| x "
            elif row[i] == 0:
                s += "| o "
            elif row[i] == None:
                s += "|   "

        s += "|"

        return s
    
    def _create_header(self):
        s2 = "    "
        for i in range(self.board_size):
            s2 += str(i + 1) + "   "
        
        return s2
        
    def show_board(self):

        print(self._create_header())

        for i in range(self.board_size):
            print(self._create_horizon_line())
            print(self._create_vertical_line(i))

        print(self._create_horizon_line())