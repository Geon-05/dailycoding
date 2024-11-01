# day13 컨트롤 제트

def solution(s:str):
    answer = 0
    s_list = s.split(' ')
    for idx, i in enumerate(s_list):
        if i == 'Z':
            s_list[idx-1] = 0
            s_list[idx] = 0
    for i in s_list:
        answer += int(i)
    return answer