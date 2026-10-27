from run import run
import tkinter as tk

root = tk.Tk()
root.title('Jeff the AI')
root.geometry('400x300')

txt = tk.Label(root,text='Request:',fg='magenta')
txt.pack(pady=5)
frm = tk.Frame(root)
entry = tk.Entry(frm)
ok = tk.Button(frm,text='Ok',command=lambda:run(entry,ans))
frm.pack()
entry.pack(side=tk.LEFT)
ok.pack(side=tk.RIGHT)
ans = tk.Label(root,text='Jeff answers here!',fg='yellow',wraplength=350,justify="left",anchor="w")
ans.pack(pady=10)

root.update_idletasks()
root.mainloop()