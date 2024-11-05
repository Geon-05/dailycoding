# day21 문자열 정수의 합

def solution(num_str):
    answer = 0
    for num in num_str:
        answer += int(num)
    return answer