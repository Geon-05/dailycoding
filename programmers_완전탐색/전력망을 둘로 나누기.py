
import copy

def solution(n, wires):
    answer = []
    temp = {}
    temp_list = []
    for a, b in wires:
        temp_list.append(a)
        temp_list.append(b)

    for a in set(temp_list):
        temp[a] = solution2(a, wires)
    
    for a, b in wires:
        as_temp = copy.deepcopy(temp)
        as_temp[a].remove(b)
        as_temp[b].remove(a)
        # print(as_temp)
        a_element = []
        b_element = []
        while True:
            why = 0
            if len(as_temp[a]) == 0:
                a_element.append(a)
            if len(as_temp[a]) > 0:
                for i in as_temp[a]:
                    a_element.append(i)
                    as_temp[a].remove(i)
                    why += 1
            if why == 0:
                break
        
        while True:
            why = 0
            for a in a_element:
                if len(as_temp[a]) == 0:
                    if a in a_element:
                        continue
                    a_element.append(a)
                if len(as_temp[a]) > 0:
                    for i in as_temp[a]:
                        a_element.append(i)
                        as_temp[a].remove(i)
                        why += 1
            if why == 0:
                break
        # print(a_element)
        
        b_element = n - len(set(a_element))
        
        if len(set(a_element)) - b_element > 0:
            min_num = len(set(a_element)) - b_element
        else:
            min_num = b_element - len(set(a_element))
        answer.append(min_num)
    # print(temp)
    # print(set(s_list+e_list))
    # print(set(s_list))
    # print(set(e_list))
    return min(answer)

def solution2(n, sub_list):
    answer = []
    for a,b in sub_list:
        if n == a:
            answer.append(b)
        if n == b:
            answer.append(a)
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

# def solution(n, wires):
#     answer = -1
#     temp = {}
#     s_list = []
#     e_list = []
#     for a, b in wires:
#         # s_list.append(a)
#         # e_list.append(b)
#         if a not in temp.keys():
#             temp[a] = [b]
#         else:
#             temp[a].append(b)
#         if b not in temp.keys():
#             temp[b] = [a]
#         else:
#             temp[b].append(a)
#     print(temp)
#     print(set(s_list+e_list))
#     print(set(s_list))
#     print(set(e_list))
#     for a, b in wires:
#         try:
#             part1 = 0
#             for i in temp[a]:
#                 if i in temp.keys():
#                     part1 += len(temp[i])
#             part2 = 0
#             for i in temp[b]:
#                 if i in temp.keys():
#                     part2 += len(temp[i])
#             print(part1,'/',part2)
#         except:
#             pass
#     # part1 =
#     # part2 = 
#     return answer

# import copy

# def solution(n, wires):
#     answer = 0
#     temp = {}
#     temp_list = []
#     for a, b in wires:
#         temp_list.append(a)
#         temp_list.append(b)

#     for a in set(temp_list):
#         temp[a] = solution2(a, wires)
    
#     for a, b in wires:
#         as_temp = copy.deepcopy(temp)
#         as_temp[a].remove(b)
#         as_temp[b].remove(a)
#         print(as_temp)
#         a_element = []
#         b_element = []
#         while True:
#             why = 0
#             if len(as_temp[a]) == 0:
#                 a_element.append(a)
#             if len(as_temp[a]) > 0:
#                 for i in as_temp[a]:
#                     a_element.append(a)
#                     as_temp[i].remove(a)
#                     a = i
#                     why += 1
#             if why == 0:
#                 break
#         print(a_element)
#         while True:
#             why = 0
#             if len(as_temp[b]) == 0:
#                 b_element.append(b)
#             if len(as_temp[b]) > 0:
#                 for i in as_temp[b]:
#                     b_element.append(b)
#                     as_temp[i].remove(b)
#                     b = i
#                     why += 1
#             if why == 0:
#                 break
#         print(b_element)
        
#         if len(a_element) - len(b_element) > 0:
#             min_num = len(a_element) - len(b_element)
#         else:
#             min_num = len(b_element) - len(a_element)
        
#         if answer > min_num:
#             answer = min_num
#     print(temp)
#     # print(temp)
#     # print(set(s_list+e_list))
#     # print(set(s_list))
#     # print(set(e_list))
#     return answer

# def solution2(n, sub_list):
#     answer = []
#     for a,b in sub_list:
#         if n == a:
#             answer.append(b)
#         if n == b:
#             answer.append(a)
#     return answer

# def solution(n, wires):
#     answer = -1
#     temp = {}
#     s_list = []
#     e_list = []
#     for a, b in wires:
#         s_list.append(a)
#         e_list.append(b)
#         if a not in temp.keys():
#             temp[a] = [b]
#         else:
#             temp[a].append(b)
#     print(temp)
#     print(set(s_list+e_list))
#     print(set(s_list))
#     print(set(e_list))
#     return answer

# def solution(n, wires):
#     answer = -1
#     a_list = []
#     b_list = []
#     for a, b in wires:
#         temp = wires[:]
#         temp.remove([a,b])
#         print(temp)
#         for i in temp:
#             if a in i:
#                 a_list.append(i)
#             if b in i:
#                 b_list.append(i)
#         print('aList',a_list)
#         print('bList',b_list)
#         print(len(b_list)-len(a_list))
#     print(temp)
#     return answer

