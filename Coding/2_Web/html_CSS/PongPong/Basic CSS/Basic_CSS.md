# Basic CSS
  
We can get a basic HTML frame through a plug `Emmet` on `Sublime`, pressing `Tab` or `Ctrl+e` after `!`.  
Result:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

</body>
</html>
<!DOCTYPE html>
<html lang="en">
```
Here is a html and CSS sample without `Selector`.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Tutorial</title>
</head>
<body>
    <div style="width:300px; font-weight:bold; font-size:20px; border:2px dashed blue;">It's a nice weather today!</div>
    <div style="width:20%;height:70px; margin-top:10px; margin-bottom:10px; border:2px solid red; padding:20px">I took a walk at a park, and fed some <span style="color:red">pigeons</span>.<br>
    They are adorable.
    </div>
    <div style="width:300px; font-weight:bold; font-size:20px; border:2px dashed blue;">There were so many children over here</div>
    <div style="width:20%;height:70px; margin-top:10px; margin-bottom:10px; border:2px solid red; padding:20px">They had a good time with a <span style="color:red">slider</span> and <span style="color:red">swings</span>.<br>
    At meantime, There are few dogs and cats were hanging around.
    </div>
</body>
</html>
```
>`<div></div>` : separate the content as a block, and also make it to the different line.  
>`<span></span>` mark the important content without return.  

If we process that with `Selector`,
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Tutorial</title>
    <style type="text/css">
        .title{width:300px; font-weight:bold; font-size:20px; border:2px dashed blue;}
        .content{width:20%;height:70px; margin-top:10px; margin-bottom:10px; border:2px solid red; padding:20px}
        .keyword{color:red}
    </style>
</head>
<body>
    <div class="title">It's a nice weather today!</div>
    <div class="content">I took a walk at a park, and fed some <span class="keyword">pigeons</span>.<br>
    They are adorable.
    </div>
    <div class="title">There were so many children over here</div>
    <div class="content">They had a good time with a <span class="keyword">slider</span> and <span class="keyword">swings</span>.<br>
    At meantime, There are few dogs and cats were hanging around.
    </div>
</body>
</html>

```
