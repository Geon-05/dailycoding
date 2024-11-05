# day13 순서 바꾸기

def solution(num_list, n):
    answer = []
    answer.extend(num_list[n:])
    answer.extend(num_list[:n])
    return answer