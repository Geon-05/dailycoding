# day10 배열 회전시키기

def solution(numbers:list, direction):
    answer = numbers
    if direction == 'right':
        answer.insert(0,numbers[-1])
        answer.pop()
    elif direction == 'left':
        answer.append(numbers[0])
        answer.pop(0)
    return answer