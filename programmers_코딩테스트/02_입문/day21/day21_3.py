# day21 삼각형의 완성조건2

def solution(sides):
    answer = 0
    con1 = max(sides) + min(sides)
    con2 = max(sides) - min(sides)
    answer = con1 - con2 - 1
    return answer