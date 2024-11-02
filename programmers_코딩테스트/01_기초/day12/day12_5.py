# day12 배열 조각하기

def solution(arr, query):
    answer = arr
    for idx, i in enumerate(query):
        if idx%2==1:
            answer = answer[i:]
        else:
            answer = answer[:i+1]
    return answer