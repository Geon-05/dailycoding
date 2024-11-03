# day23 로그인 성공?

def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            answer = 'login'
            break
        elif id_pw[0] == i[0] and id_pw[1] != i[1]:
            answer = 'wrong pw'
            break
        answer = 'fail'
    return answer