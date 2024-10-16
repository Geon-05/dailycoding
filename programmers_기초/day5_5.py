# day5 이어 붙인 수

def solution(num_list):
    answer = 0
    even_res = ''
    odd_res = ''
    for i in num_list:
        if i % 2 == 0:
            even_res += str(i)
        else:
            odd_res += str(i)
    answer = int(even_res) + int(odd_res)
    return answer