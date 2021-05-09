# Global variable that repesents game board.
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
move_list = [
    [0, 0], [0, 1], [0, 2]
    [1, 0], [1, 1], [1, 2]
    [2, 0], [2, 1], [2, 2]
]
player_turn = 0
game_over = false

# Main Function. 
def main():
    print()
    print_board()


def print_board():
    print("\t+" + "-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "+")
    for i in range(3):
        print("\t| ", end = "")
        for j in range(3):
            print(board[i][j] + " | ", end = "")
        print("\n\t+---+---+---+\n", end = "")
    print()


def clear_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'


def initialize_board():
    init = 1 
    for i in range(3):
        for j in range(3):
            board[i][j] = init
            init += 1


def check_win():
    # Check vertical and horizontal rows. 
    for i in range(3):
        if (board[i][0] == 'x' and board[i][1] == 'x' and board[i][2] == 'x'):
            return 1
        elif (board[0][i] == 'x' and board[1][i] == 'x' and board[2][i] == 'x'):
            return 1
        elif (board[i][0] == 'o' and board[i][1] == 'o' and board[i][2] == 'o'):
            return 2
        elif (board[0][i] == 'o' and board[1][i] == 'o' and board[2][i] == 'o'):
            return 2
    
    # Check diagonals.
    if (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x'):
        return 1
    elif (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x'):
        return 1
    elif (board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o'):
        return 2
    elif (board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o'):
        return 2
    
    return 0


def get_move(move):
    return move_list[move - 1]
    
    
def player_move():
    while True:
        print_board()
        print("\n\tPlayer " + player_turn + ", enter your move (1-9): ")
        move = input("")
        
        # Check if move is valid. 
        if len(move) > 1 or not move.isnumeric(): 
            print("Invalid move. Please enter a number bet. 1-9")
            continue
        elif move == "0":
            print("Invalid move. Please enter a number bet. 1-9")
            continue
        elif not is_free(move):
            print("Invalid move. That square is not free. Try again.")
            continue
        
        # Simulate move. 
        move_set = get_move(int(move))
        if player_turn == 1:
            board[move_set[0]][move_set[1]] = 'x'
            player_turn = 2
        else:
            board[move_set[0]][move_set[1]] = 'o'
            player_turn = 1


# Run main function. 
if __name__ == "__main__":
    main()