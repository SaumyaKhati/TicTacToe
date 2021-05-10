import sys, random, os

# Global variable that repesents game board.
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
move_list = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2]
]
player_turn = 0
game_over = False
winner = 0

# Main Function. 
def main():
    global player_turn, game_over, winner
    choice = start_menu()
    if choice == 2:
        print("\tThanks for playing Tic Tac Toe. Goodbye!")
        sys.exit()
    player_turn = random.randint(1,2)
    print("\n" * 2 + "\t" * 6 + "INSTRUCTIONS\n\n\t1) Decide who is player 1 and 2." + 
          "\n\t2) When it's your turn, simply enter the CORRESPONDING number for the squares shown below!\n\n")
    print_board()
    clear_board()
    while not game_over: 
        player_move()
        winner = check_win()
        if winner == 0 and not full_board():
            continue
        game_over = True
    print()
    print_board()
    if winner == 0:
        print("\n\tThis game was a tie! Better luck next time!\n")
    else:
        print("\n\tCongratulations, player " + str(winner) +"! You won!\n")


def start_menu():
    while True:
        print("\tWelcome to Tic Tac Toe. Please choose one of the following options:")
        print("\t1) Play the game. (Enter 1)")
        print("\t2) Quit. (Enter 2)")
        choice = input("").strip()
        if not choice == '1' and not choice == '2':
            print("\tInvalid move. Please enter 1 or 2.")
            continue
        else:
            break
    return int(choice)


def print_board():
    print("\t+" + "-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "+")
    for i in range(3):
        print("\t| ", end = "")
        for j in range(3):
            print(board[i][j] + " | ", end = "")
        print("\n\t+---+---+---+\n", end = "")
    print()


def clear_board():
    global board
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'


def initialize_board():
    init = 1 
    global board
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
    global player_turn # refer to global var. inside function. 
    while True:
        print("\n\tPlayer " + str(player_turn) + ", enter your move (1-9): ")
        print_board()
        move = input("\tMove: ")
        
        # Check if move is valid. 
        if len(move) > 1 or not move.isnumeric() or move == "0": 
            clear_screen()
            print("\n\tInvalid move. Please enter a number bet. 1-9")
            continue
        elif not is_free(get_move(int(move))):
            clear_screen()
            print("\n\tInvalid move. That square is not free. Try again.")
            continue
        
        # Simulate move. 
        move_set = get_move(int(move))
        if player_turn == 1:
            board[move_set[0]][move_set[1]] = 'x'
            player_turn = 2
        else:
            board[move_set[0]][move_set[1]] = 'o'
            player_turn = 1
        clear_screen()
        break


def is_free(move):
    return board[move[0]][move[1]] == '-'


def full_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')


# Run main function. 
if __name__ == "__main__":
    main()