def seat_chk(park_map, start_x, start_y, length):
    answer = None
    count_m = length ** 2
    count_tmp = 0
    if start_y + length < len(park_map) + 1:
        for y in range(length):
            if start_x + length < len(park_map[0]) + 1:
                for x in range(length):
                    if park_map[start_y + y][start_x + x] == "-1":
                        count_tmp += 1
                    else:
                        answer = False
                        return answer
    if count_m == count_tmp:
        answer = True
    else:
        answer = False
    return answer

def solution(mats, park):
    answer = -1
    pass_size = []
    for seat_size in mats:
        chk = None
        for y in range(len(park)):
            for x in range(len(park[0])):
                chk = seat_chk(park, x, y, seat_size)
                if chk:
                    pass_size.append(seat_size)
    if pass_size == []:
        answer = -1
    else:
        answer = max(pass_size)
    return answer
# mats = [3,2]
# park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

# print(solution(mats, park))


mats = [3]
park = [["-1", "-1", "-1", "-1"], ["-1", "-1", "-1", "-1"], ["A", "-1", "-1", "-1"]]

print(solution(mats, park))