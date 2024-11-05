# day15 1로 만들기

def solution(num_list):
    answer = 0
    for i in num_list:
        num = i
        while True:
            if num == 1:
                break
            if num % 2 == 0:
                num /= 2
                answer += 1
            elif num % 2 == 1:
                num -= 1
                num /= 2
                answer += 1
    return answer

print(solution([12, 4, 15, 1, 14]))