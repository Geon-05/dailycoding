# day12 소인수분해

def solution(n):
    answer = []
    p_num = []
    for i in range(1,n+1):
        temp = []
        for j in range(1,i+1):
            if i % j == 0:
                temp.append(j)
        if len(temp) == 2:
            p_num.append(i)
    for i in p_num:
        if n % i == 0:
            answer.append(i)
    return answer