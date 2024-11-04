# day24 그림 확대

def solution(picture, k):
    answer = []
    for pic in picture:
        tmp = ''
        for pic_str in pic:
            for i in range(k):
                tmp += pic_str
        for i in range(k):
            answer.append(tmp)
    return answer