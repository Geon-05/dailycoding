# day11 주사위의 개수

def solution(box, n):
    answer = 1
    for i in box:
        answer *= int(i/n)
    return answer