def solution(progresses, speeds):
    answer = []
    end_days = []
    for idx, i in enumerate(progresses):
        if (100-i) % speeds[idx] != 0:
            end_days.append(int((100-i)/speeds[idx])+1)
        else:
            end_days.append(int((100-i)/speeds[idx]))
    temp_day = 1
    temp_max = end_days[0]
    for i in end_days[1:]:
        if temp_max >= i:
            temp_day += 1
        if temp_max < i:
            answer.append(temp_day)
            temp_max = i
            temp_day = 1
    answer.append(temp_day)
    return answer

print(solution([93, 30, 55], 	[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]))
print(solution([90, 90, 90], [1, 5, 4]))
print(solution([95, 95, 95, 95], [4, 3, 2, 1]))
print(solution([99, 95, 97], [1, 1, 1]))
