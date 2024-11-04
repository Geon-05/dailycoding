# day24 조건에 맞게 수열 변환하기3

def solution(arr, k):
    answer = []
    if k % 2 == 1:
        answer = [x * k for x in arr]
    else:
        answer = [x + k for x in arr]
    return answer