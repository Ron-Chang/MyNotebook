import tkinter as tk

window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('300x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', text='今天晚上吃( What would you like for dinner?)')
l.pack()

def print_selection():
    l.config(text='吃 (Have)' + var1.get())


r1 = tk.Radiobutton(window, text='A套餐( Meal A)', variable=var1, value='Pizza', command= print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='B套餐( Meal B)', variable=var1, value='Pasta', command= print_selection)
r2.pack()

r2 = tk.Radiobutton(window, text='C套餐( Meal C)', variable=var1, value='Kabab', command= print_selection)
r2.pack()

window.mainloop()
