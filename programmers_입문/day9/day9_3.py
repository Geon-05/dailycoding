# day9 가위 바위 보

def solution(rsp):
    answer = ''
    game = {
        '5':'2',
        '2':'0',
        '0':'5'
    }
    for i in list(rsp):
        answer += game[i]
    return answer