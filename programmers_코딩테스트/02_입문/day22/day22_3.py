# day22 겹치는 선분의 길이

def solution(lines:list):
    answer = 0
    line_dict = {}
    for a, b in lines:
        for i in range(a, b):
            if i not in line_dict.keys():
                line_dict[i] = 1
            else:
                line_dict[i] += 1
    for i in line_dict.keys():
        if line_dict[i] > 1:
            answer += 1
    return answer