from math import floor, sqrt
import platform as plt
import os

if plt.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')
    print('\n\n')

words = {
    'self': ['I'],
    'people': ['Jeff','Obama','Trump','Heisenberg','Rick','Morty','Harry Potter'],
    'verb': ['hate','love','eat','murder','own','ignore','sell'],
    'verbS': ['hates','loves','eats','murders','owns','ignores','admires','built','cooks','sells'],
    'am': ['am'],
    'are': ['are'],
    'is': ['is'],
    'are': ['are'],
    'userS': ['you'],
    'bc': ['because'],
    'a': ['a'],
    'user': ['you'],
    'noun': ['cheese','basketball','football','China','McDonalds','Breaking Bad'],
    'noun is': ['cheese','basketball','football','China','McDonalds','Breaking Bad'],
    'the noun': ['the cat','the government','the cheeseburger','the law'],
    'the noun is': ['the cat','the government','the cheeseburger','the law'],
    'plur noun': ['cats', 'snakes', 'foxes', 'fish', 'tables', 'people', 'citizens','ideas','laws'],
    'plur noun are': ['cats', 'snakes', 'foxes', 'fish', 'tables', 'people', 'citizens','ideas','laws'],
    'adjective': ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low'],
    'adjectiveQ': ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low'],
    'AMadjective': ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low'],
    'punct': ['.','...','!','?']
}
nxt = {
    'start': ['self','people','userS','noun is','plur noun are','the noun is'],
    'self': ['verb','am'],
    'people': ['verbS','is'],
    'am': ['AMadjective','noun','a','the noun'],
    'is': ['adjective','noun','a','the noun'],
    'verb': ['plur noun','noun','adjective','the noun'],
    'verbS': ['plur noun','user','the noun'],
    'user': ['punct'],
    'userS': ['punct','are'],
    'are': ['adjective','noun','a'],
    'noun': ['punct'],
    'the noun': ['punct'],
    'noun is': ['is'],
    'the noun is': ['is'],
    'plur noun are': ['are'],
    'plur noun': ['punct'],
    'adjective': ['plur noun'],
    'AMadjective': ['punct'],
    'adjectiveQ': ['noun'],
    'punct': ['self','people','userS','noun is','plur noun are','the noun is'],
    'a': ['adjectiveQ']
}
inquiry = input('\033[35mRequest: \033[0m')
print()

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

def iterate(num):
    global nxt, words
    for each in range(num):
        for key in nxt:
            nxt[key] = nxt[key][1:] + nxt[key][:1]
        for key in words:
            words[key] = words[key][1:] + words[key][:1]


word_id = ['start','start','start']
answer = ''
loop = 2
for each in range(floor(sqrt(len(inquiry))*37)):
    xqc = word_id[loop]
    t = nxt[word_id[loop]]
    failed = True
    iteration = loop // 2
    tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 5) % len(t)]
    char = inquiry[(loop - 2) % len(inquiry)]
    choices = words[tt]
    word = choices[(alphabet(char) - 1) % len(choices)]
    if xqc == 'a' and word[0].lower() in ('i','o','u','a','e'):
        answer += 'n'
    if not tt == 'punct':
        answer += ' '
    if xqc in ('start','punct'):
        answer += word[0].upper() + word[1:] 
    else:
        answer += word
    word_id.append(tt)
    loop += 1
    iterate((round(loop % 5 // len(inquiry)))+1)

if word_id[loop] == 'punct': finished = True
else: finished = False
while finished == False:
    xqc = word_id[loop]
    t = nxt[word_id[loop]]
    failed = True
    iteration = loop // 2
    tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 5) % len(t)]
    char = inquiry[(loop - 2) % len(inquiry)]
    choices = words[tt]
    word = choices[(alphabet(char) - 1) % len(choices)]
    if xqc == 'a' and word[0].lower() in ('i','o','u','a','e'):
        answer += 'n'
    if not tt == 'punct':
        answer += ' '
    if xqc in ('start','punct'):
        answer += word[0].upper() + word[1:]
    else:
        answer += word
    word_id.append(tt)
    loop += 1
    iterate((round(loop % 5 // len(inquiry)))+1)

    if tt == 'punct': finished = True

print('\033[33m'+answer+'\n\033[0m')