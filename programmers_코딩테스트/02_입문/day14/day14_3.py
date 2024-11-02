# day14 암호 해독

def solution(cipher, code):
    answer = ''
    answer = cipher[code-1::code]
    return answer