# day12 2의 영역

def solution(arr):
    answer = []
    s_num = None
    e_num = None
    for idx, i in enumerate(arr):
        if i == 2 and s_num == None:
            s_num = idx
        if i == 2:
            e_num = idx
    if s_num == None:
        answer.append(-1)
    elif s_num == e_num:
        answer = [arr[s_num]]
    else:
        answer = arr[s_num:e_num+1]
    return answer