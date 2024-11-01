# day20 최댓값 만들기2

def solution(numbers):
    answer = 0
    num1 = 0
    num2 = 0
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    m_list = [m for m in numbers if m < 0]
    if len(m_list) > 1:
        m_list = sorted(m_list)
        num1 = m_list[0] * m_list[1]
    numbers = sorted(numbers)
    num2 = numbers[-1] * numbers[-2]
    answer = max([num1, num2])
    print(answer)
    return answer