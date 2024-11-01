# day12 숨어있는 숫자의 덧셈1

def solution(my_string):
    answer = 0
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9']:
            answer += int(i)
    return answer