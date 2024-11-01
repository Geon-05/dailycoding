# day11 카운트 다운

def solution(start_num, end_num):
    answer = []
    for i in range(end_num, start_num+1).__reversed__():
        answer.append(i)
    return answer