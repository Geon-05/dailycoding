# day11 문자 개수 세기

def solution(my_string):
    answer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    str_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    for i in my_string:
        for idx, j in enumerate(str_list):
            if i == j:
                answer[idx] += 1
    return answer