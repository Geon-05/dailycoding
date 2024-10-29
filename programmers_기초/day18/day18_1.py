# day18 x 사이의 개수

def solution(myString):
    answer = []
    temp = 0
    for i in myString:
        if i == 'x':
            answer.append(temp)
            temp = 0
            continue
        temp += 1
    answer.append(temp)
    return answer