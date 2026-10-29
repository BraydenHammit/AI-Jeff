from run import run
import tkinter as tk

root = tk.Tk()
root.title('Jeff the AI')
root.geometry('700x420')
root.config(bg='grey40')
blink_state = 'o'
repitition = 1
counter = 0

images = {
    'def': tk.PhotoImage(file='images/default.png').subsample(3,3),
    'talk': tk.PhotoImage(file='images/talking.png').subsample(3,3),
    'blk': tk.PhotoImage(file='images/blink.png').subsample(3,3)
}

def r(_=None):
    global teext, answer, counter
    counter += 1
    answer = run(entry)
    ans.configure(text='')
    teext = ''
    root.after(5,lambda:nextlet(counter)

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
            root.after(5,lambda:nextlet(c)
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
