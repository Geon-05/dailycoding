# day18 문자열 잘라서 정렬하기

import pandas as pd

def solution(myString:str):
    answer = []
    myString = myString.strip('x')
    myString = myString.split("x")
    word_length = len(max(myString, key=lambda x : len(x)))
    df = pd.Series(myString)
    tmp = list(df.sort_values())
    for i in tmp:
        if i != "":
            answer.append(i)
    return answer

print(solution("axbxcxdx"))
print(solution("dxccxbbbxaaaa"))