from math import sqrt, floor
from extra_code.alph import alphabet

def run(inquiry,words,nxt):
    if inquiry == '': inquiry = ' ' 

    def iterate(num):
        for _ in range(num):
            for key in nxt:
                nxt[key] = nxt[key][1:] + nxt[key][:1]
            for key in words:
                words[key] = words[key][1:] + words[key][:1]

    added = 1
    for let in inquiry:
        added += alphabet(let)
    iterate(added)
    word_id = ['start','start','start']
    wrds = []
    answer = ''
    loop = 2
    for each in range(floor(sqrt(len(inquiry))*13)):
        xqc = word_id[loop]
        t = nxt[word_id[loop]]
        iteration = loop // 2
        tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 7) % len(t)]
        char = inquiry[(loop - 2) % len(inquiry)]
        choices = words[tt]
        if inquiry[(loop + iteration) % len(inquiry)].lower() == inquiry[(loop + iteration) % len(inquiry)]:
            word = choices[(alphabet(char) - 1) % len(choices)]
        else:
            word = choices[(alphabet(char) + 1) % len(choices)]
        if xqc == 'a' and ((word[0].lower() in ('i','o','u','a','e')) or (word == 'honest')):
            answer += 'n'
        if tt not in ('punct','com'):
            answer += ' '
        if xqc in ('start','punct'):
            answer += word[0].upper() + word[1:] 
        else:
            answer += word
        wrds.append(word)
        word_id.append(tt)
        loop += 1
        iterate(loop-1)

    extloop = 0
    if word_id[loop] == 'punct': finished = True
    else: finished = False
    while finished == False:
        xqc = word_id[loop]
        t = nxt[word_id[loop]]
        if ('com' in t) and extloop > 99:
            t = ['punct']
        iteration = loop // 2
        tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 5) % len(t)]
        char = inquiry[(loop - 2) % len(inquiry)]
        choices = words[tt]
        if inquiry[(loop + iteration) % len(inquiry)].lower() == inquiry[(loop + iteration) % len(inquiry)]:
            word = choices[(alphabet(char) - 1) % len(choices)]
        else:
            word = choices[(alphabet(char) + 1) % len(choices)]
        if xqc == 'a' and ((word[0].lower() in ('i','o','u','a','e')) or (word == 'honest')):
            answer += 'n'
        if tt not in ('punct','com'):
            answer += ' '
        if xqc in ('start','punct'):
            answer += word[0].upper() + word[1:]
        else:
            answer += word
        wrds.append(word)
        word_id.append(tt)
        loop += 1
        extloop += 1
        iterate(loop-1)

        if tt == 'punct': finished = True

    return answer, word_id, wrds
