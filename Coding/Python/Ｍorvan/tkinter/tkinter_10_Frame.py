import tkinter as tk
#選單


window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('200x200')

tk.Label(window, text='On the Window', bg='yellow').pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm,)
frm_r = tk.Frame(frm,)
frm_l.pack(side='left')
frm_r.pack(side='right')



tk.Label(frm_l, text='On the frm_l1', bg='red').pack()
tk.Label(frm_l, text='On the frm_l2', bg='green').pack()
tk.Label(frm_r, text='On the frm_r1', bg='blue').pack()
#tk.Label(frm_r, text='On the frm_r2', bg='pink').pack()
#觀察差別

window.mainloop()
