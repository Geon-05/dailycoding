# day7 수열과 구간 쿼리4

def solution(arr, queries):
    answer = arr
    for s, e, k in queries:
        for idx, i in enumerate(arr[s:e+1]):
            if (s+idx) % k == 0:
                answer[idx] += 1
    return answer