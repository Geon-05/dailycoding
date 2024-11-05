# day11 팩토리얼

def solution(n):
    answer = 0
    i = 1
    while True:
        j = 1
        for k in range(1, i):
            j *= k
        if n < j:
            break
        i += 1
    answer = i - 2
    return answer