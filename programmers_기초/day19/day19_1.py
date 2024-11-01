# day19 세 개의 구분자

def solution(myStr:str):
    answer = []
    myList = myStr.replace('b','a').replace('c','a').split('a')
    for i in myList:
        if i != '':
            answer.append(i)
    if answer == []:
        answer.append('EMPTY')
    return answer