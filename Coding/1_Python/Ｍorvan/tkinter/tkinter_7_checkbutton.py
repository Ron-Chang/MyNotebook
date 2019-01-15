import tkinter as tk

window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('300x200')

l = tk.Label(window, bg='yellow', text='Which computer language you feel like?')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 1):
        l.config(text='I love both!')
    elif (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python!')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++!')
    else:
        l.config(text='I do not love either.')


var1 = tk.IntVar()
#宣告整數函數
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
# 選中 or啟動( onvalue) variable == 1
# 未選中 or未啟動( offvalue) variable == 0
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2.pack()

window.mainloop()
