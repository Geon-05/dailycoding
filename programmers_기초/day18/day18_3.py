# day18 rny_string

def solution(binomial):
    answer = 0
    binomial = binomial.split(' ')
    a = int(binomial[0])
    b = int(binomial[2])
    op = binomial[1]
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b
    return answer