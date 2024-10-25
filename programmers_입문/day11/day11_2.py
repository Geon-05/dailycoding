# day11 합성수 찾기

def solution(n):
    answer = 0
    for i in range(1,n+1):
        temp = 0
        for j in range(1,i+1):
            if i % j == 0:
                temp += 1
        if temp > 2:
            answer += 1
    return answer