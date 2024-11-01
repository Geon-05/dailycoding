# day19 빈 배열에 추가, 삭제하기

def solution(arr, flag):
    answer = []
    for idx, bool_flag in enumerate(flag):
        if bool_flag:
            for i in range(arr[idx]*2):
                answer.append(arr[idx])
        else:
            for i in range(arr[idx]):
                answer.pop()
    return answer