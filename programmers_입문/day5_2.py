# day5 아이스 아메리카노

def solution(money):
    answer = []
    americano = 0
    while money >= 5500:
        americano += 1
        money -= 5500
    answer.append(americano)
    answer.append(money)
    return answer