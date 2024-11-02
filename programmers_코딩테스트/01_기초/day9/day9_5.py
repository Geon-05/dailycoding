# day9 접미사인지 확인하기

def solution_list(my_string):
    answer = []
    my_list = list(my_string)
    for i in range(len(my_list)):
        answer.append(my_string[i:])
        answer = sorted(answer)
    return answer

def solution(my_string, is_suffix):
    answer = 0
    if is_suffix in solution_list(my_string):
        answer = 1
    else:
        answer = 0
    return answer