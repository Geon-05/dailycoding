# day12 모음 제거

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in ['a','e','i','o','u']:
            answer += i
    return answer