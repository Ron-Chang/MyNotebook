import tkinter as tk

window = tk.Tk()
window.title('btn_text_input by Ron')
window.geometry('200x200')

e = tk.Entry(window, show=None)
'''The first method means this entry on the window.
第一個方法表示輸入框在視窗內
The second one means don't hide any text input.
第二個方法表示不隱藏輸入的文字
列如：show='*'所有輸入文字皆顯示為星號

-miner prank
change * as a random alphbet to scare people
'''
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)
    #insert -> 在指標出現的地方插入文字

def insert_end():
    var = e.get()
    t.insert('end', var)
    #end -> 在文末插入文字


def insert_location():
    var = e.get()
    t.insert(0.0, var)
    #num(j).num(k) -> 最後一種方法，在第j行，第k列插入文字，起始值為零

b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
b2.pack()

b3 = tk.Button(window, text='insert location', width=15, height=2, command=insert_location)
b3.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()

'''
 |      STANDARD OPTIONS
 |
 |          activebackground, activeforeground, anchor,
 |          background, bitmap, borderwidth, cursor,
 |          disabledforeground, font, foreground
 |          highlightbackground, highlightcolor,
 |          highlightthickness, image, justify,
 |          padx, pady, relief, repeatdelay,
 |          repeatinterval, takefocus, text,
 |          textvariable, underline, wraplength
 |
 |      WIDGET-SPECIFIC OPTIONS
 |
 |          command, compound, default, height,
 |          overrelief, state, width
'''
