import tkinter as tk

window = tk.Tk()
window.title('btn_text_input by Ron')
window.geometry('200x200')

e = tk.Entry(window, show=None)

e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)



def insert_location():
    var = e.get()
    t.insert(0.0, var)


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
b2.pack()

b3 = tk.Button(window, text='insert location', width=15, height=2, command=insert_location)
b3.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()


