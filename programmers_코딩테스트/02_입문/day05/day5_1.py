# day5 옷가게 할인 받기

def solution(price):
    answer = 0
    dis = 0
    if price >= 500000:
        dis = price * 0.2
    elif price >= 300000:
        dis = price * 0.1
    elif price >= 100000:
        dis = price * 0.05
    answer = price - dis
    return int(answer)