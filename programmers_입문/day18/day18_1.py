# day18 문자열안에 문자열

def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer