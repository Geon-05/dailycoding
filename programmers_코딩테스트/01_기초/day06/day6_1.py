# day6 마지막 두 원소

def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2]:
        tmp = num_list[-1] - num_list[-2]
        answer.append(tmp)
    else:
        tmp = num_list[-1] * 2
        answer.append(tmp)
    return answer