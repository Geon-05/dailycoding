# day9 접미사 배열

def solution(my_string):
    answer = []
    my_list = list(my_string)
    for i in range(len(my_list)):
        answer.append(my_string[i:])
        answer = sorted(answer)
    return answer