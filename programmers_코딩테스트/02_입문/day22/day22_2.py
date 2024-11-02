# day22 평행

def solution(dots:list):
    answer = 0
    dots.sort(key=lambda x:x[0])
    case_list = [
        [0,1,2,3],
        [0,2,1,3],
        [0,3,1,2]
    ]
    for a, b, c, d in case_list:
        if ((dots[a][0]-dots[b][0])/(dots[a][1]-dots[b][1])) == ((dots[c][0]-dots[d][0])/(dots[c][1]-dots[d][1])):
            answer = 1
    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))