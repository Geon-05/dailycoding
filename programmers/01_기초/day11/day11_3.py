# day11 글자 지우기

def solution(my_string, indices):
    answer = ''
    for idx, i in enumerate(my_string):
        if idx not in indices:
            answer += i
    return answer