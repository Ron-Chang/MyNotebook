# git 筆記

# 1. 基礎操作

## 設定登入資訊

```bash
git config --global user.name "Ron-Chang"
git config --global user.email "aaron9****9@gmail.com"
```

## 查閱設定
```bash
git config user.name
git config user.email
```

## 建立新的版本庫

1. 建立新的檔案
```bash
echo "# [README TITLE]" >> README.md
```
2. 初始化本地 [initialize]
```bash
git init
```
3. 把檔案加入舞台 [stage]
```bash
git add README.md
```
4. 註解並提交 [commit]
```bash
git commit -m "first commit"
```
5. 遠端加入 [remote]
```bash
git remote add origin git@github.com:Ron-Chang/repository.git
```
6. 推送至來源-主幹 [master] 
```bash
git push -u origin master
```

## 新增，推送
```bash
git add .
git commit -m "comment"
```
equivalent, if there's no new files.
```bash
git commit -am "comment"
```
提交修改至之前的commit中 amend(修訂)
>id 是會改變的  

```bash
git commit --amend --no-edit
```

## 取消提交 [unstaged]
```bash
git reset file.py
```


## 查閱紀錄
`git log`: 調閱紀錄檔。  
>> `git log --graph --oneline` 圖形化。  

`git diff`：與上一個版本不同處
>比對 committed(提交推送後的紀錄) & unstaged==modified（尚未推上舞台的改動)  
換句話說，add 放上舞台準備推送時，diff 就沒有東西了。
>>`git diff --cached`
>>用以對比，committed的版本 & staged==modified舞台上的版本  

>>`git diff HEAD`
>>用以對比，unmodified 跟 modified的版本

`git status`：檢查本機，舞台與遠端狀態
>> `git status -s`

`git reflog`: 調閱HEAD移動的紀錄(reference log)。 

## [專案]回朔到不同版本

以下皆為回到`上兩個`版本的方法  
- [x] `git reset --hard HEAD^^`  
- [x] `git reset --hard HEAD~2`  
- [x] `git reset --hard HEAD@{2}`  

直接前往指定id版本
```bash
git reset --hard id
```
## [文件]回朔到不同版本

```bash
git checkout commit.id -- file.py
```

# 2. 分支處理

### 分支列表
`git branch`

### 建立分支
`git branch [name]`

### 切換分支至
`git checkout [name]`

### 建立並且切換至新分支
`git checkout -b [name]`

### 刪除分支
`git branch -d [name]`

## 合併分支 [merge]
`git merge --no-ff -m "merge info." [name]` (no fast-forward)

### 處理合併衝突 [conflict]
```python
<<<<<<< HEAD
# HEAD VERSION
=======
# [name] VERSION
>>>>>>> [name]
```
排解合併衝突
```python
# HEAD VERSION and [name] VERSION
```
`git commit -am "solve conflict"`

## 重新定義參考基準[rebase] (接枝)  
>[What is rebase?](https://blog.yorkxin.org/2011/07/29/git-rebase.html)  

```bash
# step 1
(C1)--------------------(C3)-----[Branch A]--->
    \______(C2)___(C4)___[Branch B]--->

# step 2    把(C3)放置暫存(剪下分支)

                        (C3)

(C1)---------------------[Branch A]-------->
    \______(C2)___(C4)___[Branch B]-------->

# step 3    把[Branch B][Branch A]合併

                        (C3)

(C1)-------(C2)---(C4)------[Branch B]-->---[Branch A]--->

# step 4    把C3放回(接枝)
(C1)-------(C2)---(C4)--[Branch B]-->--(C3)--[Branch A]--->
```

## 實際操作
```bash
git checkout master
git rebase [name]
```
### 1. 解決衝突
### 2. 加入舞台,重新提交
### 3. `git rebase --continue`, 或是 `--skip`, `--abort`

## 臨時修改 [stash]

### 1. 暫存修改
```bash
git stash
```
### 2. 執行其他任務

### 3. 回復暫存
```bash
git stash pop
```


