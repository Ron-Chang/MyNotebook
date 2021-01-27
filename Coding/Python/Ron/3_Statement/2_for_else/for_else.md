# FOR...ELSE STATEMENT  
<p align="right">This note took from <a href="https://foofish.net/for-else.html">liuzhijun</a></p>

### if...else...  
>Once achieved the condition, we excute if statement, or excute statement.  

>如果滿足條件就執行(if)內敘述，否則執行(else)內敘述。  

```python
# Format:
if a==b:
    print("true")
else:
    print("false")
```

### for...else...  
In Pyhton, `else` not only can work with `if`, but also capible to work with `while` and `try...except`, for instance,  

然而，在 Python 中 `else` 不僅能和 `if` 搭配使用，還有另一種特有的句法是 `for else`，此外，還可以和 `while`、`try except` 組合使用，例如：  

```python
for i in range(3):
    print(i,end=', ')
else:
    print("end")

'''
result:
0, 1, 2, end
'''
```
>If we follow the experiences about `if esle` statements, There's only one will be excuted. However,It just shows the opposite result, `print("end")` is excuted after `for loop` finished in this instance. That's odd. If we translate as a human language.  
`if else`: __*`if` something happened, do A `or` do B*__.  
`for else`: __*We're doing B, no matter A has or has not been excuted.*__  

>根據以往的經驗，一旦執行了`if` 之中的敘述，就不會執行 else 內的敘述，反之亦然，但是`for else` 卻與`if else` 卻呈現出相反的結果，當`for` 循環结束後，卻又執行了`else` 內的函數，`if else` 白話來說就是`如果 否则`，而`for else` 翻成白話更接近`直到 然后`，再理解成英文的`for then`更為恰當。

Another exsample:  
```python
for i in []:
    print(i)
else:
    print("end")
'''
result:
end
'''
```
>Although we running an empty list in the begin, the else statement still has been excuted.  

>即使`for`循環的項目是一個空列表，仍然會執行else下的敘述。

How about insert a `break`,  

如果我們用break提前終止`for`循環  
```python
for i in range(3):
    print(i)
    if i % 2 == 0:
        break
else:
    print("end")

'''
result:
0
'''
```
>The fuction is terminated once break has been excuted.  

>循環遇到`break` 後，直接跳過`else`就結束了。  


綜上所述，可以得出一個結論，只有當循環裡沒有遇到 `break` 時，`else` 才會執行。真正和 `else` 搭配使用的是 `for` 循環中的 `break`，`break` 與 `else` 才是兩個互斥的條件。  

「python之禪」告訴了我們答案：
>"Although that way may not be obvious at first unless you're Dutch."。  

在平時的開發中真的很少有 `for else` 的應用場景，不過，像下面這種場景用 `for else` 還真是一種 pythonic 的用法。

當你用 for 循環疊代查找列表的中的某個元素時，如果找到了就立刻退出循環，如果疊代完了列表還沒找到需要以另外一種形式（比如異常）的方式通知調用者時，用 `for else` 無疑是最好的選擇。

<a href="https://stackoverflow.com/a/9980752/1392860">source</a>
```python
for i in mylist:
    if i == target:
        break
    process(i)
else:
    raise ValueError("List argument missing terminal flag.")
```

如果不用 `for else` ， 那麼還需要專門建立一個臨時標記變量來標記是否已經找到了  

```python
found = False
for i in mylist:
    if i == target:
        found = True
        break
    process(i)

if not found:
    raise ValueError("List argument missing terminal flag.")
```
當你想在房間裡找某樣東西時，只要在任意位置找到了，就停止繼續搜查工作。但如果把整個房間都翻遍了，還沒找到我們想要的東西時，需要告訴人家，很抱歉，這兒沒有你要找的東西。遇到這樣的情況時就用 `for else` ，除此之外，恐怕只會引起誤操作。
