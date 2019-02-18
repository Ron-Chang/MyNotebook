## ls -l & chmod  
>Stand for __ch__ange __mod__e  

chmod format:  
```bash
chmod [options] mode[,mode] file1 [file2 ...]
```

使用ls命令的查看文件或目錄的屬性

```bash
ls -l file
```

### Octal 八進制語法
chmod使用八進制來指定權限。
文件或目錄的權限位是由9個權限位來控制,每三位為一組,  


|                       |    4    |    2     |     1      |
|-----------------------|---------|----------|------------|
| 擁有用戶  USER(OWNER) | Read(r) | Write(w) | Execute(x) |
| 群組用戶  GROUP       | Read(r) | Write(w) | Execute(x) |
| 其它用戶  OTHER       | Read(r) | Write(w) | Execute(x) |


文件權限被放在一個比特掩碼中，掩碼中指定的比特位設為1，用來說明一個類具有相應的優先級。
chmod的八進制語法的數字說明:  

| r | w | x | - |
|---|---|---|---|
| 4 | 2 | 1 | 0 |
  
所有者的權限用數字表達: 屬主的那三個權限位的數字加起來的總和. 如rwx, 也就是4+2+1, 應該是7.  
用戶組的權限用數字表達: 屬組的那個權限位數字的相加的總和. 如rw-, 也就是4+2+0, 應該是6.  
其它用戶的權限數字表達: 其它用戶權限位的數字相加的總和. 如r-x, 也就是4+0+1, 應該是5.  

| 第一位 | d | (directory)為目錄文件 |
|--------|---|-----------------------|
|        | l | (link)連結文件        |
|        | - | 普通文件              |
|        | p | 管道                  |
  

|  第2-4位   |   | (使用者權限)  |
|------------|---|---------------|
| 權限數字 4 | r | (read)讀      |
| 權限數字 2 | w | (write)寫     |
| 權限數字 1 | x | (execute)執行 |

| 第5-7位  | rwx 讀 寫 執行 | (同階使用者的權限) |
|----------|----------------|--------------------|
| 第8-10位 | rwx 讀 寫 執行 | (其他使用者的權限) |

__*若文件或目錄有延伸屬性在權限許可文字後方追加`＠`*__  
__*若文件或目錄有延伸安全資訊在權限許可文字後方追加`＋`*__  
>If the file or directory has extended attributes, the permissions field printed by the `-l` option is followed by a `@` character.  
Otherwise, if the file or directory has extended security information, the permissions field printed by the `-l` flag is followed by a `+` character.  
  
  
Reference:  
<ul>
    <li><a href="https://zh.wikipedia.org/wiki/Chmod">[wiki]</a></li>
    <li><a href="https://youtu.be/wXVauecQPI0">[Youtube]</a></li>
</ul>
