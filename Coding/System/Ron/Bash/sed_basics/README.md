# [Linux Commands Tutorial - sed basics](https://www.youtube.com/watch?v=uVJpq_Tq-fE) by Lambdanautic

#### FYI: There is a slightly difference between macOS and linux.
For macOS users:
> I assume you have installed homebrew and zsh.
```bash
brew install gnu-sed
source ~/.zshrc
```

## Topics covered
1. Modes of operation
2. example: filtering lines by linenumber
3. example: filtering lines by content
4. example: removing text within line
5. example: replacing text within line

#### examples: `my.csv`
```csv
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```

### That's Get it Start!
1. Print it all without any condition.
```bash
cat my.csv | sed -r ''
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
> --regexp-extended | `macOS`: -E; `Linux`: -E, -r

2. Print it all without the 2nd to the 4th line include the 4th.
```bash
$ cat my.csv | gsed -r "2,4d"
id,name,description,participants
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
> `d` refernce 'delete' or 'do not print it'
> 2 and 4 nothing to do with id just mean for the line number.

3.Print 2nd to the 4th lines.
```bash
$ cat my.csv | gsed -n -r "2,4p"
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
```
> -n, --quiet, --silent | suppress automatic printing of pattern space
```bash
$ cat my.csv | gsed -r "2,4p"
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
```bash
$ cat my.csv | gsed -r -n "2,4d"

```

4. Print it all except the lines including Frank
```bash
$ cat my.csv | gsed -r '/Frank/d'
id,name,description,participants
3,"test3","description test 3","Dennis,Jamie,Jim"
5,"test5","description test 5","Mike,Tom,Jamie"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
9,"test9","description test 9","Ann,Tim"
```
> put pattern in `/pattern/`

5. Print it all the lines including Frank
```bash
$ cat my.csv | gsed -n -r '/Frank/p'
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
6,"test6","description test 6","John,Mike,Frank"
8,"test8","description test 8","Frank,Jamie"
```
> equivalent `cat my.csv | grep Frank`

6. Substitude the pattern
```bash
$ cat my.csv | gsed -r 's/Frank/Wayne/'
id,name,description,participants
1,"test1","description test 1","Wayne,Tom,Dennis"
2,"test2","description test 2","Julia,Wayne,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Wayne,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Wayne"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Wayne,Jamie"
9,"test9","description test 9","Ann,Tim"
```
> `gsed -r 's/{old}/{new}/'`
> `s` reference for 'substitute'
```bash
$ cat my.csv | gsed -r 's/test/nothing/'
id,name,description,participants
1,"nothing1","description test 1","Frank,Tom,Dennis"
2,"nothing2","description test 2","Julia,Frank,Tim"
3,"nothing3","description test 3","Dennis,Jamie,Jim"
4,"nothing4","description test 4","Tom,Tim,Frank,Julia"
5,"nothing5","description test 5","Mike,Tom,Jamie"
6,"nothing6","description test 6","John,Mike,Frank"
7,"nothing7","description test 7","Julia,Ann,Dennis,Tom"
8,"nothing8","description test 8","Frank,Jamie"
9,"nothing9","description test 9","Ann,Tim"
```
> It will just apply on the fisrt match.

7. Replace all the matches in every lines
```bash
$ cat my.csv | gsed -r 's/test/nothing/g'
id,name,description,participants
1,"nothing1","description nothing 1","Frank,Tom,Dennis"
2,"nothing2","description nothing 2","Julia,Frank,Tim"
3,"nothing3","description nothing 3","Dennis,Jamie,Jim"
4,"nothing4","description nothing 4","Tom,Tim,Frank,Julia"
5,"nothing5","description nothing 5","Mike,Tom,Jamie"
6,"nothing6","description nothing 6","John,Mike,Frank"
7,"nothing7","description nothing 7","Julia,Ann,Dennis,Tom"
8,"nothing8","description nothing 8","Frank,Jamie"
9,"nothing9","description nothing 9","Ann,Tim"
```
> `g` reference for 'global'.
> be aware of the pattern is case-sensitive.
```bash
$ cat my.csv | gsed -r 's/TEST/nothing/g'
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```

8. Replace the pattern case-insensitive
```bash
$ cat my.csv | gsed -r 's/TEST/nothing/gi'
id,name,description,participants
1,"nothing1","description nothing 1","Frank,Tom,Dennis"
2,"nothing2","description nothing 2","Julia,Frank,Tim"
3,"nothing3","description nothing 3","Dennis,Jamie,Jim"
4,"nothing4","description nothing 4","Tom,Tim,Frank,Julia"
5,"nothing5","description nothing 5","Mike,Tom,Jamie"
6,"nothing6","description nothing 6","John,Mike,Frank"
7,"nothing7","description nothing 7","Julia,Ann,Dennis,Tom"
8,"nothing8","description nothing 8","Frank,Jamie"
9,"nothing9","description nothing 9","Ann,Tim"
```
> `i` for 'insensitive'

9. Remove the pattern matches
```bash
$ cat my.csv | gsed -r 's/TEST//gi'
id,name,description,participants
1,"1","description  1","Frank,Tom,Dennis"
2,"2","description  2","Julia,Frank,Tim"
3,"3","description  3","Dennis,Jamie,Jim"
4,"4","description  4","Tom,Tim,Frank,Julia"
5,"5","description  5","Mike,Tom,Jamie"
6,"6","description  6","John,Mike,Frank"
7,"7","description  7","Julia,Ann,Dennis,Tom"
8,"8","description  8","Frank,Jamie"
9,"9","description  9","Ann,Tim"
```
> Simply just left the second gap empty.

10. Process in the specific lines
```bash
$ cat my.csv | gsed -r '2,4 s/TEST/nothing/gi'
id,name,description,participants
1,"nothing1","description nothing 1","Frank,Tom,Dennis"
2,"nothing2","description nothing 2","Julia,Frank,Tim"
3,"nothing3","description nothing 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
or 
```bash
$ cat my.csv | gsed -r '3,+4 s/TEST/nothing/gi'
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
2,"nothing2","description nothing 2","Julia,Frank,Tim"
3,"nothing3","description nothing 3","Dennis,Jamie,Jim"
4,"nothing4","description nothing 4","Tom,Tim,Frank,Julia"
5,"nothing5","description nothing 5","Mike,Tom,Jamie"
6,"nothing6","description nothing 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
or
```bash
$ cat my.csv | gsed -r '5,$ s/TEST/nothing/gi'
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"nothing4","description nothing 4","Tom,Tim,Frank,Julia"
5,"nothing5","description nothing 5","Mike,Tom,Jamie"
6,"nothing6","description nothing 6","John,Mike,Frank"
7,"nothing7","description nothing 7","Julia,Ann,Dennis,Tom"
8,"nothing8","description nothing 8","Frank,Jamie"
9,"nothing9","description nothing 9","Ann,Tim"
```
> `$` dollar sign means 'to the end' of the file

11. Save to a file
__*Cannot overwrite itself*__
```bash
$ cat my.csv | gsed -r '' > my.csv.bak
```
12. Append to a file
__*Cannot overwrite itself*__
```bash
$ cat my.csv | gsed -r '' >> my.csv.bak
```
13.Apply the modification to the current file
```bash
$ cat my.csv | gsed -i -r 's/TEST/WOW/gi' my.csv

