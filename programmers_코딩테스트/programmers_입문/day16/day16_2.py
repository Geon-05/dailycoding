# day16 가장 큰 수 찾기

def solution(array:list):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer