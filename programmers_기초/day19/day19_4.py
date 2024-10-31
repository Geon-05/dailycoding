# day19 배열 만들기6

def solution(arr):
    answer = []
    stk = []
    i = 0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
    answer = stk
    if answer == []:
        answer.append(-1)
    return answer