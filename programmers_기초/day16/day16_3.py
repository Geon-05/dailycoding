# day16 배열에서 문자열 대소문자 변환하기

def solution(strArr):
    answer = []
    for idx, i in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
    return answer