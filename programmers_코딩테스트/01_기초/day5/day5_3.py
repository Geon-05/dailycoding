# day5 주사위 게임 2

def solution(a, b, c):
    answer = 0
    if len(set([a,b,c])) == 3:
        answer = a+b+c
    elif len(set([a,b,c])) == 2:
        answer = (a+b+c)*(a**2+b**2+c**2)
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    return answer

