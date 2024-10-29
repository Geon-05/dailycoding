# day17 공백으로 구분하기2

def solution(my_string):
    answer = []
    while True:
        temp = my_string + ''
        my_string = my_string.replace('  ',' ')
        if temp == my_string:
            break
    answer = my_string.split(' ')
    for i in answer:
        if i == '':
            answer.remove('')
    return answer

print(solution(" i    love  you"))
print(solution("    programmers  "))