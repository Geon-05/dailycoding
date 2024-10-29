# day17 숫자 찾기

def solution(num, k):
    answer = -1
    for idx, i in enumerate(str(num)):
        if i == str(k):
            answer = idx + 1
            break
    return answer