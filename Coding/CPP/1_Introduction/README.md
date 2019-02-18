### C++ Basics  
>### C++ 基本語法  

C++ Program is defined as `Objects` union, these Objects are affect each other.
>C++ 程序可以定義為對象的集合,這些對象通過調用彼此的方法進行交互.  

+ Object: Object is an instance of class, it could include value and fuction.  
>__對象__ 是 __類__ 的實例,具有 __`狀態`__ 和 __`行為`__ .  
>
|   [類]   |                  |                |
|--------|------------------|----------------|
| 對象   | 狀態             | 行為           |
| 一隻狗 | 顏色、名稱、品種 | 搖動、叫喚、吃 |
  
+ Class: Class is defined as a description of object's behavior, status template and blueprint.  
> __類__ 可以定義為描述對象之行為狀態之模板,一個類可以包含多個方法.
>
| [描述] |        |       |
|------|--------|-------|
| ->    | 對象 | .行為 |
| ->    | 狀態 | .模板 |


+ Method:  
> __方法__ 表示一種 __`行為`__,可以在其中 __寫入邏輯__ 以及 __操作數據__.
+ Variable: 
> __對象__ 有其獨特的 __即時變量__ , __對象__ 透過 __即時變量__ 得以創建不同 __`狀態`__ .  

_Sample.1-1_  
>print out "Hello World"  
輸出 "Hello World"  

```c++
#include <iostream>
using namespace std;
// main() 程序開始執行
int main()
{
   cout << "Hello World"; // 輸出 Hello World
   return 0;
}
```
解釋:  
+ 第一行頭文件 `<iostream>` ,定義程序中必需包含的訊息.  
+ `using namespace std;` 透過編譯器使用 std 命名空間.為 C++ 中的新概念.  
+ `// main() 是程序開始執行的地方` 是一個單行注釋.單行注釋以 `//` 開頭,在行末結束.  
+ `int main()` 是主函數,程序從這裡開始執行.  
+ `cout << "Hello World";` 會在屏幕上顯示消息 __"Hello World"__ .  
+ `return 0;` 調用返回值0,終止 __main( )__ 函數.

