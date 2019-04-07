from openpyxl import Workbook, load_workbook
import random
import datetime as dt

# 建立工作簿
wb = Workbook()

# 建立起始表單
ws = wb.active

ws1 = wb.create_sheet() #默認插在工作簿末尾
ws2 = wb.create_sheet(index=0) # 插入在工作簿的第一個位置
# create_sheet(self,title=None,index=None)

# 表單命名
ws.title = "New Title"

# 表單標籤上色
ws.sheet_properties.tabColor = "EE27EB"

# 關鍵名稱賦值
ws1["A1"] = "ws1_A1"
ws1["b1"] = 100

# 方法賦值
ws2.cell(1,1).value = "ws2_A1"
ws2.cell(1,2).value = 100*3

# 迴圈賦值
for i in range(1,11):
    for j in range(1,11):
        foo = ws.cell(row = i, column = j)
        foo.value = i+j

# 調用函式
ws.cell(11,1).value = 7
ws.cell(11,2).value = "=SUMIF(A1:A10,A11,J1:J10)"

# 切片選取複數單元格
cell_range = ws1["G8":"S16"]

# 對所有單元格隨機賦(1,500)值
for i in cell_range:
    for j in i:

        j.value = random.randint(1,500)

cell_range = ws1["H9":"R15"]
# 加入條件,對所有單元格賦值
for i in cell_range:
    for j in i:
        if j.value > 250:
            j.value = ""

        cell_name = str(j).split(".")[1].strip(">")
        print(cell_name+": "+str(j.value))

# 加入日期
datetime_cell = ws["A12"]
datetime_cell.value = dt.datetime.now()
print(datetime_cell.value)

# 最大列row數、最小行column數應用
print(ws.max_row)
words = [chr(i) for i in range(65,91)]

current_max_row = ws.max_row

for i in range(0,len(words)):
    foo = ws.cell(row = ws.max_row+1, column = ws.min_column)
    # # or
    # foo = ws.cell(row = current_max_row+i, column = ws.min_column)

    print(i)
    foo.value = words[i]


# 儲存工作簿
wb.save('test.xlsx')


