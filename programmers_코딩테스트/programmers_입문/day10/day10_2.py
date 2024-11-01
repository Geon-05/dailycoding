# day10 2차원으로 만들기

def solution(num_list, n):
    answer = []
    for j in range(int(len(num_list)/n)):
        temp = []
        for k in range(n):
            temp.append(num_list[j*n+k])
        answer.append(temp)
    return answer