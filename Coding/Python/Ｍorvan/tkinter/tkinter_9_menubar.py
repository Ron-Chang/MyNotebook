import tkinter as tk
#選單


window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('200x200')

l = tk.Label(window, text='do 0', bg='yellow')
l.pack()

counter = 1
def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="New..", command=do_job)
filemenu.add_command(label="Open..", command=do_job)
filemenu.add_command(label="Save..", command=do_job)

filemenu.add_separator()
#分割線

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label="Import..", menu=submenu, underline=1)
submenu.add_command(label='Submenu 1', command=do_job)
#次級選單

filemenu.add_separator()
filemenu.add_command(label="Quit", command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Cut", command=do_job)
editmenu.add_command(label="Copy", command=do_job)
editmenu.add_command(label="Paste", command=do_job)

window.config(menu=menubar)

window.mainloop()
