# day10 공 던지기

def solution(numbers, k):
    answer = 0
    answer = numbers[(k*2-1) % len(numbers) - 1]
    return answer