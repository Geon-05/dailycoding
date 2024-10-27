# day15 조건에 맞게 수열 변환하기2

import copy

def solution(arr):
    answer = 0
    answer_temp = copy.deepcopy(arr)
    while True:
        temp = []
        for i in answer_temp:
            if (i >= 50) and (i % 2 == 0):
                temp.append(int(i/2))
            elif (i < 50) and (i % 2 == 1):
                temp.append(i * 2 + 1)
            else:
                temp.append(i)
        answer += 1
        for idx, i in enumerate(temp):
            if i != answer_temp[idx]:
                answer_temp = copy.deepcopy(temp)
                break
            if idx + 1 == len(temp):
                return answer - 1
        
print(solution([1, 2, 3, 100, 99, 98]))
print(solution([63]))
print(solution([2]))