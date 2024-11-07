def func_chk(width, height, x, y):
    answer = False
    if width >= x and height >= y:
        answer = True
    elif width >= y and height >= x:
        answer = True
    return answer

def fold(x, y):
    if x > y:
        x = int(x / 2)
    else:
        y = int(y / 2)
    return x, y

def solution(wallet, bill):
    answer = 0
    width = wallet[0]
    height = wallet[1]
    x = bill[0]
    y = bill[1]
    while True:
        if func_chk(width, height, x, y):
            break
        x, y = fold(x, y)
        answer += 1
    return answer

print(solution([30, 15],[26, 17]))
print(solution([50, 50],[100, 241]))
print(solution([0,0],[0,0]))