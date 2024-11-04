# day24 l로 만들기

import string

def solution(myString):
    answer = ''
    low_dict = {}
    for idx, i in enumerate(string.ascii_lowercase):
        low_dict[i] = idx + 1
    for char_base in myString:
        if low_dict[char_base] < 12:
            answer += 'l'
            continue
        answer += char_base
    return answer