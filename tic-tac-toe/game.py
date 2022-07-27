class TicTacToe:
    def __init__(self):
        self.board = [' 'for _ in range(9)]#using a single list to represent a 3 x 3 board.
        self.current_winner = None #keep track of the winner
        
    def print_board(self):
        pass