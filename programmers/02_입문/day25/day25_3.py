# day25 연속된 수의 합

def solution(num, total):
    total_save = total
    total += num
    while total >= 0:
        answer = []
        tmp = 0
        for i in range(total-num+1,total+1):
            answer.append(i)
            tmp += i
        if tmp == total_save:
            break
        total -= 1
    return answer

print(solution(5, 0))