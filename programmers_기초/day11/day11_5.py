# day11 가까운 1 찾기

def solution(arr, idx):
    answer = 0
    for index, i in enumerate(arr[idx:]):
        if i == 1:
            answer = index + idx
            break
        answer = -1
    return answer