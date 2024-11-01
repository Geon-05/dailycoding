def solution(participant, completion):
    answer = ''
    participant_dict = {}
    for i in participant:
        try:
            participant_dict[i] += 1
        except:
            participant_dict[i] = 1
            
    completion_dict = {}
    for i in completion:
        try:
            completion_dict[i] += 1
        except:
            completion_dict[i] = 1
    
    
    for i in completion_dict.keys():
        participant_dict[i] -= completion_dict[i]
        if participant_dict[i] == 0:
            del participant_dict[i]
    answer = participant_dict.popitem()[0]
    return answer