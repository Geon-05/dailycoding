# day10 qr code

def solution(q, r, code):
    answer = ''
    for idx, i in enumerate(code):
        if idx%q == r:
            answer += i
    return answer