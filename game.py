def createBoard(board):
    for i in board:
        print(" | ".join(i))
        print("-" * 10)
def ticTacToe():
    player1 = input("Player 1 enter your name: ")
    player2 = input("Player 2 enter your name: ")

    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(' ')
        board.append(row)
    players = [player1, player2]
    curr_player = players[0]

    print(f"Hey {player1} and {player2}, Welcome to Tic Tac Toe!")
    print("Rules are simple, you just have to enter correct row and column i.e. 0,1, or 2")

    while True:
        createBoard(board)
        row = int(input(f"{curr_player}, enter row (0, 1, or 2): "))
        col = int(input(f"{curr_player}, enter column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = 'X' if curr_player == player1 else 'O'

            winner = winnerChecker(board)
            if winner:
                createBoard(board)
                print(f"{curr_player} wins!")
                break

            if fullBoardChecker(board):
                createBoard(board)
                print("It's a tie!")
                break

            curr_player = player2 if curr_player == player1 else player1
        else:
            print("Invalid move. Try again.")


def winnerChecker(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] != ' ':
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] != ' ':
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] != ' ':
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] != ' ':
        return board[0][2]
    return None


def fullBoardChecker(board):
    for i in board:
        if ' ' in i:
            return False
    return True
ticTacToe()
