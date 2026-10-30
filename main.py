from extra_code.run import run
from extra_code.base import base_vars
import tkinter as tk

root = tk.Tk()
root.title('Jeff the AI')
root.geometry('700x420')
root.config(bg='grey40')
blink_state = 'o'
repitition = 1
counter = 0
words, structure = base_vars()

images = {
    'def': tk.PhotoImage(file='images/default.png').subsample(3,3),
    'talk': tk.PhotoImage(file='images/talking.png').subsample(3,3),
    'blk': tk.PhotoImage(file='images/blink.png').subsample(3,3)
}

def r(_=None):
    global teext, answer, counter, ids, wrds, feedbackfrm, upvote, downvote, midvote, vote
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
    answer, ids, wrds = run(entry.get(),words,structure)
    ids.pop(0)
    ids.pop(0)
    ids.pop(0)
    ans.configure(text='')
    teext = ''
    root.after(5,lambda:nextlet(counter))

def feedback(f=False):
    global ids, wrds
    previd = 'start'
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
    vote.configure(text=f'                             Vote: {'Bad' if f == False else 'Good' if f == True else 'Neutral'}                             ',fg=('red' if f == False else 'lime' if f == True else "#ddff00"))
    vote.pack()

def nextlet(c):
    global teext
    if counter == c:
        try:
            teext += answer[len(teext)]
        except IndexError: return
        ans.configure(text=teext)
        if (len(teext) % 20) == 0:
            img.configure(image=images['def'])
        elif (len(teext) % 10) == 0:
            img.configure(image=images['talk'])
        if not (len(teext) == len(answer)):
            root.after(5,lambda:nextlet(c))
        else: img.configure(image=images['def'])
        root.update_idletasks()

def blink():
    global blink_state, repitition
    repitition += 1
    if blink_state == 'o':
        blink_state = 'c'
        img.configure(image=images['blk'])
        root.after(100,blink)
    elif blink_state == 'c':
        blink_state = 'o'
        img.configure(image=images['def'])
        root.after(2800 + ((repitition * 152) % 4000),blink)

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

entry.bind('<Return>',r)
root.after(2800 + ((repitition * 152) % 4000),blink)
root.update_idletasks()
root.mainloop()
