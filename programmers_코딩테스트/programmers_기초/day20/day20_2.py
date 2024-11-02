# day20 배열 비교하기

def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        arr1_add = 0
        arr2_add = 0
        for num1 in arr1:
            arr1_add += num1
        for num2 in arr2:
            arr2_add += num2
        if arr1_add > arr2_add:
            answer = 1
        elif arr1_add < arr2_add:
            answer = -1
        else:
            answer = 0
    return answer