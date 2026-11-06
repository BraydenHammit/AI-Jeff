from extra_code.run import run
from extra_code.base import base_vars
import tkinter as tk
from tkinter import scrolledtext
import json
import os

dirr = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(dirr,'data/'), exist_ok=True)

def save(b=False):
    with open("data/words.json", "w") as file:
        json.dump(words, file, indent=4)
    with open("data/structure.json", "w") as file:
        json.dump(structure, file, indent=4)
    with open("data/logs.json", "w") as file:
        json.dump(logs, file, indent=4)
    if b:
        b.configure(text='Saved!')
        root.after(1000,lambda:setbackbutton(b,'s'))

def clear(b=False):
    global logs, words, structure
    with open('data/structure.json', "w") as f:
        json.dump({}, f, indent=4)
    with open('data/words.json', "w") as f:
        json.dump({}, f, indent=4)
    with open('data/logs.json', "w") as f:
        json.dump([], f, indent=4)
    logs = []
    words, structure = base_vars()
    if b:
        b.configure(text='Data has been cleared.')
        root.after(1500,lambda:setbackbutton(b,'c'))

def setbackbutton(b,type):
    if type == 's':
        b.configure(text='Save')
    elif type == 'c':
        b.configure(text='Clear')

if not os.path.exists(os.path.join(dirr, 'data/')):
    with open('data/structure.json', "w") as f:
        json.dump({}, f, indent=4)
    with open('data/words.json', "w") as f:
        json.dump({}, f, indent=4)
    with open('data/logs.json', "w") as f:
        json.dump([], f, indent=4)

if not os.path.exists(os.path.join(dirr, 'data/structure.json')):
    with open('data/structure.json', "w") as f:
        json.dump({}, f, indent=4)
if not os.path.exists(os.path.join(dirr, 'data/words.json')):
    with open('data/words.json', "w") as f:
        json.dump({}, f, indent=4)
if not os.path.exists(os.path.join(dirr, 'data/logs.json')):
    with open('data/logs.json', "w") as f:
        json.dump([], f, indent=4)

root = tk.Tk()
root.title('Jeff the AI')
root.geometry('700x440')
root.config(bg='grey40')
blink_state = 'o'
repitition = 1
counter = 0
if (os.path.getsize('data/words.json') > 5) and (os.path.getsize('data/structure.json') > 5) and (os.path.getsize('data/logs.json') > 5):
    words = json.load(open('data/words.json'))
    structure = json.load(open('data/structure.json'))
    logs = json.load(open('data/logs.json'))
    ext, extt = base_vars()
    voted = False
    for key1, key2 in zip(ext, extt):
        for val1, val2 in zip(ext[key1], extt[key2]):
            if not (val1 in words[key1]):
                words[key1].append(val1)
            if not (val2 in structure[key2]):
                structure[key2].append(val2)
else:
    words, structure = base_vars()
    logs = []
    voted = 'xqc'

images = {
    'def': tk.PhotoImage(file='images/default.png').subsample(3,3),
    'talk': tk.PhotoImage(file='images/talking.png').subsample(3,3),
    'blk': tk.PhotoImage(file='images/blink.png').subsample(3,3),
    'r': tk.PhotoImage(file='images/right.png').subsample(3,3),
    'l': tk.PhotoImage(file='images/left.png').subsample(3,3),
}

def r(_=None):
    global teext, answer, counter, ids, wrds, feedbackfrm, upvote, downvote, midvote, vote, voted
    if counter == 0:
        feedbackfrm = tk.Frame(root,highlightbackground='grey40',bg='grey40')
        upvote = tk.Button(feedbackfrm,text='Good',command=lambda:feedback(f=True),fg='green',highlightbackground='grey40',bg='grey60')
        midvote = tk.Button(feedbackfrm,text='Mid',command=lambda:feedback(None),highlightbackground='grey40',bg='grey60',fg="#e5e21a")
        downvote = tk.Button(feedbackfrm,text='Bad',command=lambda:feedback(f=False),highlightbackground='grey40',bg='grey60',fg="red")
        vote = tk.Label(feedbackfrm,highlightbackground='grey40',bg='grey40',text='Vote: N/A')
        feedbackfrm.place(x=360,y=350)
        upvote.pack(side=tk.LEFT,padx=20)
        midvote.pack(side=tk.LEFT,padx=20)
        downvote.pack(side=tk.LEFT,padx=20)
    else:
        upvote.pack(side=tk.LEFT,padx=20)
        midvote.pack(side=tk.LEFT,padx=20)
        downvote.pack(side=tk.LEFT,padx=20)
        try:vote.pack_forget()
        except:None
    counter += 1
    _ = onesent.get()
    if not voted:
        logs.append('[Rating: None]')
    logs.append(f'User: {entry.get()}')
    if _ == True:
        answer, ids, wrds = run(entry.get(),words,structure,onesent=True)
        logs.append('[Single Sentence Mode - On]')
    else:
        answer, ids, wrds = run(entry.get(),words,structure)
        logs.append('[Single Sentence Mode - Off]')
    logs.append(f'Jeff: {answer}')
    ids.pop(0)
    ids.pop(0)
    ids.pop(0)
    ans.configure(text='')
    teext = ''
    voted = False
    save()
    root.after(5,lambda:nextlet(counter))

