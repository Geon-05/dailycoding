# day4 flag에 따라 다른 값 변환하기

def solution(a, b, flag):
    answer = 0
    if flag:
        answer = a + b
    else:
        answer = a - b
    return answer