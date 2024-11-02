# day21 전국 대회 선발 고사

def solution(rank, attendance):
    answer = 0
    tmp = {}
    tmp_list = []
    for i in range(len(rank)):
        tmp[rank[i]*attendance[i]] = i
    for key in sorted(tmp.keys()):
        if key != 0:
            tmp_list.append(tmp[key])
    answer = tmp_list[0] * 10000 + tmp_list[1] * 100 + tmp_list[2]
    return answer