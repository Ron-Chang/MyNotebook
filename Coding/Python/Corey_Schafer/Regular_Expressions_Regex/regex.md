# Regular Expressions Regex  
<p align="right">This note took from <a href="https://youtu.be/sa-TUpSx1JA">Corey Schafer</a>'s Youtube tutorial</p>  

#### Sublime Text 3:  
1. Press `Command⌘ + F` to activate `Find...`.  
2. Press `⌘⌥R` or hit 'E' as following picture to turn on `Regular Expression`
![sublime_find](sublime_find.png)  

Sample_1 <a href="https://github.com/CoreyMSchafer/code_snippets/tree/master/Regular-Expressions">simple.txt</a>:  
```
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

cat
mat
pat
bat

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
153*918*1009
800-123-2929
800-142-4229

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

```

<a href="https://github.com/CoreyMSchafer/code_snippets/blob/master/Regular-Expressions/snippets.txt">Source</a>  
#### `.`  
It's going to match every charaters,including alphabets and symbols except new line.
>If we just need to look up '.', we have to combine backslash as `\.`.  
For instances, looking for "coreyms.com" we have to type in `coreyms\.com`.  

#### `\d`  
Digit (0-9)  
#### `\D`  
Not a Digit (0-9)  
>Get phone numbers_1  
`\d\d\d.\d\d\d.\d\d\d\d`  
-> 321-555-4321  
-> 123.555.1234  
-> 153\*918\*1009  
-> 800-123-2929  
-> 800-142-4229  

#### `\w`  
Word Character (a-z, A-Z, 0-9, _)  
#### `\W`  
Not a Word Character  

#### `\s`  
Whitespace (space, tab, newline)  
#### `\S`  
Not Whitespace (space, tab, newline)  
<hr />  

__*Attention: "\_\_" means is skipped in `find...` in those following smaples.*__  
#### `\b`  
Word Boundary  
#### `\B`  
Not a Word Boundary  
>   
Directly look up: `Ha` `HaHa`  
`\b`Ha: `Ha` `Ha`\_\_  
`\B`Ha: \_\_ \_\_`Ha`  
`\b`Ha`\b`: `Ha` \_\_\_\_  

#### `^`  
Beginning of a String  
>`^`Ha: `Ha` \_\_\_\_ 

#### `$`  
End of a String  
>Ha`$`: \_\_ \_\_`Ha`  


#### `[ ]`  
Matches Characters in brackets  
Get phone numbers_2: accept `-` and `.` only between numbers.  
>Input: `\d\d\d[-.]\d\d\d[-.]\d\d\d\d`  
>>-> 321-555-4321  
-> 123.555.1234  
-> 800-123-2929  
-> 800-142-4229  

>Input: `[89]00[-.]\d\d\d[-.]\d\d\d\d`  
>>-> 800-123-2929  
-> 800-142-4229  

> __*`[1234567]` == `[1-7]`*__  
Input: `[1-7]\d\d[-.]\d\d\d[-.]\d\d\d\d`  
>>-> 321-555-4321  
-> 123.555.1234  

> `[a-z]` All lower case alphabets  
`[a-zA-Z]` All alphabets  
`[a-zA-Z0-9]` All characters without symbols

#### `[^ ]`  
Matches Characters NOT in brackets  
It's opposite as `[ ]`  
>Input: `[^b]at`
>>-> cat  
-> mat  
-> pat  

>`[^a-z]`: Matches all characters except lower case characters. 

#### Quantifiers:  
\* - 0 or More  
\+ - 1 or More  
? - 0 or One  
{3} - Exact Number  
{3,4} - Range of Numbers (Minimum, Maximum)  

>Input: `\d{3}.\d{3}.\d{4}`  
>>-> 321-555-4321  
-> 123.555.1234  
-> 153\*918\*1009  
-> 800-123-2929  
-> 800-142-4229  

>Input: `Mr\.?\s[A-Z]\w+`  
("?" means it can be "1" period or "0" period after "Mr", then follow by a capital letter and more than "1" word character)  
>>-> Mr. Schafer  
-> Mr Smith  

>Input: `Mr\.?\s[A-Z]\w*`  
("?" means it can be "1" period or "0" period after "Mr", then follow by a capital letter and more than "0" word character)  
>>-> Mr. Schafer  
-> Mr Smith  
-> Mr. T  

#### `( )`  
Group  
#### `|`  
Either Or  
>Input: `M(r|s|rs)\.?\s[A-Z]\w*`  
("?" means it can be "1" period or "0" period after "Mr" or "Ms" or "Mrs", then follow by a capital letter and more than "0" word character)  
>>-> Mr. Schafer  
-> Mr Smith  
-> Ms Davis  
-> Mrs. Robinson  
-> Mr. T  


#### Get an emails  
>Input:`[a-zA-Z]+@[a-zA-Z]+\.com`  
>>-> CoreyMSchafer@gmail.com  

>Input:`[a-zA-Z]+@[a-zA-Z]+\.(com|edu)`  
>>-> CoreyMSchafer@gmail.com  
-> corey.schafer@university.edu  

>Input:`[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|edu|net)`  
>>-> CoreyMSchafer@gmail.com  
-> corey.schafer@university.edu  
-> corey-321-schafer@my-work.net  

#### Get an url's domain  
>Input:`https?://(www\.)?\w+\.\w+`  
>>-> https://www.google.com  
-> http://coreyms.com  
-> https://youtube.com  
-> https://www.nasa.gov  


>Make a group  
Input:`https?://(www\.)?(\w+)(\.\w+)`  
>>-> https://www.google.com  
-> http://coreyms.com  
-> https://youtube.com  
-> https://www.nasa.gov  

>Input Find:`https?://(www\.)?(\w+)(\.\w+)`  
Input Replace:`Group 1: $1`  
__*Atom and Sublime Text are both using `$` sign*__  
>>'https://www.google.com' -> 'Group 1: www.'  
'http://coreyms.com' -> 'Group 1: '  
'https://youtube.com' -> 'Group 1: '  
'https://www.nasa.gov' -> 'Group 1: www.'  

>Input Find:`https?://(www\.)?(\w+)(\.\w+)`  
Input Replace:`Group 3: $2`  
>>'https://www.google.com' -> 'Group 3: google'  
'http://coreyms.com' -> 'Group 3: coreyms'  
'https://youtube.com' -> 'Group 3: youtube'  
'https://www.nasa.gov' -> 'Group 3: nasa'  
Got a domain name

>Input Find:`https?://(www\.)?(\w+)(\.\w+)`  
Input Replace:`$2$3`  
>>'https://www.google.com' -> 'google.com'  
'http://coreyms.com' -> 'coreyms.com'  
'https://youtube.com' -> 'youtube.com'  
'https://www.nasa.gov' -> 'nasa.gov'  
Got domain

#### Read a Regex  
>Input: `[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+` 
>Translate:
>>`[a-zA-Z0-9_.+-]+`: more than "1" word and including "\_\.+-" and all alphabet and numbers.  
`@`: literal look up '@'  
`[a-zA-Z0-9-]+\.`: more than "1" word and including "-" and all alphabet and numbers follow by a period.  
`[a-zA-Z0-9.-]+`: more than "1" word and including "\.-" and all alphabet and numbers.  
