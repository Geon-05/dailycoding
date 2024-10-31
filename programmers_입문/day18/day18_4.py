# day18 문자열 정렬하기1

def solution(my_string):
    answer = ''
    tmp = my_string.lower()
    for i in sorted(tmp):
        answer += i
    return answer