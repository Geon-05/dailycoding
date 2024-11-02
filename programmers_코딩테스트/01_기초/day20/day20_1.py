# day20 배열의 길이를 2의 거듭제곱으로 만들기

def solution(arr):
    answer = []
    n_chk = 0
    while True:
        if len(arr) <= 2 ** n_chk:
            break
        n_chk += 1
    for i in range(2 ** n_chk):
        if len(arr) > i:
            answer.append(arr[i])
        else:
            answer.append(0)
    return answer

item1_1 = [1, 2, 3, 4, 5, 6]

item2_1 = [58, 172, 746, 89]

item3_1 = [1]

print(solution(item1_1))
print(solution(item2_1))
print(solution(item3_1))