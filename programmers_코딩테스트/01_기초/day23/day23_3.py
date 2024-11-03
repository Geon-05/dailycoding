# day23 정수 찾기

def solution(num_list, n):
    answer = 0
    try:
        num_list.remove(n)
        answer = 1
    except:
        pass
    return answer