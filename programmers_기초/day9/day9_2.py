# day9 부분 문자열 이어 붙여 문자열 만들기

def solution(my_strings, parts):
    answer = ''
    for idx, i in enumerate(my_strings):
        s = parts[idx][0]
        e = parts[idx][1]
        answer += i[s:e+1]
    return answer