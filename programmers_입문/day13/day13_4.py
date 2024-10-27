# day13 삼각형의 완성조건1

def solution(sides:list):
    answer = 0
    side_max = max(sides)
    sides.remove(side_max)
    if side_max < sides[0]+sides[1]:
        answer = 1
    else:
        answer = 2
    return answer