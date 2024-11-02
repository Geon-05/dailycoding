# day22 배열의 원소 삭제하기

import copy

def solution(arr, delete_list):
    answer = []
    arr_copy = copy.copy(arr)
    for del_str in delete_list:
        for arr_str in arr:
            if del_str == arr_str:
                arr_copy.remove(del_str)
    answer = arr_copy
    return answer

item1_1 = [293, 1000, 395, 678, 94]
item1_2 = [94, 777, 104, 1000, 1, 12]

item2_1 = [110, 66, 439, 785, 1]
item2_2 = [377, 823, 119, 43]

print(solution(item1_1, item1_2))
print(solution(item2_1, item2_2))