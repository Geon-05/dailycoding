# day6 수열과 구간 쿼리2

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = []
        for i in arr[s:e+1]:
            if i > k:
                temp.append(i)
        if temp:
            answer.append(min(temp))
        else:
            answer.append(-1)
    return answer