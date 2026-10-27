from math import floor, sqrt
import tkinter as tk

def run():
    inquiry = entry.get()

    adjectives = ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low','slippery','rough','vibrant','large','massive','disgusting','vile']
    nouns = ['cheese','basketball','football','China','McDonalds','Breaking Bad']
    the_nouns = ['the cat','the government','the cheeseburger','the law']
    plur_nouns = ['cats', 'snakes', 'foxes', 'fish', 'tables', 'people', 'citizens','ideas','laws']

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
        'noun': nouns,
        'noun is': nouns,
        'the noun': the_nouns,
        'the noun is': the_nouns,
        'plur noun': plur_nouns,
        'plur noun are': plur_nouns,
        'adjective': adjectives,
        'adjectiveQ': adjectives,
        'AMadjective': adjectives,
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

    ans.configure(text=answer)


root = tk.Tk()
root.title('Jeff the AI')
root.geometry('400x300')

txt = tk.Label(root,text='Request:',fg='magenta')
txt.pack(pady=5)
frm = tk.Frame(root)
entry = tk.Entry(frm)
ok = tk.Button(frm,text='Ok',command=run)
frm.pack()
entry.pack(side=tk.LEFT)
ok.pack(side=tk.RIGHT)
ans = tk.Label(root,text='Jeff answers here!',fg='yellow',wraplength=350,justify="left",anchor="w")
ans.pack(pady=10)

root.update_idletasks()
root.mainloop()