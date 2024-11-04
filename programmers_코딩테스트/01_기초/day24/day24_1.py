# day24 커피 심부름

def solution(order):
    answer = 0
    for order_pro in order:
        if 'latte' in order_pro:
            answer += 5000
            continue
        answer += 4500
    return answer