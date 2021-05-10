import sys, random, os, math

# Global Variables.
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# Store array indices corresponding to each move on the board. Ex: 1 = (0, 0), 2 = (0, 1), etc. 
move_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
player_turn = 0
game_over = False
winner = 0


def main():
    execute_game()

# Simulates game.
def execute_game():
    choice = start_menu()

    if choice == 1:
        player_game()
    elif choice == 2:
        computer_game()
    elif choice == 3:
        instructions()
        clear_board()
    else:
        print("\tThanks for playing Tic Tac Toe. Goodbye!\n")
        sys.exit()


def player_game():
    global player_turn, game_over, winner
    # "Set" default game state.
    clear_screen()
    clear_board()
    game_over = False
    winner = 0
    player_turn = 0

    player_turn = random.randint(0, 1) + 1
    clear_screen()
    while not game_over: 
        player_move()
        winner = check_win(board)
        if winner == 0 and not full_board(board):
            continue
        game_over = True
    print()
    print_board()
    if winner == 0:
        print("\n\tThis game was a tie! Better luck next time!\n")
    else:
        print("\n\tCongratulations, player " + str(winner) +"! You won!\n")
    # Ensure valid input.
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


def computer_game():
    global player_turn, game_over, winner
    # "Set" default game state.
    clear_screen()
    clear_board()
    game_over = False
    winner = 0
    player_turn = 0
    computer = 0

    player_turn = random.randint(0, 1) + 1
    computer = random.randint(0, 1) + 1
    clear_screen()

    # Play game.
    while not game_over: 

        if not player_turn == computer:
            player_move()
        else:
            best = best_move(board, computer)
            if computer == 1:
                board[best[0]][best[1]] = 'x'
                player_turn = 2
            else:
                board[best[0]][best[1]] = 'o'
                player_turn = 1

        winner = check_win(board)
        if winner == 0 and not full_board(board):
            continue
        game_over = True
    
    print()
    print_board()
    if winner == 0:
        print("\n\tThis game was a tie! Better luck next time!\n")
    elif winner == computer:
        print("\n\tThe computer won! Better luck next time!\n")
    else:
        print("\n\tCongrats! You won the game.\n")

    # Ensure valid input.
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
        print("\t1) Play the game (2 player version).")
        print("\t2) Play the computer.")
        print("\t3) Read the instructions.")
        print("\t4) Quit.")
        choice = input("").strip()
        if not choice in ['1', '2', '3', '4']:
            print("\tInvalid move. Please enter a number within 1-4.")
            continue
        else:
            break
    return int(choice)


def instructions():
    print("\n" * 2 + "\t" * 6 + "INSTRUCTIONS\n\n\t1) Tic-Tac-Toe is a two player game." +  
          "\n\t2) The classic version is played on a 3x3 board." + 
          "\n\t3) One player places 'x' pieces, the other places 'o'." +
          "\n\t4) The objective is to place your pieces consecutively on a row or column, or either diagonal." +
          "\n\t5) To make your move, you enter a number matching the board squares (as shown below)," +
          "\n\t   and the appropriate piece will be automatically placed for you!\n")
    initialize_board()
    print_board()
    while True:
        print("\n\tWould you like to play now? (y/n)")
        move = input("\tAnswer: ").lower()
        clear_screen()
        if move == 'y' or move == 'yes':
            execute_game()
        elif move == 'n' or move == 'no':
            print("\n\tAww....Goodbye. Hope you try out the game next time!\n")
            sys.exit()
        else:
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
            board[i][j] = str(init)
            init += 1


def check_win(game_board):
    # Check vertical and horizontal rows. 
    for i in range(3):
        if (game_board[i][0] == 'x' and game_board[i][1] == 'x' and game_board[i][2] == 'x'):
            return 1
        elif (game_board[0][i] == 'x' and game_board[1][i] == 'x' and game_board[2][i] == 'x'):
            return 1
        elif (game_board[i][0] == 'o' and game_board[i][1] == 'o' and game_board[i][2] == 'o'):
            return 2
        elif (game_board[0][i] == 'o' and game_board[1][i] == 'o' and game_board[2][i] == 'o'):
            return 2
    
    # Check diagonals.
    if (game_board[0][0] == 'x' and game_board[1][1] == 'x' and game_board[2][2] == 'x'):
        return 1
    elif (game_board[0][2] == 'x' and game_board[1][1] == 'x' and game_board[2][0] == 'x'):
        return 1
    elif (game_board[0][0] == 'o' and game_board[1][1] == 'o' and game_board[2][2] == 'o'):
        return 2
    elif (game_board[0][2] == 'o' and game_board[1][1] == 'o' and game_board[2][0] == 'o'):
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


def full_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')


# Returns best move (as a list) for current player using minimax algorithm.
def best_move(board, current_player):
    
    if current_player == 1:
        max_score = -math.inf
        top_move = [-1, -1]
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'x'
                    score = minimax(board, 2)
                    board[i][j] = '-'
                    if score > max_score:
                        max_score = score
                        top_move = [i, j]
    else:
        min_score = math.inf
        top_move = [3, 3]
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'o'
                    score = minimax(board, 1)
                    board[i][j] = '-'
                    if score < min_score:
                        min_score = score
                        top_move = [i, j]
    return top_move


# Returns max score for current pos. 
def minimax(board, current_player):
    # Store evaluation of position. 
    state = is_game_over(board)
    # If game is over, return static evaluation of pos. 
    if state[0] == True:
        return state[1]
    
    # Check if currentPlayer is the "maximing" player
    if current_player == 1:
        maxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'x'
                    eval = minimax(board, 2)
                    board[i][j] = '-'
                    if eval > maxEval:
                        maxEval = eval
        return maxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'o'
                    eval = minimax(board, 1)
                    board[i][j] = '-'
                    if eval < minEval:
                        minEval = eval
        return minEval




 
    


# Evaluates current position of game. 
def is_game_over(board):
    res = eval_pos(board)
    if res == 2:
        return [False, 2]
    else:
        return [True, res]


def eval_pos(board):
    val = check_win(board)

    if val == 1:
        return val
    elif val == 2:
        return -1
    if full_board(board):
        return 0
    else: 
        return 2


# Run main function. 
if __name__ == "__main__":
    main()