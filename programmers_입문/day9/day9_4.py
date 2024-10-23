# day9 구슬을 나누는 경우의 수

def solution(balls, share):
    answer = 0
    balls_temp = 1
    share_temp = 1
    miner_temp = 1
    for i in range(1,balls+1):
        balls_temp *= i
    for i in range(1,share+1):
        share_temp *= i
    for i in range(1, balls - share + 1):
        miner_temp *= i
    answer = balls_temp / (share_temp * miner_temp)
    return answer