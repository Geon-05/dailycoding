# day23 날짜 비교하기

def solution(date1, date2):
    answer = 0
    for i in range(3):
        if date1[i] < date2[i]:
            answer = 1
            break
        if date1[i] > date2[i]:
            answer = 0
            break
    return answer

print(solution([2022, 1, 1], [2021, 12, 31 ]))