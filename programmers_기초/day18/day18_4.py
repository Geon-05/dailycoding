# day18 문자열 바꿔서 찾기

def solution(myString, pat):
    answer = 0
    tmp = ''
    for char_base in myString:
        if char_base == 'A':
            tmp += 'B'
        else:
            tmp += 'A'
    if len(tmp) < len(pat):
        return answer
    for i in range(len(myString)-len(pat)+1):
        if tmp[i:i+len(pat)] == pat:
            answer = 1
            break
    return answer