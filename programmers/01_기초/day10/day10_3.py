# day10 문자열 뒤집기

# def solution(my_string, s, e):
#     answer = ''
#     my_string = list(my_string)
#     if s == 0:
#         answer += my_string[e]
#         s = 1
#         for idx, i in enumerate(my_string[e:s-1:-1]):
#             if idx == 0:
#                 continue
#             my_string[idx+s] = i
#         for i in my_string:
#             answer += i
#         return answer
#     for idx, i in enumerate(my_string[e:s-1:-1]):
#         my_string[idx+s] = i
#     for i in my_string:
#         answer += i
#     return answer

def solution(my_string, s, e):
    answer = ''
    first = my_string[:s]
    middle = my_string[s:e+1]
    end = my_string[e+1:]
    middle = middle[::-1]
    answer = first+middle+end
    return answer

print(solution("Progra21Sremm3", 6, 12))
print(solution("Stanley1yelnatS", 4, 10))