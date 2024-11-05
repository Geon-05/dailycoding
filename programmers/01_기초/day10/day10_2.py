# day10 접두사인지 확인하기

def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(is_prefix)):
        if len(my_string) < len(is_prefix):
            answer = 0
            break
        if my_string[i] != is_prefix[i]:
            answer = 0
            break
        else:
            answer = 1
    return answer