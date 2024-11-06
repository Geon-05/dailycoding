# day25 다음에 올 숫자

def solution(common):
    answer = 0
    if common[0] - common[1] == common[1] - common[2]:
        answer = common[-1] * 2 - common[-2] 
    else:
        answer = common[-1] ** 2 / common[-2]
    return answer