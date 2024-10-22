# day8 주사위 게임3

def solution(a, b, c, d):
    answer = 0
    dice_dict = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0
    }
    dice_dict.items()
    dice_dict[a] += 1
    dice_dict[b] += 1
    dice_dict[c] += 1
    dice_dict[d] += 1
    play_dict = {
        1:[],
        2:[],
        3:[],
        4:[]
    }
    for a, b in dice_dict.items():
        if b == 4:
            play_dict[4].append(a)
        elif b == 3:
            play_dict[3].append(a)
        elif b == 2:
            play_dict[2].append(a)
        elif b == 1:
            play_dict[1].append(a)
    if len(play_dict[4]) == 1:
        answer = case1(play_dict[4][0])
    elif len(play_dict[3]) == 1:
        answer = case2(play_dict[3][0], play_dict[1][0])
    elif len(play_dict[2]) == 2:
        answer = case3(play_dict[2][1], play_dict[2][0])
    elif len(play_dict[2]) == 1:
        answer = case4(play_dict[1][1], play_dict[1][0])
    elif len(play_dict[1]) == 4:
        answer = play_dict[1][0]
    
    return answer

def case1(a):
    return 1111 * a
def case2(a, b):
    return (10 * a + b) ** 2
def case3(a, b):
    return (a + b) * (a - b)
def case4(a, b):
    return a * b