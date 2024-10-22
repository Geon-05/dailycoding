# day8 9로 나눈 나머지

def solution(number):
    answer = 0
    temp = 0
    for i in str(number):
        temp += int(i)
    answer = temp % 9
    return answer