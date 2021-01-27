import tkinter as tk

window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('300x200')

l = tk.Label(window, bg='yellow', text='What would you like for dinner?')
l.pack()

def print_selection(v):
    l.config(text='吃 (Have)' + v)

s = tk.Scale(window,

    label='Height',
    from_=200, to=140,
    orient=tk.VERTICAL,
    length=360, resolution=1,
    tickinterval=3,
    showvalue=0,

    command=print_selection)
'''
數值(注意底線)
從from_
到to

-orient(方向)
垂直VERTICAL
水平HORIZONTAL

-length(長度單位為 pixel)
-showvalue(拖動時是否顯示數值 布林表示 [1,0])
-tickinterval(尺標單位),
-resolution(1為整數, 0.1保留小數下一位)
'''
s.pack()

window.mainloop()
