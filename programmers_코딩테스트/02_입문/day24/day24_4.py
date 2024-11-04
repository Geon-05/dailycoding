# day24 k의 개수

def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        answer += str(num).count(str(k))
    return answer