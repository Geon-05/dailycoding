# day21 외계어 사전

def solution(spell, dic:list):
    answer = 2
    tmp = ''
    for i in dic:
        i = sorted(i)
        for j in spell:
            if j in i:
                i.remove(j)
            else:
                i.append('zz')
        if i == []:
            answer = 1
            break
    return answer

item1_1 = ["p", "o", "s"]
item1_2 = ["sod", "eocd", "qixm", "adio", "soo"]

item2_1 = ["z", "d", "x"]
item2_2 = ["def", "dww", "dzx", "loveaw"]

item3_1 = ["s", "o", "m", "d"]
item3_2 = ["moos", "dzx", "smm", "sunmmo", "som"]


print(solution(item1_1, item1_2))
print(solution(item2_1, item2_2))
print(solution(item3_1, item3_2))