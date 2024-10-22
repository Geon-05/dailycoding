# day8 간단한 논리 연산

def solution(x1, x2, x3, x4):
    answer = True
    if x1 or x2:
        tmp1 = True
    else:
        tmp1 = False
    if x3 or x4:
        tmp2 = True
    else:
        tmp2 = False
    if tmp1 and tmp2:
        answer = True
    else:
        answer = False
    return answer