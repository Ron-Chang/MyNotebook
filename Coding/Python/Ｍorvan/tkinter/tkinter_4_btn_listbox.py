import tkinter as tk

window = tk.Tk()
window.title('btn_text_input by Ron')
window.geometry('200x200')


var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=30, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    #curselection = current selection
    #curselection為當前所選

    var1.set(value)


b1 = tk.Button(window, text='Print Selection', width=15, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set(('I', 'II', 'III', 'IV'))
#Set initial value by 'Set'
#利用Set 設定初始值

lb = tk.Listbox(window, listvariable=var2)

list_items = ['V', 'VI', 'VII', 'VIII']

#循環插入
for item in list_items:
    lb.insert('end', item)

lb.insert(0, '--Start--')

lb.insert(2, 'Second')
lb.delete(2)
#在第二行插入 Second
#刪除第二行
lb.insert('end', '--END--')
lb.pack()


window.mainloop()
