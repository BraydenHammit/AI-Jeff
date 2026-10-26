from math import floor, sqrt

words = {
    'self': ['me','I'],
    'verb': ['hate','love','run','eat','murder'],
    'user': ['you'],
    'def': ['the'],
    'noun': ['cheese','cat', 'government'],
    'plur noun': ['cats', 'snakes', 'foxes', 'fish', 'tables'],
    'adjective': ['green','ugly','handsome','pretty','juicy'],
    'punct': ['.']
}
nxt = {
    'self': 'verb',
    'verb': 'plur noun',
    'user': 'punct',
    'def': '____________',
    'noun': 'punct',
    'plur noun': 'punct',
    'adjective': 'noun',
    'punct': '___________'
}
inquiry = input('Request: ')


word_id = []
answer = ''
loop = 0
for each in range(floor(sqrt(len(inquiry)))):
    t = nxt[word_id[loop-1]]
    answer += words[t][(len(words[t])//2)-1]
    word_id.append(t)
    loop += 1