# day22 유한소수 판별하기
def sol1(a,b):
    while

def solution(a, b):
    answer = 0
    a_list = []
    b_list = []
    for num in range(2,a+1):
        if a % num == 0:
            a_list.append(num)
    for num in range(2,b+1):
        if b % num == 0:
            b_list.append(num)
    for i in a_list:
        if i in b_list:
            b /= i
    
    return answer

print(solution(7,20))
print(solution(11,22))
print(solution(12,21))