from run import run
import tkinter as tk

root = tk.Tk()
root.title('Jeff the AI')
root.geometry('400x300')
root.config(bg='grey40')

def r():
    global teext, answer
    answer = run(entry)
    ans.configure(text='')
    teext = ''
    root.after(5,nextlet)

def nextlet():
    global teext
    teext += answer[len(teext)]
    ans.configure(text=teext)
    if not (len(teext) == len(answer)):
        root.after(5,nextlet)

txt = tk.Label(root,text='Request:',fg='magenta',highlightbackground='grey40',bg='grey40')
txt.pack(pady=5)
frm = tk.Frame(root,highlightbackground='grey40',bg='grey40')
entry = tk.Entry(frm,highlightbackground='grey40',bg='grey40')
ok = tk.Button(frm,text='Ok',command=r,highlightbackground='grey40',bg='grey60')
frm.pack()
entry.pack(side=tk.LEFT,padx=5)
ok.pack(side=tk.RIGHT)
ans = tk.Label(root,text='Jeff answers here!',fg='yellow',wraplength=350,justify="left",anchor="w",highlightbackground='grey40',bg='grey40')
ans.pack(pady=10)

root.update_idletasks()
root.mainloop()