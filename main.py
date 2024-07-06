import time


# prints the board in formatted way
def print_board(current_board):
    print("Current Board")
    for row in current_board:
        print("-------------------")
        print(f"|  {row[0]}  |  {row[1]}  |  {row[2]}  |")
    print("-------------------")


# board: current board
# depth: current depth
# max_depth: maximum depth
# is_max: if player is '0' => maximizing if player is 'X' => minimizing
def minimax(board, depth, max_depth, is_max):
    # checking for winning condition
    # return's -1 if 'X' wins
    # return's 1 if '0' wins
    # if it's draw return's 0
    if check_winner(board, 1):
        return -1
    elif check_winner(board, 0):
        return 1
    elif check_draw(board) or depth == max_depth:
        return 0

    # for the maximizing player
    if is_max:
        # is set to negative infinite
        max_evl = -float('inf')
        # loops through whole board places '0' and checks all the different possibilities through recursion
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = '0'
                    # sets is_max to false, to switch to minimizing player
                    evl = minimax(board, depth + 1, max_depth, False)
                    # gets the max value
                    max_evl = max(max_evl, evl)
                    # undo the changes in board
                    board[i][j] = ' '

        return max_evl
    else:
        # is set to positive infinite
        min_evl = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    evl = minimax(board, depth + 1, max_depth, True)
                    # here we want minimum value
                    min_evl = min(min_evl, evl)
                    # undo the changes in board
                    board[i][j] = ' '

        return min_evl


# this function decides the best move for '0'
def ai_move(board, max_depth):
    # initialize max_evl to negative infinite and best_move to none
    max_evl = -float('inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = '0'
                evl = minimax(board, 0, max_depth, False)
                board[i][j] = ' '
                # gets the value from minimax function and compares it with max_evl
                if evl > max_evl:
                    # if true set stores the evl and best_move i.e. the current indexes
                    max_evl = evl
                    best_move = (i, j)

    return best_move


# this function takes the current_board and current_player as inputs
# if player is 'X' it will prompt for input
# and for '0' the algorithm will pick the best move
def play(current_board, current_player):
    if current_player == 1:
        user_input = input("Enter the row and column as 'row col': ")
        # doing error checking if user input is not correct
        try:
            # getting row and col form input
            row = int(user_input.split(" ")[0])
            col = int(user_input.split(" ")[1])
        except:
            print("Your input was incorrect. Try again..")
            play(current_board, current_player)
        else:
            if row > 2 or col > 2 or row < 0 or col < 0:
                print("Your input was incorrect. Try again..")
                play(current_board, current_player)
            else:
                # put 'X' only when there is empty spce
                if current_board[row][col] == ' ':
                    current_board[row][col] = "X"
                else:
                    print("Wrong input")
                    play(current_board, current_player)
    else:
        # if player is '0' the algorithm will give the best move
        move = ai_move(current_board, 8)
        row = move[0]
        col = move[1]
        current_board[row][col] = '0'
    # finally returns the changed board
    return current_board


# checking for draw condition
def check_draw(current_board):
    for i in range(3):
        for j in range(3):
            if current_board[i][j] == ' ':
                return False
    return True


# checking for winning condition
def check_winner(current_board, player):
    if player == 1:
        checker = 'X'
    else:
        checker = '0'
    if (current_board[0][0] == current_board[0][1] == current_board[0][2] == checker) \
            or (current_board[1][0] == current_board[1][1] == current_board[1][2] == checker) \
            or (current_board[2][0] == current_board[2][1] == current_board[2][2] == checker) \
            or (current_board[0][0] == current_board[1][0] == current_board[2][0] == checker) \
            or (current_board[0][1] == current_board[1][1] == current_board[2][1] == checker) \
            or (current_board[0][2] == current_board[1][2] == current_board[2][2] == checker) \
            or (current_board[0][0] == current_board[1][1] == current_board[2][2] == checker) \
            or (current_board[0][2] == current_board[1][1] == current_board[2][0] == checker):
        return True
    else:
        return False


# initializing board, player and game
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 0
game = True
# continue until the game is False
while game:
    # printing board
    print_board(board)
    # checking winner
    is_winner = check_winner(board, player)
    # if any player wins loop breaks and game is set to False
    if is_winner:
        game = False
        if is_winner:
            if player == 0:
                print("Player 'o' wins!")
            else:
                print("Player 'X' wins!")
        break
    # checking for draw condition
    if check_draw(board):
        game = False
        print("It's a draw!")
        break
    # changing player
    player = 1 - player

    if player == 0:
        print("Ai playing....")
        time.sleep(0.8)
    # updates the new board bby calling play() function
    board = play(board, player)
