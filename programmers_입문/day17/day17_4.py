# day17 OX퀴즈

def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split(' ')
        if i[1] == '+':
            if i[4] == str(int(i[0]) + int(i[2])):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if i[4] == str(int(i[0]) - int(i[2])):
                answer.append('O')
            else:
                answer.append('X')
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))