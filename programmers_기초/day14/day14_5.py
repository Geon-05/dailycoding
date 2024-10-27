# day14 수열과 구간 쿼리1

def solution(arr, queries):
    answer = arr
    for a, b in queries:
        for idx, i in enumerate(arr[a:b+1]):
            arr[idx+a] += 1
    return answer