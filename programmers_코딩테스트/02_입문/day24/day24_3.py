# day24 A로 B만들기

def solution(before, after):
    answer = 0
    before_list = [i for i in before]
    after_list = [i for i in after]
    try:
        for i in before_list:
            after_list.remove(i)
        answer = 1
    except:
        pass
    return answer