from board import Board
b = Board(5)
print(b)
print(b.is_full())
b.set_value(1,2,-1)
print(b.is_full())
