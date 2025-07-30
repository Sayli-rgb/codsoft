import random

# 🎯 Sayli's Tic-Tac-Toe Game (with computer moves)

def show_board(game):
    for r in game:
        print(" | ".join(r))
        print("-" * 9)

def check_winner(game, sign):
    for i in range(3):
        if all(cell == sign for cell in game[i]):  # Row
            return True
        if all(game[j][i] == sign for j in range(3)):  # Column
            return True
    if all(game[i][i] == sign for i in range(3)) or all(game[i][2 - i] == sign for i in range(3)):
        return True
    return False

def board_full(game):
    return all(cell != " " for row in game for cell in row)

def available_moves(game):
    return [(i, j) for i in range(3) for j in range(3) if game[i][j] == " "]

# 🎉 Game Start
game_board = [[" " for _ in range(3)] for _ in range(3)]

print("🧠 Welcome! This is Sayli’s Smart Tic-Tac-Toe 🎮")
print("You will play as ❌ (X). Computer will be ⭕ (O).\n")

while True:
    show_board(game_board)
    try:
        user_row = int(input("👉 Enter row (0-2): "))
        user_col = int(input("👉 Enter column (0-2): "))
    except ValueError:
        print("⚠️ Please enter numbers only (0 to 2).")
        continue

    if not (0 <= user_row <= 2 and 0 <= user_col <= 2):
        print("❌ Invalid position. Try between 0 to 2.")
        continue

    if game_board[user_row][user_col] != " ":
        print("🔁 That cell is taken. Try a different spot.")
        continue

    game_board[user_row][user_col] = "X"

    if check_winner(game_board, "X"):
        show_board(game_board)
        print("🎊 Yay! You won this round!")
        break

    if board_full(game_board):
        show_board(game_board)
        print("🤝 It's a draw!")
        break

    # 💻 Computer move
    move = random.choice(available_moves(game_board))
    game_board[move[0]][move[1]] = "O"

    if check_winner(game_board, "O"):
        show_board(game_board)
        print("😥 Oh no! Computer wins!")
        break

    if board_full(game_board):
        show_board(game_board)
        print("🤝 It's a draw!")
        break
