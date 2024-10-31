# day18 세균 증식

def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer