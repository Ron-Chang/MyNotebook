# RE Module  
<p align="right">This note took from <a href="https://youtu.be/K8L6KVGG-7o">Corey Schafer</a>'s Youtube tutorial</p>  

Sample_1 <a href="https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Regular-Expressions/simple.py">simple.txt</a>:  
```python
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)
```
  
<hr />  
<p align="right">原文 作者：<a href="https://blog.csdn.net/djskl/article/details/44357389">CSDN djskl</a></p>  

#### 1. match  
>re.match(pattern, string[, flags])
從首字母開始開始匹配，string如果包含pattern子串，則匹配成功，返回Match對象，失敗則返回None，若要完全匹配，pattern要以$結尾。  

#### 2. search  
>re.search(pattern, string[, flags])
若string中包含pattern子串，則返回Match對象，否則返回None，注意，如果string中存在多個pattern子串，只返回第一個。  

#### 3. findall  
>re.findall(pattern, string[, flags])
返回string中所有與pattern相匹配的全部字串，返回形式為數組。  

#### 4. finditer  
>re.finditer(pattern, string[, flags])
返回string中所有與pattern相匹配的全部字串，返回形式為迭代器。  

若匹配成功，match()/search()返回的是Match對象，finditer()返回的也是Match對象的迭代器，獲取匹配結果需要調用Match對象的group()、groups或group(index)方法。

group()、groups()與group(index)的區別，如下所示：

```python
>>> import re
>>> s = '23432werwre2342werwrew'
>>> p = r'(\d*)([a-zA-Z]*)'
>>> m = re.match(p,s)
>>> m.group()
'23432werwre'
>>> m.group(0)
'23432werwre'
>>> m.group(1)
'23432'
>>> m.group(2)
'werwre'
>>> m.groups()
('23432', 'werwre')
>>> m = re.findall(p,s)
>>> m
[('23432', 'werwre'), ('2342', 'werwrew'), ('', '')]
>>> p=r'(\d+)'
>>> m=re.match(p,s)
>>> m.group()
'23432'
>>> m.group(0)
'23432'
>>> m.group(1)
'23432'
>>> m.groups()
('23432',)
>>> m=re.findall(p,s)
>>> m
['23432', '2342']
```

綜上：
group()：母串中與模式pattern匹配的子串；
group(0)：結果與group()一樣；
groups()：所有group組成的一個元組，group(1)是與patttern中第一個group匹配成功的子串，group(2)是第二個，依次類推，如果index超了邊界，拋出IndexError；
findall()：返回的就是所有groups的數組，就是group組成的元組的數組，母串中的這一撮組成一個元組，那一措組成一個元組，這些元組共同構成一個list，就是findall()的返回結果。另，如果groups是只有一個元素的元組，findall的返回結果是子串的list，而不是元組的list了。

例子  
>s ="1113446777"  

用正則表達式把s分為1111, 3, 44, 6, 777

```python
>>> import re
>>> s='1113446777'
>>> m = re.findall(r'(\d)\1*',s)
>>> print m
['1', '3', '4', '6', '7']
>>> m = re.search(r'(\d)\*',s)
>>> m.group()
>>> m=re.search(r'(\d)\1*',s)
>>> m.group()
'111'
>>> m.groups()
('1',)
>>> m.group(0)
'111'
>>> m.group(1)
'1'
>>> m.group(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
>>> m=re.finditer(r'(\d)\1*',s)
>>> m.next().group()
'111'
>>> m.next().group()
'3'
>>> m.next().group()
'44'
>>> m.next().group()
'6'
>>> m.next().group()
'777'
>>> m.next().group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
另一个例子：  

```python
>>> p = r'(\d)\1+([a-zA-Z]+)'
>>> s = '1111werwrw3333rertert4444'
>>> p = r'(\d)\1+([a-zA-Z]*)'
>>> import re
>>> re.findall(p,s)
[('1', 'werwrw'), ('3', 'rertert'), ('4', '')]
>>> m = re.search(p,s)
>>> m.group()
'1111werwrw'
>>> m.group(1)
'1'
>>> m.group(2)
'werwrw'
>>> m.groups()
('1', 'werwrw')
>>> m = re.finditer(p,s)
>>> m.next().group()
'1111werwrw'
>>> m.next().group()
'3333rertert'
>>> m.next().group()
'4444'
>>> m.next().group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
