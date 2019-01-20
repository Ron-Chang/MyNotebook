# Learn CSS in 12 minutes
<p align="right""> by <a href="https://youtu.be/0afZj1G0BIE/">Jake Wright</a></p> 
   
__Frame__:  
<p align="center"><img src="https://raw.githubusercontent.com/Ron-Chang/MyNotebook/master/Coding/2_Web/html_CSS/Jake_Wright%20/CSS_in_12_Mins/img/div.png"/><br>
Btw, there is a mistake in this picture,<br> It's not <del>#heads</del>, please instead of `#header`.</p>  
__HTML__:  

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>Examples</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="sample.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <div id="container">
        <div id="header">
            <h1>My Website</h1>
        </div>
        <div id="content">
            <div id="nav">
                <h3>Navigation</h3>
                <ul>
                    <li><a href="" class="selected">Home</a></li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </div>

            <div id="main">
                <h2>Home Page</h2>
            <p>I introduce CSS, explain how to link a CSS file with an HTML document and teach the syntax of the language along with the most common properties.<br>Support this channel at <a href="https://www.patreon.com/jakewright">HERE</a></p>
            <p>----------- More tutorials -----------<br>Learn HTML in 12 Minutes: <a href="http://youtu.be/bWPMSSsVdPk">Link</a> <br>Learn More HTML in 12 Minutes: <a href="http://youtu.be/KJ13lX20FqU">Link</a> <br>Learn JavaScript in 12 Minutes: <a href="http://youtu.be/Ukg_U3CnJWI">Link</a> <br>Learn PHP in 15 Minutes: <a href="http://youtu.be/ZdP0KM49IVk">Link</a>
            </p>
            <p>----------- Text editors ----------- <br>For Windows users, I recommend using Notepad++ to edit HTML files:<a href="http://notepad-plus-plus.org">Link</a> <br>For Mac users, I recommend Sublime Text:<a href="http://www.sublimetext.com">Link</a>
            </p>
            </div>
        </div>
        <div id="footer">
            Copyright &copy; 2019 Jake Wright.
        </div>
    </div>
</body>
</html>
```  

__CSS__:  

```css
body{
    background-color: #EEE;
    /*#EEE = #EEEEEE*/
    font-family: Helvetica, Arial, sans-serif;
}

a{
    text-decoration: none;
    color: red;
}

h1, h2, h3{
    margin: 0;
}

#container{
    background-color: white;
    width: 800px;
    margin-left: auto;
    margin-right: auto;
}

#header {
    background-color: #66CCFF;
    color: #white;
    padding: 10px;
    text-align: center;

}

#content{
    padding: 10px;
    /*padding: top right bottom left;*/
    /*padding: 10px 10px 10px 10px == padding: 10px;*/
}

#nav{
    width: 180px;
    float: left;
}

#nav .selected{
    font-weight: bold;
}

#nav ul{
    list-style-type: none;
    padding: 0;
}

#main{
    width: 600px;
    float: right;
}

#footer{
    clear: both;
    padding: 10px;
    background-color: #999;
    color: white;
    text-align: right;
}

```

__result__:  
<p align="center">
<img src="https://github.com/Ron-Chang/MyNotebook/blob/master/Coding/2_Web/html_CSS/Jake_Wright%20/CSS_in_12_Mins/img/result.png?raw=true" />
</p>  

## Note:  

Basic:  
```css
#id {
    /*property_name:value;*/
    color: #00f0f0;
}
```
Assign on the tags, such as, `<body>`, `<h1>` and `<a>`.
```css
a, body, h1{
    /*property_name:value;*/
    color: #00f0f0;
}
```
Assign to particular class
```css
.class{
    /*property_name:value;*/
    color: #00f0f0;
}
```
Assign both id and class, split with comma
```css
#id, .class {
    /*property_name:value;*/
    color: #00f0f0;
}
```
Assign particular class under a specific id
```css
#id .class {
    /*property_name:value;*/
    color: #00f0f0;
}
#body .id .class {
    /*property_name:value;*/
    color: #00f0f0;
}
```

We can also put a `<style>` tag into a html, without link to css file.
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        #id{
            /*property_name:value;*/
            background-color: grey;
        }
    </style>
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```
or, use a inline css
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1 style="property_name:value; color:#00f0f0;">Navigation</h1>
</body>
</html>
```
But, Recommand separate it!  
