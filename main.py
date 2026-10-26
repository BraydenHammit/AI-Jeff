from math import floor, sqrt

words = {
    'self': ['I','jeff'],
    'verb': ['hate','love','run','eat','murder'],
    'user': ['you'],
    'def': ['the'],
    'noun': ['cheese','cat', 'government'],
    'plur noun': ['cats', 'snakes', 'foxes', 'fish', 'tables'],
    'adjective': ['green','ugly','handsome','pretty','juicy'],
    'punct': ['.','...']
}
nxt = {
    'start': ['self','user','noun'],
    'self': ['verb'],
    'verb': ['plur noun','noun','user'],
    'user': ['punct'],
    'def': '____________',
    'noun': ['punct'],
    'plur noun': ['punct'],
    'adjective': ['noun','plur noun'],
    'punct': ['self','user','noun']
}
inquiry = input('Request: ')

def alphabet(value):
    alph = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    try:
        val = alph[value.lower()]
        return val
    except:
        try:
            val = int(value)
            return val
        except:
            return 1


word_id = ['start','start','start']
answer = ''
loop = 2
for each in range(floor(sqrt(len(inquiry))*7)):
    xqc = word_id[loop]
    if not xqc == 'punct':
        answer += ' '
    t = nxt[word_id[loop]]
    failed = True
    iteration = 0
    while failed:
        iteration += 1
        try:
            tt = t[round(sqrt(loop*len(t)//len(t)+iteration))]
            failed = False
        except: 
            try:
                tt = t[round(iteration//len(t))]
            except: pass
        if iteration > 100:
            tt = t[0]
            failed = False
    if xqc == 'start':
        try:
            answer += words[tt][((len(words[tt])//2)*alphabet(inquiry[loop-2]))-1].title()
        except:
            try:
                answer += words[tt][((len(words[tt])//2)*alphabet(inquiry[loop-2]))-20].title()
            except:
                answer += words[tt][(len(words[tt])//2)-1].title()
    else:
        try:
            answer += words[tt][((len(words[tt])//2)*alphabet(inquiry[loop-2]))-1]
        except:
            try:
                answer += words[tt][((len(words[tt])//2)*alphabet(inquiry[loop-2]))-20]
            except:
                answer += words[tt][(len(words[tt])//2)-1]
    word_id.append(tt)
    loop += 1



print(answer)