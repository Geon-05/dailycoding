# day20 캐릭터의 좌표

def solution(keyinput, board):
    answer = [0,0]
    x_minmax = [-(board[0]-1)/2,(board[0]-1)/2]
    y_minmax = [-(board[1]-1)/2,(board[1]-1)/2] 
    for key in keyinput:
        if key == 'up' and (y_minmax[1] > answer[1]):
            answer[1] += 1
        elif key == 'down' and (y_minmax[0] < answer[1]):
            answer[1] -= 1
        elif key == 'right' and (x_minmax[1] > answer[0]):
            answer[0] += 1
        elif key == 'left' and (x_minmax[0] < answer[0]):
            answer[0] -= 1
    return answer