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

# def solution(phone_book:list):
#     answer = True
#     length_dict = {}
#     for i in phone_book:
#         length = len(i)
#         if length not in length_dict:
#             length_dict[length] = []
#         length_dict[length].append(i)
#     length_list = list(length_dict.keys())
#     for idx, i in enumerate(length_list):
#         for j in length_list[idx+1:]:
#             for k in length_dict[i]:
#                 if k in list(map(lambda x: x[:i],length_dict[j])):
#                     answer = False
#                     break
#     return answer

def solution(phone_book:list):
    answer = True
    if phone_book.count('') > 0:
        answer = False
        return answer
    while True:
        temp, answer = check(phone_book)
        if answer == False:
            return answer
        num = 0
        for i in temp.keys():
            if len(temp[i]) == 0:
                num += 1
            elif len(temp[i]) == 1:
                num += 1
            elif len(temp[i]) > 1:
                answer = solution(temp[i])
                if answer == False:
                    return answer
        if num == 10:
            return answer

def check(phone_list):
    temp = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    answer = True
    for idx, i in enumerate(phone_list):
        try:
            i[0]
        except:
            phone_list.pop(idx)
            continue
        if i[0] == '0':
            temp['0'].append(i[1:])
            count0 += 1
        elif i[0] == '1':
            temp['1'].append(i[1:])
            count1 += 1
        elif i[0] == '2':
            temp['2'].append(i[1:])
            count2 += 1
        elif i[0] == '3':
            temp['3'].append(i[1:])
            count3 += 1
        elif i[0] == '4':
            temp['4'].append(i[1:])
            count4 += 1
        elif i[0] == '5':
            temp['5'].append(i[1:])
            count5 += 1
        elif i[0] == '6':
            temp['6'].append(i[1:])
            count6 += 1
        elif i[0] == '7':
            temp['7'].append(i[1:])
            count7 += 1
        elif i[0] == '8':
            temp['8'].append(i[1:])
            count8 += 1
        elif i[0] == '9':
            temp['9'].append(i[1:])
            count9 += 1
    if len(temp['0']) != count0:
        answer = False
    elif len(temp['1']) != count1:
        answer = False
    elif len(temp['2']) != count2:
        answer = False
    elif len(temp['3']) != count3:
        answer = False
    elif len(temp['4']) != count4:
        answer = False
    elif len(temp['5']) != count5:
        answer = False
    elif len(temp['6']) != count6:
        answer = False
    elif len(temp['7']) != count7:
        answer = False
    elif len(temp['8']) != count8:
        answer = False
    elif len(temp['9']) != count9:
        answer = False
    return temp, answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["123", "13", "134"]))
print(solution(["123", "12"]))
print(solution(["13", "23", "4444444", "12", "25"]))
print(solution(["12","123","1235","567","88"]))