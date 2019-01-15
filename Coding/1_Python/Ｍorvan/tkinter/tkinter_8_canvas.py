import tkinter as tk
#畫布


window = tk.Tk()
window.title('Radio BTN by Ron')
window.geometry('600x600')

canvas = tk.Canvas(window, bg='#DA9E40', height=300, width=400)
image_file = tk.PhotoImage(file='/Users/ron/Documents/Python/practice/tkinter/test_img.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
'''anchor 錨點位置 圖片何處為起點
分別用方位角的字首來表示
東e 西w 南s 北n
中center
西北nw 西南sw 東北ne 東南se
all of them are lowercases
'''
x0, y0, x1, y1 = 50, 50, 80, 80

line = canvas.create_line(x0, y0, x1, y1)
#畫線
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
#畫圓
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=135)
#扇形 strat=起始角 extent=結束角
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
#矩形
canvas.pack()

def moveit():
    canvas.move(rect, 0, 10)
    #(物件, x, y)
    canvas.move(image, 2, 3)

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()
