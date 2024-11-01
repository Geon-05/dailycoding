# day19 무작위로 K개의 수 뽑기

def solution(arr, k):
    answer = []
    i = 0
    while len(answer) < k:
        try:
            if arr[i] not in answer:
                answer.append(arr[i])
            i += 1
        except:
            answer.append(-1)
    return answer

print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))