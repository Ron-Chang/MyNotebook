# What is Git?
### Briefly, it allows you to version control your program.

Normally, we have to create bunch files to keep a different version of code to prevent if there is something we need in the previous file.
for instance,

#### test_ver_1.0.0.py
> a function to remove even number call `REMOVE_EVEN_NUMBER`
#### test_ver_1.0.3_beta.py
> `REMOVE_EVEN_NUMBER` is not stable for the program, we rib it off
#### test_ver_1.7.2.py
> somehow we found a way can solve the issue of `REMOVE_EVEN_NUMBER` we put it back.
#### test_ver_2.0.0.py
> We still think our users private is priority. so we rib it again.

In git we just need one file
### test.py
In the `MASTER` branch
### test.py
create a new branch `DEVELOP`, add function `REMOVE_EVEN_NUMBER`, and the `MASTER` is still published
### test.py
finished testing `REMOVE_EVEN_NUMBER` merge branch `DEVELOP` back to Master, removed branch `DEVELOP`, `MASTER` got new function!
### test.py
if we dont need it. `git reset --hard HEAD~1` == `git reset --hard HEAD^` == `git reset --hard @^`
Reset to the last version, and continue to develop.
>`git reset .` and `git reset --hard`  
>`git branch` and `git branch <branch_name>`  
>`git checkout .` and `git checkout <branch_name>`  
>those command looks simlar but it's very different.  

you can choose what kind of version you would like to work with or release even published!
There is another benefit, in the open source world, you can easy to pulling, cloning someone’s code with git.

In the end you could be a part of the author make your contribution for the project your are interested in.

GIT is a command

There’s a few different websites provides version control and some of them is for free, but the most company paying for security.

STEP 1. Install homebrew
[https://docs.brew.sh/Installation](https://docs.brew.sh/Installation) Have a look!

Open your terminal cd to your home directory
`cd ~`
put the following line in your terminal and return
`mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew`

`mkdir` is make a folder name homebrew 
`&&` means at the same time doing the following actions
`curl` is a basic request to ask resource through internet.
if you install package with out homebrew you may see a lot of command with `curl`
