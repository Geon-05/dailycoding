# day22 0떼기

def solution(n_str):
    answer = ''
    search = False
    for i in n_str:
        if i != '0':
            search = True
        if search:
            answer += i
    return answer