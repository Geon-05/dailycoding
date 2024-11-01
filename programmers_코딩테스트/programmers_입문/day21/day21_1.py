# day21 숨어있는 숫자의 덧셈2

def solution(my_string):
    answer = 0
    tmp_list = []
    tmp_str = ''
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            tmp_str += i
        else:
            tmp_list.append(tmp_str)
            tmp_str = ''
    tmp_list.append(tmp_str)
    for num in tmp_list:
        if num != '':
            answer += int(num)
    return answer

# def solution(my_string):
#     answer = 0
#     tmp_list = []
#     tmp_str = ''
#     for idx, i in enumerate(my_string):
#         if i in ['1','2','3','4','5','6','7','8','9','0']:
#             tmp_str += i
#         else:
#             tmp_list.append(tmp_str)
#             tmp_str = ''
#     for idx in range(len(tmp_list)-1,0,-1):
#         if tmp_list[idx] == '':
#             tmp_list.remove('')
#     if tmp_list == []:
#         return 0
#     else:
#         for num in tmp_list:
#             answer += int(num)
#     return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))
print(solution("R9"))