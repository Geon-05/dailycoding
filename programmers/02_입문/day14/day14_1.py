# day14 가까운 수

def solution(array, n):
    answer = 0
    temp = [i-n for i in array]
    part1 = [101]
    part2 = [101]
    for i in temp:
        if i == 0:
            return n
        elif i > 0:
            part1.append(i)
        elif i < 0:
            part2.append(-i)
    if min(part1) > min(part2):
        answer = n - min(part2)
    elif min(part1) < min(part2):
        answer = n + min(part1)
    else:
        answer = n - min(part2)
    return answer

print(solution([3, 10, 28], 20))
print(solution([1, 4, 2, 1], 3))
print(solution([10, 11, 12], 13))