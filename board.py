# Define Board class that represents the n by n tic tac toe grid.
# A -1 represents a '-' (empty), 0 represents 'o' and 1 represents 'x'.
class Board:
    VALUE_MAP = {-1:'-', 0:'o', 1:'x'}
    def __init__(self, size):
        self.board = [[-1] * size] * size
        print(self.board)
        self.size = size

    def __str__(self):
        N = self.size

        top_border = "\t+"
        for i in range(N):
            top_border += "-" * N + "+"
        print(top_border)

        for i in range(N):
            print("\t|", end="")
            for j in range(N):
                print(self.VALUE_MAP[self.board[i][j]] + " | ", end="")
            print("\n\t+---+---+---+")
