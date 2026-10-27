from math import floor, sqrt

words = {
    'self': ['I'],
    'self3rd': ['Jeff'],
    'verb': ['hate','love','eat','murder'],
    'verbS': ['hates','loves','eats','murders','owns'],
    'am': ['am'],
    'are': ['are'],
    'is': ['is'],
    'are': ['are'],
    'userS': ['you'],
    'a': ['a(n)'],
    'user': ['you'],
    'noun': ['cheese','the cat','the government','basketball','football','China','the cheeseburger','McDonalds'],
    'plur noun': ['cats', 'snakes', 'foxes', 'fish', 'tables', 'people', 'citizens'],
    'adjective': ['green','ugly','handsome','pretty','juicy','sentient'],
    'adjectiveQ': ['green','ugly','handsome','pretty','juicy','sentient'],
    'punct': ['.','...','!','?']
}
nxt = {
    'start': ['self','self3rd','userS','noun'],
    'self': ['verb','am'],
    'self3rd': ['verbS','is'],
    'am': ['adjective','noun','a'],
    'is': ['adjective','noun','a'],
    'verb': ['plur noun','noun','adjective'],
    'verbS': ['plur noun','user'],
    'user': ['punct'],
    'userS': ['punct','are'],
    'are': ['adjective','noun','a'],
    'noun': ['punct'],
    'plur noun': ['punct'],
    'adjective': ['plur noun'],
    'adjectiveQ': ['noun'],
    'punct': ['self','user','noun','self3rd'],
    'a': ['adjectiveQ']
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
    t = nxt[word_id[loop]]
    failed = True
    iteration = 0
    tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 5) % len(t)]
    if not tt == 'punct':
        answer += ' '
    char = inquiry[(loop - 2) % len(inquiry)]
    choices = words[tt]
    word = choices[(alphabet(char) - 1) % len(choices)]
    if xqc in ('start','punct'):
        answer += word.capitalize() 
    else:
        answer += word
    word_id.append(tt)
    loop += 1

if word_id[loop] == 'punct': finished = True
else: finished = False
while finished == False:
    xqc = word_id[loop]
    t = nxt[word_id[loop]]
    failed = True
    iteration = 0
    tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 5) % len(t)]
    if not tt == 'punct':
        answer += ' '
    char = inquiry[(loop - 2) % len(inquiry)]
    choices = words[tt]
    word = choices[(alphabet(char) - 1) % len(choices)]
    if xqc in ('start','punct'):
        answer += word.capitalize() 
    else:
        answer += word
    word_id.append(tt)
    loop += 1

    if tt == 'punct': finished = True

print(answer)