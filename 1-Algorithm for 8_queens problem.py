#check if the place is safe
def is_safe(row, col, board):
    for i in range(row):
        if board[i] == col:
            return False
        elif abs(board[i] - col) == abs(i - row):
            return False
    return True



#delete not_unique answers
def rotate(board):
    new_board = [0] * 8
    for i in range(8):
        col = board[i]
        new_board[col] = 7 - i
    return new_board

def flip(board):
    return[7 - col for col in board]
    
def all_cases(board):
    all_answers = []
    current = board[:]
    for j in range(4):
        all_answers.append(current)
        all_answers.append(flip(current))
        current = rotate(current)
    return all_answers

def is_unique(board, solutions):
    all_answers = all_cases(board)
    for s in solutions:
        if s in all_answers:
            return False
    return True



unique_solutions = []

#solving the problem with backtracking
def solve(board, row):
    if row == 8:
        if is_unique(board, unique_solutions):
            unique_solutions.append(board[:])
            return
    else:
        for col in range(8):
            if is_safe(row, col, board):
                board[row] = col
                solve(board, row+1)


#getting the answers
board = [0] * 8
solve(board, 0)

print("no of answers :", len(unique_solutions))

for solution in unique_solutions:
    print(solution)
 

###با آنکامنت کردن تابع ها و شرط ایف در تابع حل مساله فقط جواب های منحصر به فرد چاپ میشوند