# day24 치킨 쿠폰

def solution(chicken):
    answer = 0
    tmp = 0
    while chicken > 0:
        tmp += 1
        if tmp == 10:
            answer += 1
            tmp = 0
            continue
        chicken -= 1
    return answer