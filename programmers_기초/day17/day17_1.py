# day17 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

def solution(myString, pat):
    answer = ''
    for i in range(len(myString),len(pat)-1,-1):
        if myString[i-len(pat):i] == pat:
            answer = myString[:i]
            break
    return answer