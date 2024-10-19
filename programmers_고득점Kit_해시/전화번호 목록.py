# def solution(phone_book:list):
#     answer = True
#     phone_book.sort(key=len)
#     efficiency = 1
#     for i in phone_book:
#         print(list(map(lambda x: x[:len(i)],phone_book[efficiency:])))
#         if i in list(map(lambda x: x[:len(i)],phone_book[efficiency:])):
#             answer = False
#             break
#         efficiency += 1
#     return answer


# 효율성이 가장 좋았던경우
# def solution(phone_book:list):
#     answer = True
#     length_dict = {}
#     for i in phone_book:
#         length = len(i)
#         if length not in length_dict:
#             length_dict[length] = []
#         length_dict[length].append(i)
#     length_list = list(length_dict.keys())
#     for i in range(len(length_list)-1):
#         for j in length_dict[length_list[i]]:
#             for k in length_list[i::-1]:
#                 for l in length_dict[k]:
#                     if j == l[:len(j)]:
#                         return False
#     return answer

# 정확도가 가장 높았던경우
# def solution(phone_book:list):
#     answer = True
#     phone_book.sort(key=len)
#     efficiency = 1
#     for i in phone_book:
#         if i in list(map(lambda x: x[:len(i)],phone_book[efficiency:])):
#             answer = False
#             break
#         efficiency += 1
#     return answer



# def solution(phone_book:list):
#     answer = True
#     length_dict = {}
#     for i in phone_book:
#         length = len(i)
#         if length not in length_dict:
#             length_dict[length] = []
#         length_dict[length].append(i)
#     length_list = list(length_dict.keys())
#     for i in range(len(length_list)-1):
#         for j in length_dict[length_list[i]]:
#             for k in length_list[:i+1:-1]:
#                 for l in length_dict[k]:
#                     if j == l[:len(j)]:
#                         return False
#     return answer

def solution(phone_book:list):
    answer = True
    length_dict = {}
    for i in phone_book:
        length = len(i)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(i)
    length_list = list(length_dict.keys())
    for idx, i in enumerate(length_list):
        for j in length_list[idx+1:]:
            for k in length_dict[i]:
                if k in list(map(lambda x: x[:i],length_dict[j])):
                    answer = False
                    break
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["123", "13", "134"]))
print(solution(["123", "12"]))
print(solution(["13", "23", "4444444", "12", "25"]))
print(solution(["12","123","1235","567","88"]))