# day20 배열의 길이에 따라 다른 연산하기

def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for idx, i in enumerate(arr):
            if idx % 2 == 0:
                answer.append(i + n)
            else:
                answer.append(i)
    else:
        for idx, i in enumerate(arr):
            if idx % 2 == 0:
                answer.append(i)
            else:
                answer.append(i + n)
    return answer