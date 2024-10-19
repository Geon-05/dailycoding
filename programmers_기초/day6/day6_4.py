# day6 수열과 구간 쿼리 3

def solution(arr, queries):
    answer = []
    for i, j in queries:
        temp = (arr[i], arr[j])
        arr[j] = temp[0]
        arr[i] = temp[1]
    answer = arr
    return answer