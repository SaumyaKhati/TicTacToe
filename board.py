# Class that represents an n by n tic tac toe grid.
# A -1 represents a '-' (empty), 0 represents 'o' and 1 represents 'x'.
class Board:
    VALUE_MAP = {-1:'-', 0:'o', 1:'x'}
    def __init__(self, size):
        self.board = [[1] * size] * size
        self.size = size

    def __str__(self):
        N = self.size

        Board.print_border(N)
        for i in range(N):
            print("\t|", end="")
            for j in range(N):
                row = " " * (N // 2) + Board.VALUE_MAP[self.board[i][j]] + " " * (N // 2) + "|" 
                print(row, end='')
            Board.print_border(N)
        return ""

    @staticmethod
    def print_border(N):
        # Allow 'x', 'o' to appear in the center of each box.
        multiplier = N if N % 2 == 1 else N + 1
        border = "\n\t+"
        for i in range(N):
            border += "-" * multiplier + "+" 
        print(border)

    def clear(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = -1

    def set_value(self, pos_x, pos_y, val):
        # Ensure coordinates are in range.
        assert pos_x >= 0 and pos_x <= self.size - 1
        assert pos_y >= 0 and pos_y <= self.size - 1

        self.board[pos_x][pos_y] = val

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -1:
                    return False
        return True
        
