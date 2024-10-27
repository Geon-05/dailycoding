# day13 중복된 문자 제거

def solution(my_string):
    answer = ''
    temp = []
    for i in my_string:
        if i not in temp:
            temp.append(i)
            answer += i
    return answer