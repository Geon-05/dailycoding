# day15 원하는 문자열 찾기

def solution(myString:str, pat:str):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    for i in range(len(myString)):
        try:
            if myString[i:i+len(pat)] == pat:
                answer = 1
        except:
            pass
    return answer