# day3 더 크게 합치기

def solution(a, b):
    answer = 0
    if int(str(a)+str(b)) > int(str(b)+str(a)):
        answer = int(str(a)+str(b))
    else:
        answer = int(str(b)+str(a))
    return answer

print(solution(9, 91))
print(solution(89, 8))
print(solution(72, 72))