# day23 등수 매기기

def solution(score):
    answer = []
    rank_list = []
    for idx, per_score in enumerate(score):
        score[idx].append((per_score[0]+per_score[1])/2)
        rank_list.append((per_score[0]+per_score[1])/2)
        score[idx].append(idx)
    rank = 1
    rank_dict = {}
    for i in sorted(rank_list, reverse=True):
        if i not in rank_dict.keys():
            rank_dict[i] = rank
        else:
            pass
        rank += 1
    for i in score:
        answer.append(rank_dict[i[2]])
    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))