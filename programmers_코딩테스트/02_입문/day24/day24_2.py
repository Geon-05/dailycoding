# day24 이진수 더하기

def solution(bin1, bin2):
    answer = ''
    dec1 = 0
    dec2 = 0
    for idx, num in enumerate(bin1[::-1]):
        dec1 +=  int(num) * (2 ** idx)
    for idx, num in enumerate(bin2[::-1]):
        dec2 += int(num) * (2 ** idx)
    total = dec1 + dec2
    tmp_bin = ''
    while total > 0:
        tmp_bin += str(total % 2)
        total = int(total/2)
    tmp_list = [i for i in tmp_bin]
    for i in tmp_list[::-1]:
        answer += i
    if tmp_bin == '':
        answer = '0'
    return answer