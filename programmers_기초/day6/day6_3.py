# day6 수 조작하기 2

def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        i = numLog[i] - numLog[i+1]
        if i == -1:
            answer += 'w'
        elif i == 1:
            answer += 's'
        elif i == -10:
            answer += 'd'
        elif i == 10:
            answer += 'a'
    return answer