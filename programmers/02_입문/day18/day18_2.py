# day18 제곱수 판별하기

def solution(n):
    answer = 2
    for i in range(1,n+1):
        if n % i == 0:
            tmp = n / i
            if tmp / i == 1:
                answer = 1
    return answer