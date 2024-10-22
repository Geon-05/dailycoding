# day8 문자열 여러 번 뒤집기

def solution(my_string, queries):
    answer = ''
    for i, j in queries:
        temp = my_string[i:j+1][::-1]
        my_string = my_string[:i] + temp + my_string[j+1:]
    answer = my_string
    return answer