# day16 문자열 계산하기

def solution(my_string:str):
    answer = 0
    my_string = my_string.split(' ')
    num_list = my_string[::2]
    oper_list = my_string[1::2]
    temp = int(num_list.pop(0))
    while len(num_list) > 0:
        if oper_list.pop(0) == '+':
            temp += int(num_list.pop(0))
        else:
            temp -= int(num_list.pop(0))
    answer = temp
    return answer

print(solution("3 + 4"))
print(solution("10 + 1"))
print(solution("10 - 1"))
print(solution("10 - 100"))
print(solution("0 - 10"))