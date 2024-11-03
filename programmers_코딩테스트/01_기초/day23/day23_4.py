# day23 주사위 게임1

def solution(a, b):
    answer = 0
    a_odd_bool = (a % 2 == 1)
    b_odd_bool = (b % 2 == 1)
    if a_odd_bool and b_odd_bool:
        answer = a ** 2 + b ** 2
    elif a_odd_bool or b_odd_bool:
        answer = 2 * (a + b)
    else:
        answer = a - b
        if answer < 0:
            answer = -answer
    return answer

print(solution(3,5))