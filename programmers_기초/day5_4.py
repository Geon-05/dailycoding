# day5 원소들의 곱과 합

def solution(num_list):
    answer = 0
    mul_res = 1
    sum_res = 0
    for i in num_list:
        mul_res *= i
        sum_res += i
    square = sum_res ** 2
    if mul_res < square:
        answer = 1
    else:
        answer = 0
    return answer

