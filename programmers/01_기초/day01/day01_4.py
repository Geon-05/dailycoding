# day1 대소문자 바꿔서 출력하기

str = input()
answer = ''
for char_base in str:
    if char_base.islower():
        answer += char_base.upper()
    else:
        answer += char_base.lower()
print(answer)