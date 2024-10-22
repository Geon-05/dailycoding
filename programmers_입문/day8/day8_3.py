# day8 진료순서 정하기

def solution(emergency):
    answer = []
    a_dict = {}
    for idx, i in enumerate(sorted(emergency,reverse=True)):
        a_dict[i] = idx+1
    for i in emergency:
        answer.append(a_dict[i])
    return answer