from run import run
import tkinter as tk

root = tk.Tk()
root.title('Jeff the AI')
root.geometry('400x300')

def r():
    global teext, answer
    answer = run(entry,ans)
    ans.configure(text='')
    teext = ''
    root.after(5,nextlet)

def nextlet():
    global teext
    teext += answer[len(teext)]
    ans.configure(text=teext)
    if not (len(teext) == len(answer)):
        root.after(5,nextlet)

txt = tk.Label(root,text='Request:',fg='magenta')
txt.pack(pady=5)
frm = tk.Frame(root)
entry = tk.Entry(frm)
ok = tk.Button(frm,text='Ok',command=r)
frm.pack()
entry.pack(side=tk.LEFT)
ok.pack(side=tk.RIGHT)
ans = tk.Label(root,text='Jeff answers here!',fg='yellow',wraplength=350,justify="left",anchor="w")
ans.pack(pady=10)

root.update_idletasks()
root.mainloop()