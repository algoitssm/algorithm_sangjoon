def poliomino(board: str):
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")

    if "X" in board:
        return -1

    return board


board = input()
ans = poliomino(board)
print(ans)