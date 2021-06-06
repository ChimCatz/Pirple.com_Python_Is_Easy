

def board_dimensions(board_rows, board_columns):
    max_col = 140
    max_row = 12
    board_rows = int(board_rows)
    board_columns = int(board_columns)
    if board_columns <= max_col and board_rows <= max_row:
        for row in range(board_rows):
            if row % 2 == 0:
                for col in range(1, board_columns):
                    if col % 2 == 1:
                        if col != board_columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * board_columns)
        return True
    else:
        reason = ""
        if board_columns > max_col and board_rows > max_row:
            reason = "board_columns and board_rows"
        elif board_columns > max_col:
            reason += "board_columns"
        elif board_rows > max_row:
            reason += "board_rows"
        print("Sorry, cannot create the board, too many {0:s}.".format(reason))
        return False


board_dimensions(6, 6)