# day19 잘라서 배열로 저장하기

def solution(my_str, n):
    answer = []
    num = 1
    tmp = ''
    for i in my_str:
        tmp += i
        num += 1
        if num == n+1:
            answer.append(tmp)
            num = 1
            tmp = ''
    if tmp != '':
        answer.append(tmp)
    return answer