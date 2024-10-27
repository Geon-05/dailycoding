# day13 왼쪽 오른쪽

def solution(str_list):
    answer = []
    for idx, i in enumerate(str_list):
        if i == 'l':
            answer = str_list[:idx]
            break
        if i == 'r':
            answer = str_list[idx+1:]
            break
    return answer