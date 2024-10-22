# day8 외계행성의 나이

def solution(age):
    answer = ''
    num_dict = {}
    simple_str = 'abcdefghij'
    for idx, i in enumerate(simple_str):
        num_dict[str(idx)] = i
    for i in str(age):
        answer += num_dict[i]
    return answer