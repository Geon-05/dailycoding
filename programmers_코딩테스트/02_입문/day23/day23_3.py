# day23 옹알이1

def solution(babbling):
    answer = 0
    word_list = ['aya', 'ye', 'woo', 'ma']
    for chk_word in babbling:
        for word in word_list:
            if word in chk_word:
                tmp_word = ''
                chk_word = chk_word.split(word)
                for i in chk_word:
                    tmp_word += '/'+i
                chk_word = tmp_word
        chk_word = chk_word.replace('/','')
        if chk_word == '':
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))