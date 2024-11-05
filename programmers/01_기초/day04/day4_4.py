# day4 조건 문자열

def solution(ineq, eq, n, m):
    answer = 0
    if ineq == '>':
        if eq == '=':
            answer = int(bool(n>=m))
        else:
            answer = int(bool(n>m))
    else:
        if eq == '=':
            answer = int(bool(n<=m))
        else:
            answer = int(bool(n<m))
    return answer