```

14. Working with regular expression
- Delete specific line
```bash
$ cat my.csv | gsed -r '/^id.*participants$/d'
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
- Insert or Append a new line
> '/{REGULAR-EXPRESSION}/i{NEW-LINE-INSERTED}'
> '/{REGULAR-EXPRESSION}/a{NEW-LINE-APPENDED}'

1. Insert a line before the line including Tom
```bash
$ cat my.csv | gsed -r '/Tom/iHERER INSERT A NEW LINE/'
id,name,description,participants
HERER INSERT A NEW LINE/
1,"test1","description test 1","Frank,Tom,Dennis"
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
HERER INSERT A NEW LINE/
4,"test4","description test 4","Tom,Tim,Frank,Julia"
HERER INSERT A NEW LINE/
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
HERER INSERT A NEW LINE/
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```
2. Append a line before the line including Julia
```bash
$ cat my.csv | gsed -r '/Julia/iHERER APPEND A NEW LINE/'
id,name,description,participants
1,"test1","description test 1","Frank,Tom,Dennis"
HERER APPEND A NEW LINE/
2,"test2","description test 2","Julia,Frank,Tim"
3,"test3","description test 3","Dennis,Jamie,Jim"
HERER APPEND A NEW LINE/
4,"test4","description test 4","Tom,Tim,Frank,Julia"
5,"test5","description test 5","Mike,Tom,Jamie"
6,"test6","description test 6","John,Mike,Frank"
HERER APPEND A NEW LINE/
7,"test7","description test 7","Julia,Ann,Dennis,Tom"
8,"test8","description test 8","Frank,Jamie"
9,"test9","description test 9","Ann,Tim"
```

### DOES NOT SUPPORT `\d`, `\D`, `\s` and etc, except `\w`. Ee can easy to use `[[:space:]]` `[[:digit:]]` or`[0-9]` to instead, if necessary.
