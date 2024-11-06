# day25 문자열 밀기

def solution(A:str, B):
    answer = 0
    tmp = A
    while len(A) > answer:
        if tmp == B:
            return answer
        tmp = A[-1]
        for char_base in A[:-1]:
            tmp += char_base
        A = tmp
        answer += 1
    answer = -1
    return answer

print(solution('hello','ohell'))