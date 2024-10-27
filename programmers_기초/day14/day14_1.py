# day14 홀수 vs 짝수

def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for i in num_list[0::2]:
        odd += i
    for i in num_list[1::2]:
        even += i
    if odd > even:
        answer = odd
    else:
        answer = even
    return answer