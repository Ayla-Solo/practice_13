def isValidSudoku(board):

    # проверка строк
    for row in board:
        nums = []

        for cell in row:
            if cell != ".":          # проверяем только заполненные клетки
                if cell in nums:     # если цифра уже была
                    return False
                nums.append(cell)

    # проверка столбцов
    for col in range(9):
        nums = []

        for row in range(9):
            if board[row][col] != ".":
                if board[row][col] in nums:
                    return False
                nums.append(board[row][col])

    # проверка квадратов 3x3
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):

            nums = []

            # обходим клетки внутри квадрата
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):

                    if board[row][col] != ".":
                        if board[row][col] in nums:
                            return False
                        nums.append(board[row][col])

    return True   # если нарушений нет