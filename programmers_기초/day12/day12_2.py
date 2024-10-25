# day12 첫 번째로 나오는 음수

def solution(num_list):
    answer = 0
    for idx, i in enumerate(num_list):
        if i < 0:
            answer = idx
            break
        answer = -1
    return answer