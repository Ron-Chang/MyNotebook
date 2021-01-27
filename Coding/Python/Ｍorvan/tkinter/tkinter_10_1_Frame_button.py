import tkinter as tk
#選單


window = tk.Tk()
window.title('Tkinter by Ron')
window.geometry('350x400')


var1 = tk.StringVar()


l = tk.Label(window, text='On the Window', bg='yellow', width=100, height=3)
l.pack()

def input_num():
    l.config(get())

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm,)
frm_r = tk.Frame(frm,)
frm_l.pack(side='left')
frm_r.pack(side='right')


b9 = tk.Button(window, text='9', width=4, height=2,
    command=input_num)
b9.place(x=80, y=0 , anchor='nw')

b8 = tk.Button(window, text='8', width=4, height=2, font=30,
    command=input_num)
b8.place(x=40, y=0 , anchor='nw')

b7 = tk.Button(window, text='7', width=4, height=2,
    command=input_num)
b7.place(x=0, y=0 , anchor='nw')


b6 = tk.Button(window, text='6', width=4, height=2,
    command=input_num)
b6.place(x=80, y=36 , anchor='nw')

b5 = tk.Button(window, text='5', width=4, height=2, font=30,
    command=input_num)
b5.place(x=40, y=36 , anchor='nw')

b4 = tk.Button(window, text='4', width=4, height=2,
    command=input_num)
b4.place(x=0, y=36 , anchor='nw')


b3 = tk.Button(window, text='3', width=4, height=2,
    command=input_num)
b3.place(x=80, y=72 , anchor='nw')

b2 = tk.Button(window, text='2', width=4, height=2, font=30,
    command=input_num)
b2.place(x=40, y=72 , anchor='nw')

b1 = tk.Button(window, text='1', width=4, height=2,
    command=input_num)
b1.place(x=0, y=72 , anchor='nw')

b0 = tk.Button(window, text='0', width=8, height=2,
    command=input_num)
b0.place(x=0, y=108 , anchor='nw')

b_dot = tk.Button(window, text='.', width=4, height=2,
    command=input_num)
b_dot.place(x=80, y=108 , anchor='nw')

tk.Label(frm_l, text='On the frm_l1', bg='red').pack()
tk.Label(frm_l, text='On the frm_l2', bg='green').pack()
tk.Label(frm_r, text='On the frm_r1', bg='blue').pack()
#tk.Label(frm_r, text='On the frm_r2', bg='pink').pack()
#觀察差別

window.mainloop()

'''
STANDARD OPTIONS

  activebackground, activeforeground, anchor,
  background, bitmap, borderwidth, cursor,
  disabledforeground, font, foreground
  highlightbackground, highlightcolor,
  highlightthickness, image, justify,
  padx, pady, relief, repeatdelay,
  repeatinterval, takefocus, text,
  textvariable, underline, wraplength

WIDGET-SPECIFIC OPTIONS

  command, compound, default, height,
  overrelief, state, width
  '''
