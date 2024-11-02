# day20 문열 묶기

def solution(strArr):
    answer = 0
    tmp_dict = {}
    for i in strArr:
        if len(i) not in tmp_dict.keys():
            tmp_dict[len(i)] = 1
        else:
            tmp_dict[len(i)] += 1
    for i in tmp_dict.keys():
        if answer < tmp_dict[i]:
            answer = tmp_dict[i]
    return answer