# day7 배열 만들기2

def solution(l, r):
    answer = []
    for i in range(l,r+1):
        tmp=[]
        for j in list(str(i)):
            if j in ['1','2','3','4','6','7','8','9']:
                tmp.append(1)
        if len(tmp) == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)