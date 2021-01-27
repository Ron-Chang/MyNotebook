import tkinter as tk
from tkinter import messagebox
#選單


window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('200x200')

def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='hahahahaha')
    #顯示-訊息

    #tk.messagebox.showwarning(title='Hi', message='wowowowow')
    #顯示-警告

    #tk.messagebox.showerror(title='Hi', message='nonononono')
    #顯示-錯誤

    #print(tk.messagebox.askquestion(title='Hi', message='askquestion'))
    #顯示-按鈕回傳字符串 (Return 'Yes' or 'No') 可用來控制變量

    #print(tk.messagebox.askyesno(title='Hi', message='askyesno'))
    #顯示-按鈕回傳布林選項 (Return True or Fales) 可用來控制變量

    print(tk.messagebox.askretrycancel(title='Hi', message='asktrycancel'))
    #顯示-按鈕回傳布林選項 (Return True or Fales) 可用來控制變量

    #print(tk.messagebox.askokcancel(title='Hi', message='askokcancel'))
    #顯示-按鈕回傳布林選項 (Return True or Fales) 可用來控制變量

tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()

'''help(tkinter.messagebox)
from tkinter import *
from tkinter import messagebox

askokcancel(title=None, message=None, **options)
    Ask if operation should proceed; return true if the answer is ok

askquestion(title=None, message=None, **options)
    Ask a question

askretrycancel(title=None, message=None, **options)
    Ask if operation should be retried; return true if the answer is yes

askyesno(title=None, message=None, **options)
    Ask a question; return true if the answer is yes

askyesnocancel(title=None, message=None, **options)
    Ask a question; return true if the answer is yes, None if cancelled.

showerror(title=None, message=None, **options)
    Show an error message

showinfo(title=None, message=None, **options)
    Show an info message

showwarning(title=None, message=None, **options)
    Show a warning message
'''
