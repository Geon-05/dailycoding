# day25 정사각형으로 만들기

def solution(arr):
    if len(arr) < len(arr[0]):
        for i in range(len(arr[0])-len(arr)):
            tmp = []
            for i in range(len(arr[0])):
                tmp.append(0)
            arr.append(tmp)
    else:
        for i in range(len(arr)):
            for j in range(len(arr)-len(arr[i])):
                arr[i].append(0)
    answer = arr
    return answer

print(solution([[1]]))
print(solution([[1,2]]))
print(solution([[1],[2]]))
print(solution([[1,2],[2,3]]))
print(solution([[1,2,3,4]]))