# day24 특별한 이차원 배열1

def solution(n):
    answer = []
    for x in range(n):
        tmp = []
        for y in range(n):
            if x == y:
                tmp.append(1)
                continue
            tmp.append(0)
        answer.append(tmp)
    return answer