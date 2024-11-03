# day22 유한소수 판별하기

# def sol1(num):
#     for i in range(1,num+1):
        

# def solution(a, b):
#     answer = 0
#     a_list = []
#     b_list = []
#     for num in range(2,a+1):
#         if a % num == 0:
#             a_list.append(num)
#     for num in range(2,b+1):
#         if b % num == 0:
#             b_list.append(num)
#     for i in a_list:
#         print(i)
#         if i in b_list:
#             b =  b / i
#     print(b)
#     return answer

def prime(num):
    answer = []
    x = 2
    while x <= num:
        if num % x == 0:
            answer.append(x)
            num //= x
        else:
            x += 1
    return answer

def solution(a, b):
    answer = 1
    a_prime = prime(a)
    b_prime = prime(b)
    tmp_prime = []
    for i in a_prime:
        if i in b_prime:
            b_prime.remove(i)
    for i in b_prime:
        if i not in [2,5]:
            tmp_prime.append(i)
    if len(tmp_prime) > 0:
        answer = 2
    return answer


print(solution(7,20))
print(solution(11,22))
print(solution(12,21))
print(solution(9,18))
print(solution(1,8))
print(solution(3,9))