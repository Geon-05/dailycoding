# day23 특이한 정렬

def solution(numlist, n):
    answer = []
    tmp_dict = {}
    for num in numlist:
        tmp_num = 0
        if num - n >= 0:
            tmp_num = num - n
        else:
            tmp_num = -(num - n)
        
        if tmp_num not in tmp_dict.keys():
            tmp_dict[tmp_num] = [num]
        else:
            tmp_dict[tmp_num].append(num)
    for i in sorted(tmp_dict.keys()):
        if len(tmp_dict[i]) > 1:
            answer.append(max(tmp_dict[i]))
            answer.append(min(tmp_dict[i]))
        else:
            answer.append(tmp_dict[i][0])
    return answer

print(solution([1, 2, 3, 4, 5, 6],4))
print(solution([10000,20,36,47,40,6,10,7000],30))