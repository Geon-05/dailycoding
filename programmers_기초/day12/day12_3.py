# day12 배열 만들기3

def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer.extend(arr[a:b+1])
    return answer