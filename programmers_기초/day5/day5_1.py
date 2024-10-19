# day5 코드 처리하기

def solution(code):
    mode = False
    answer = ''
    for i, ret in enumerate(list(code)):
        if ret == '1':
            mode = not(mode)
            continue
        
        if not(mode) and i % 2 == 0:
            answer += ret
            
        if mode and i % 2 == 1:
            answer += ret
    
    if answer == '':
        answer = 'EMPTY'
    
    return answer

res = solution('abc1abc1abc')
print(res)