def feedback(f=False):
    global ids, wrds, voted
    previd = 'start'
    voted = True
    vott = 'Bad' if f == False else 'Good' if f == True else 'Neutral'
    logs.append(f'[Rating: {vott}]')
    if f == True:
        for id, word in zip(ids, wrds):
            for _ in range(5):
                words[id].append(word)
                structure[previd].append(id)
            previd = id
    elif f == False:
        for id, word in zip(ids, wrds):
            for _ in range(2):
                if word in words[id]:
                    words[id].pop(words[id].index(word))
                if not (word in words[id]):
                    words[id].append(word)
            if id in structure[previd]:
                structure[previd].pop(structure[previd].index(id))
            if not (id in structure[previd]):
                structure[previd].append(id)
            previd = id
    upvote.pack_forget()
    midvote.pack_forget()
    downvote.pack_forget()
    save()
    vote.configure(text=f"                             Vote: {vott}                             ",fg=('red' if f == False else 'lime' if f == True else "#ddff00"))
    vote.pack()

def nextlet(c):
    global teext
    if counter == c:
        try:
            teext += answer[len(teext)]
        except IndexError: return
        ans.configure(text=teext)
        if (len(teext) % 10) == 0:
            img.configure(image=images['def'])
        elif (len(teext) % 5) == 0:
            img.configure(image=images['talk'])
        if not (len(teext) == len(answer)):
            root.after(10,lambda:nextlet(c))
        else: img.configure(image=images['def'])
        root.update_idletasks()

def blink():
    global blink_state, repitition
    if blink_state == 'o':
        if frame % 7 == 0:
            if frame % 2 == 0:
                blink_state = 'r'
                img.configure(image=images['r'])
                root.after(2000 + ((repitition * 75) % 3000),blink)
            else:
                blink_state = 'l'
                img.configure(image=images['l'])
                root.after(2000 + ((repitition * 75) % 3000),blink)
        else:
            blink_state = 'c'
            img.configure(image=images['blk'])
            root.after(50 + ((repitition * 2) % 300),blink)
    elif blink_state == 'c' or blink_state == 'l' or blink_state == 'r':
        repitition += 1
        blink_state = 'o'
        img.configure(image=images['def'])
        root.after(2800 + ((repitition * 152) % 4000),blink)

def loggg():
    global logext
    if logs == []:
        texxxt = '[No logs available.]'
    else:
        texxxt = ''
        for line in logs:
            texxxt += line+'\n\n'
    logext = tk.Toplevel(root)
    logext.config(bg='grey20')
    log = scrolledtext.ScrolledText(logext, wrap=tk.WORD, width=50, height=10, highlightthickness=2, highlightbackground="black", relief="flat")
    log.insert(tk.INSERT, texxxt)
    log.pack(pady=30,padx=30)
    log.configure(state='disabled')
    info.configure(text='X',command=logext.destroy)

def savewindow():
    global wind
    wind = tk.Toplevel(root)
    wind.config(bg='grey20')
    s = tk.Button(wind,text='Save',command=lambda:save(b=s),fg='black',activeforeground='black',bg='grey40',highlightbackground='grey60',bd=0)
    c = tk.Button(wind,text='Clear',command=lambda:clear(b=c),fg='black',activeforeground='black',bg='grey40',highlightbackground='grey60',bd=0)
    w = tk.Label(wind,text='WARNING:\nClearing save data will delete all saved information.\nCleared data may not be recoverable.',fg='black',highlightbackground='grey20',bg='grey20')
    s.pack(pady=10)
    c.pack(pady=10)
    w.pack(pady=10)
    saveB.configure(text='X',command=wind.destroy)

onesent = tk.BooleanVar()
check = tk.Checkbutton(root,text="Single Sentence Mode",variable=onesent,highlightbackground='grey40',bg='grey40',activebackground='grey40')
check.place(x=10,y=410)
info = tk.Button(root,command=loggg,fg='black',highlightbackground='grey40',bg='grey60')
try: info.configure(text='ⓘ')
except: info.configure(text='i')
info.place(x=640,y=410)
saveB = tk.Button(root,command=savewindow,text='Save',fg='black',highlightbackground='grey40',bg='grey60')
saveB.place(x=570,y=410)
img = tk.Label(root,image=images['def'],highlightbackground='grey40',bg='grey40')
img.place(x=10,y=10)
overfrm = tk.Frame(root,highlightbackground='grey40',bg='grey40',width=360)
overfrm.place(x=330,y=10)
txt = tk.Label(overfrm,text='                                           Request:                                           ',fg="#800b4d",highlightbackground='grey40',bg='grey40')
txt.pack(pady=5)
frm = tk.Frame(overfrm,highlightbackground='grey40',bg='grey40')
entry = tk.Entry(frm,highlightbackground='grey40',bg='grey30')
ok = tk.Button(frm,text='Ok',command=r,highlightbackground='grey40',bg='grey60')
frm.pack()
entry.pack(side=tk.LEFT,padx=5)
ok.pack(side=tk.RIGHT)
ans = tk.Label(overfrm,text='Jeff answers here!',fg="#b6b118",wraplength=350,justify="left",anchor="w",highlightbackground='grey40',bg='grey40')
ans.pack(pady=10)

frame = 0
def frame_upd():
    global frame
    frame += 1
    root.after(10,frame_upd)
    if frame % 10 == 0:
        try:
            if not logext.winfo_exists():
                try: info.configure(text='ⓘ')
                except: info.configure(text='i')
                info.configure(command=loggg)
        except NameError: None
        try:
            if not wind.winfo_exists():
                saveB.configure(command=savewindow,text='Save')
        except NameError: None
root.after(10,frame_upd)

entry.bind('<Return>',r)
root.after(2800 + ((repitition * 152) % 4000),blink)
root.update_idletasks()
root.mainloop()

save()