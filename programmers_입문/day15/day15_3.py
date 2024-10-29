# day15 한 번만 등장한 문자

def solution(s):
    answer = ''
    temp_dict = {}
    temp_list = []
    for i in s:
        if i not in temp_dict.keys():
            temp_dict[i] = 1
        else:
            temp_dict[i] += 1
    for i in temp_dict.keys():
        if temp_dict[i] == 1:
            temp_list.append(i)
    temp_list.sort()
    for i in temp_list:
        answer += i
    return answer

print(solution("abdc"))