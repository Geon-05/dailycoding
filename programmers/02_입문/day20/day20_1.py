# day20 직사각형 넓이 구하기

def solution(dots):
    answer = 0
    x_list = []
    y_list = []
    for x, y in dots:
        x_list.append(x)
        y_list.append(y)
    x_list = sorted(list(set(x_list)))
    y_list = sorted(list(set(y_list)))
    answer = (x_list[1]-x_list[0])*(y_list[1]-y_list[0])
    return answer