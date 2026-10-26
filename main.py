from math import floor, sqrt

words = {
    'self': ['me','I','jeff'],
    'verb': ['hate','love','run','eat','murder'],
    'user': ['you'],
    'def': ['the'],
    'noun': ['cheese','cat', 'government'],
    'plur noun': ['cats', 'snakes', 'foxes', 'fish', 'tables'],
    'adjective': ['green','ugly','handsome','pretty','juicy'],
    'punct': ['.']
}
nxt = {
    'start': ['self','user','noun'],
    'self': ['verb'],
    'verb': ['plur noun','noun','user'],
    'user': 'punct',
    'def': '____________',
    'noun': ['punct'],
    'plur noun': ['punct'],
    'adjective': ['noun','plur noun'],
    'punct': ['self','user','noun']
}
inquiry = input('Request: ')


word_id = ['start']
answer = ''
loop = 0
for each in range(floor(sqrt(len(inquiry)))):
    t = nxt[word_id[loop-1]]
    failed = True
    iteration = 0
    while failed:
        iteration += 1
        try:
            tt = t[round(sqrt(len(inquiry)//len(t)+iteration))]
            failed = False
        except IndexError: 
            try:
                tt = t[round(iteration//len(t))]
            except IndexError: pass
        if iteration > 100:
            tt = t[0]
            failed = False
    if t == ['start']:
        answer += words[tt][(len(words[tt])//2)-1].title()
    else:
        answer += words[tt][(len(words[tt])//2)-1]
    answer += ' '
    word_id.append(tt)
    loop += 1



print(answer)