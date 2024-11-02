# day20 다항식 더하기

def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(' ')
    x_list = []
    num_list = []
    for i in polynomial[::2]:
        if 'x' in i:
            x_list.append(i)
        else:
            num_list.append(i)
    x_val = 0
    num_val = 0
    for x_v in x_list:
        if x_v == 'x':
            x_val += 1
        else:
            x_v = x_v.replace('x','')
            x_val += int(x_v)
    for n_v in num_list:
        num_val += int(n_v)
    if x_val == 1:
        x_val = 'x'
    elif x_val > 1:
        x_val = f'{x_val}x'
    if x_val != 0 and num_val != 0:
        answer = f'{x_val} + {num_val}'
    elif x_val == 0:
        answer = f'{num_val}'
    elif num_val == 0:
        answer = f'{x_val}'
    else:
        answer = 0
    return answer