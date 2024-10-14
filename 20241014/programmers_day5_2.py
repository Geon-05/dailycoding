# day5 등차수열의 특정한 항만 더하기

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a
        a += d
    return answer

included = [True,False,False,True,True]
res = solution(3, 4, included)
print(res)

included = [False,False,False,True,False,False,False]
res = solution(7, 1, included)
print(res)