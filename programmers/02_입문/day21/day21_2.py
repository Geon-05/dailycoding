# day21 안전지대

def solution(board):
    answer = 0
    n = len(board) - 1
    for y_idx, y in enumerate(board):
        for x_idx, x in enumerate(y):
            if x % 2 == 1:
                for i in [y_idx-1, y_idx, y_idx+1]:
                    for j in [x_idx-1, x_idx, x_idx+1]:
                        if i < 0 or j < 0 or i > n or j > n:
                            pass
                        else:
                            board[i][j] += 2
    print(board)
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))