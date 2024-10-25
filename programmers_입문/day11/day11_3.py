# day11 최댓값 만들기1

def solution(numbers:list):
    answer = 0
    num1 = max(numbers)
    numbers.remove(num1)
    num2 = max(numbers)
    answer = num1 * num2
    return answer