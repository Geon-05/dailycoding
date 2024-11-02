# day22 저주의 숫자3

def solution(n):
    answer = 0
    tmp_num = 1
    tmp_list = []
    while len(tmp_list) < n:
        if (tmp_num % 3 == 0) or ('3' in str(tmp_num)):
            tmp_num += 1
            continue
        tmp_list.append(tmp_num)
        tmp_num += 1
    print("list : ",tmp_list)
    answer = tmp_list[-1]
    return answer

print(solution(15))