# day3 두 수의 연산값 비교하기

def solution(a, b):
    answer = 0
    answer = a01(a,b)
    return answer

def a01(num1,num2):
    tmp1 = int(str(num1) + str(num2))
    tmp2 = int(2 * int(num1) * int(num2))
    if tmp1 > tmp2:
        return tmp1
    elif tmp2 > tmp1:
        return tmp2
    else:
        return tmp1