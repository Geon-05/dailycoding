# day19 중복된 숫자 개수

def solution(array, n):
    answer = 0
    for num in array:
        if num == n:
            answer += 1
    return answer