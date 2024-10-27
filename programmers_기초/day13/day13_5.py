# day13 n개 간격의 원소들

def solution(num_list, n):
    answer = []
    answer= num_list[::n]
    return answer