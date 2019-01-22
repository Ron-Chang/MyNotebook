# PHP  
<p align="right""> by <a href="https://youtu.be/ZdP0KM49IVk/">Jake Wright</a></p> 

### 1. Ｗhat is PHP?  
1. PHP: Hypertext Preprocessor. `超文本處理器`
2. We have to running PHP scripts on servers.  

### 2. What about PHP files?  
1. Including `HTML`, `JavaScript` and `PHP`.
2. Excute scripts on the server, and return html bacd to browsers.
3. Default extention is `.php`
>__PHP 檔案是什麼__  
PHP 文件可包含文本、HTML、JavaScript代碼和 PHP 代碼  
PHP 代碼在服務器上執行，結果以純 HTML 形式返回給瀏覽器  
PHP 文件的默認文件擴展名是 ".php"  

### 3. What can we do with PHP?  

1. Allow to creat `dynamic webpage`.  
2. Be able to `creat`, `open`, `read`, `write` and `close` documents on servers.  
3. Allow to collect forms and data.  
4. Be able to `post` and `get` cookies.  
5. `Add`, `delete` and `modify` data in database.  
6. `Add a limitation` for user to visit some pages.  
7. `Encoding` data.  
8. Allow to export image, PDF, Flash, XHTML, XML and so on `without HTML` through PHP.  

>__PHP 能做什麼__  
PHP 可以生成動態頁面內容  
PHP 可以創建、打開、讀取、寫入、關閉服務器上的文件  
PHP 可以收集表單數據  
PHP 可以發送和接收 cookies  
PHP 可以添加、刪除、修改您的數據庫中的數據  
PHP 可以限制用戶訪問您的網站上的一些頁面  
PHP 可以加密數據  
通過 PHP，您不再限於輸出 HTML。您可以輸出圖像、PDF 文件，甚至 Flash 電影。您還可以輸出任意的文本，比如 XHTML 和 XML。  

### 4. Why we use PHP?  

1. Support `Windows`, `Mac OS`, `Unix` and `Linux`.  
2. It's supported in most server environments ( `Apache`, `IIS`).  
3. It's supported wide database.  
4. It's `Free`, we can download it on [www.php.net](www.php.net) .  
5. Easy to learn and running effective on the server.  

>__為什麼使用 PHP？__  
PHP 可在不同的平台上運行（Windows、Linux、Unix、Mac OS X 等）  
PHP 與目前幾乎所有的正在被使用的服務器相兼容（Apache、IIS 等）  
PHP 提供了廣泛的數據庫支持  
PHP 是免費的，可從官方的 PHP 資源下載它： www.php.net  
PHP 易於學習，並可高效地運行在服務器端  


### 5. What are we going to do in this course?  
1. Installing WAMP/MAMP
2. PHP files
3. Outputting strings
4. Variables
5. Concatenation
6. Operators
7. If statements
8. Handling data from HTML forms
9. Arrays
10. Loops

Sample:  
```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <?php

    echo "Hello, World!";

    ?>
</body>
</html>
```
>result:  
Hello, World!

If we need a variable, we have to announce it with `$`.  

```php
$myvar = "This is my variable.";
echo $myvar;
```
>result:  
This is my variable.  

```php
$number_1 = 5;
$number_2 = 7;
$sum = $number_1 + $number_2;
echo $sum;
```
>result:  
12  

```php
$name = "Ron";
echo "Hello, " . $name."!";
echo "<br>";
```
>result:  
Hello, Ron!  
<br>  

```php
$loggedIn = 1; //1 == true, 0 == false and None -> null
if ($loggedIn == true){
    echo "You are logged in";
}else{
    echo "Please log in";
}
```
>result:  
You are logged in  

### Create a page linking php file  

`/index.html`  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>index.html</title>
    </head>
<body>
    <form action="process.php" method="post">
        Enter your name: <input name="user_name" type="text">
        <input type="submit">
    </form>
</body>
</html>
```
>result:  
![](link_php_files.png)  

`/process.php`  
```php
<!DOCTYPE html>
<html>
    <head>
        <title>process.php</title>
    </head>
<body>
    <?php

        $name = $_POST["user_name"];
        echo "Hello, " . $name;

    ?>
</body>
</html>
```
>result:  
Hello, Ron  

### Arrays  

```php
<!DOCTYPE html>
<html>
    <head>
        <title>process.php</title>
    </head>
<body>
    <?php

        //$people1 = "Ano";
        //$people2 = "Ron";
        //$people3 = "Catherine";
        
        $people = array("Ano", "Ron", "Catherine");

        print_r($people);
        echo "<br>";
        echo $people[2];

    ?>
</body>
</html>
```
>result:  
Array ( [0] => Ano [1] => Ron [2] => Catherine )  
Catherin  


### FOR  

```php
<!DOCTYPE html>
<html>
    <head>
        <title>process.php</title>
    </head>
<body>
    <?php

        $people = array("Ano", "Ron", "Catherine");

        // put element from $people into $i and print $i
        foreach ($people as $i){
            echo $i . ' ';
        }

    ?>
</body>
</html>
```
>Result:  
Ano Ron Catherine  

```php
<!DOCTYPE html>
<html>
    <head>
        <title>process.php</title>
    </head>
<body>
    <?php

        $numbers = array(5, 3, 7);
        $sum = 0;
        foreach ($numbers as $number){
            $sum = $sum + $number;
        }
        echo $sum;
    ?>
</body>
</html>
```
>Result:  
15  
