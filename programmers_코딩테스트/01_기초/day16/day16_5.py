# day16 특정한 문자를 대문자로 바꾸기

def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if alp == i :
            answer += i.upper()
        else:
            answer += i
    return answer