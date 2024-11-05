# day25 문자열 밀기

def solution(A:str, B):
    answer = 0
    while len(A) > answer:
        tmp = A[-1]
        for char_base in A[:-1]:
            tmp += char_base
        if tmp == B:
            return answer
        A = tmp
        answer += 1
    answer = -1
    return answer

print(solution('hello','ohell'))