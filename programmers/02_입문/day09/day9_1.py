# day9 개미 군단

def solution(hp):
    answer = 0
    while hp > 0:
        if hp >= 5:
            answer += 1
            hp -= 5
        elif hp >= 3:
            answer += 1
            hp -= 3
        else:
            answer += 1
            hp -= 1
    return answer