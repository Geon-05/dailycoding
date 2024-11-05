# day25 정수를 나선형으로 배치하기

def solution(n):
    answer = []
    for y in range(n):
        tmp = []
        for x in range(n):
            tmp.append([y,x])
        answer.append(tmp)
    pattern = [['y', True],['x',True],['y',False],['x',False]]
    pattern_num = 0
    x = 0
    y = -1
    i = 1
    n = n * 2
    while n > 0:
        for tmp2 in range(int(n/2)):
            if pattern[pattern_num][0] == 'x' and pattern[pattern_num][1]:
                x += 1
            elif pattern[pattern_num][0] == 'x' and not pattern[pattern_num][1]:
                x -= 1
            elif pattern[pattern_num][0] == 'y' and pattern[pattern_num][1]:
                y += 1
            elif pattern[pattern_num][0] == 'y' and not pattern[pattern_num][1]:
                y -= 1
            answer[x][y] = i 
            i += 1
        if pattern_num == 3:
            pattern_num = 0
        else:
            pattern_num += 1
        n -= 1
    return answer