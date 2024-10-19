# day6 짝수 홀수 개수

def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        elif i % 2 == 1:
            odd += 1
    answer.append(even)
    answer.append(odd)
    return answer