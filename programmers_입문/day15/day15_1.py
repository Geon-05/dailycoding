# day15 영어가 싫어요

def solution(numbers):
    answer = ''
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    while len(numbers) > 0:
        for idx, i in enumerate(num_list):
            if numbers[:2] == i[:2]:
                answer += str(idx)
                temp = list(numbers)
                for j in range(len(i)):
                    temp.pop(0)
                numbers = ''
                for k in temp:
                    numbers += k
    return int(answer)

print(solution("onetwothreefourfivesixseveneightnine"))