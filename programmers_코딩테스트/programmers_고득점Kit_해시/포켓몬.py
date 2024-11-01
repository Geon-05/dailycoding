def solution(nums):
    answer = 0
    kind = len(set(nums))
    num = len(nums)/2
    answer = min(kind, num)
    return answer