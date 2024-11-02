# day7 콜라츠 수열 만들기

def solution(n):
    answer = []
    while True:
        answer.append(int(n))
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        
        if answer[-1] == 1:
            break
    return answer