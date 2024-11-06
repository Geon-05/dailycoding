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


park_map = [["-1", "-1", "-1", "-1"], ["-1", "-1", "-1", "-1"], ["A", "-1", "-1", "-1"]]

print(seat_chk(park_map, 0, 0, 2))