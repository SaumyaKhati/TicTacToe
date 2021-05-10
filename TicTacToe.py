import sys, random, os

# Global Variables.
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
move_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
player_turn = 0
game_over = False
winner = 0


def main():
    execute_game()


def execute_game():
    global player_turn, game_over, winner
    choice = start_menu()
    clear_screen()
    if choice == 3:
        print("\tThanks for playing Tic Tac Toe. Goodbye!\n")
        sys.exit()
    elif choice == 2:
        instructions()
    player_turn = random.randint(1,2)
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
    while True:
        print("\n\tWould you like to play again? (y/n)")
        move = input("\tAnswer: ").lower()
        clear_screen()
        if move == 'y' or move == 'yes':
            execute_game()
        elif move == 'n' or move == 'no':
            print("\n\tThanks for playing Tic Tac Toe. Goodbye!\n")
            sys.exit()
        else:
            print("\tInvalid choice. Please enter yes(y) or no (n).")



def start_menu():
    while True:
        print("\n\tWelcome to Tic Tac Toe. Please choose one of the following options:")
        print("\t1) Play the game.")
        print("\t2) Read the instructions.")
        print("\t3) Quit.")
        choice = input("").strip()
        if not choice in ['1', '2', '3']:
            print("\tInvalid move. Please enter 1, 2, or 3.")
            continue
        else:
            break
    return int(choice)


def instructions():
    print("\n" * 2 + "\t" * 6 + "INSTRUCTIONS\n\n\t1) Tic-Tac-Toe is a two player game." +  
          "\n\t2) The classic version is played on a 3x3 board." + 
          "\n\t3) One player places 'x' pieces, the other places 'o'." +
          "\n\t4) The objective is to place your pieces consecutively on a row or column, or either diagonal." +
          "\n\t5) To make your move, you simply enter a number corresponding to the board squares (as shown below)," +
          "\n\t   and the appropriate piece will be automatically placed for you!\n")
    print_board()
    while True:
        print("\n\tWould you like to play the game? (y/n)")
        move = input("\tAnswer: ").lower()
        if move == 'y' or move == 'yes':
            clear_screen()
            return 0
        elif move == 'n' or move == 'no':
            print("\n\tGoodbye!\n")
            sys.exit()
        else:
            clear_screen()
            print("\tInvalid choice. Please enter yes(y) or no (n).")


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

# Board setup for instructions only
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

# Get the array index pos. corresponding to move.
def get_move(move):
    return move_list[move - 1]
    
# Simulates a player move.  
def player_move():
    global player_turn 
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