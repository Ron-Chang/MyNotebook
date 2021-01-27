# SQLAlchemy and ORM

Note-taking from : [SQLAlchemy 與 ORM](https://blog.techbridge.cc/2017/08/12/python-web-flask101-tutorial-sqlalchemy-orm-database-models/)


# MVC


MVC 模式（Model–view–controller）是軟體工程中的一種軟體架構模式，把軟體系統分為三個基本部分：模型（Model）、視圖（View）和控制器（Controller）。

![mvc_role_diagram.png](mvc_role_diagram.png)

- 控制器（Controller）- 對 Request/Response 進行處理並透過 Controller 把 Model 的資料串接到 View（Templates）。
- 視圖（View） - 直接面對使用者的使用者介面設計。
- 模型（Model） - 負責和資料庫互動，儲存資料。

使用 MVC 的好處在於可以用更高階的角度去思考整個程式架構提高程式可重用性和降低程式耦合性。 事實上 Django、Rails 和 ASP.NET MVC 等較成熟的 Web 框架也是參考 MVC 的架構去設計。

# 關聯式資料庫（RDB）

Database 資料庫一個資料儲存的集合，方便我們去讀取新增刪除修改，而 Relational Database（關聯式資料庫）廣泛應用資料庫應用程式中，它把資料儲存在行列表格中，有可能不同資料表的內容會彼此依賴關聯。常見的關聯式資料庫，例如：MySQL、Postgres、Oracle、MSSSQL、SQLite。

# ORM

ORM 指的是 Object Relational Mapping（物件關聯對應），是一種程式設計技術，用於實現物件導向程式語言裡不同類型系統的資料之間的轉換。一般而言物件導向是從軟體工程基本原則（例如：耦合、聚合、封裝）的基礎上發展起來的，然而關聯式資料庫則是從數學理論發展而來的，兩套理論存在顯著的區別。為了解決這個不符合的現象，物件關聯對映技術搬演著中介層的角色，讓開發可以使用物件方式來操作資料庫，而不用使用 SQL 語法，當然若是要使用複雜的操作，仍需要使用到 SQL 語法。

# 使用 Flask SQLAlchemy

SQLAlchemy 是 Python 社群最廣泛使用的 ORM 套件。為了方便使用 ORM 來操作資料庫，我們使用 SQLAlchemy 的封裝 Flask SQLAlchemy 來進行 Models 的建立（當然你也可以單獨使用 SQLAlchemy）。

範例：

`models.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
```

`manage.py`
```python
# 建立資料表欄位
from main import db

class Todo(db.Model):
    # __table__name = 'user_table'，若不寫則看 class name
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Todo %r>' % self.content
```
操作：
```bash
$ python manage.py shell
>>> db.create_all()
```

# CRUD 操作設計

CRUD 是一般網路應用程式最常見的資料庫操作（create, read, update, delete），接著我們要使用 session 來操作我們的 CRUD 功能，首先先在終端機中輸入 $ python manage.py shell 後進行資料庫指令模擬操作（要注意的是 Flask SQLAlchemy 針對每個 request 會創建一個新的 session，若沒有 commit 的操作即被丟棄）

1. 新增（Create）
>新增一筆資料後將它加到 db.session 中，完成 commit：

```bash
>>> todo = Todo(content='hacking')
>>> db.session.add(todo)
>>> db.session.commit()
```

2. 讀取（Read）
Model.query 是 db.session.query(Model) 的簡寫，所以我們可以使用以下方式讀取資料庫資料：

```bash
# 取得所有 todo 資料
>>> todos = Todo.query.all()
>>> todos
# 限制 1 筆資料
>>> todos = Todo.query.limit(1).all()
# 正向/逆向排序
>>> todos = Todo.query.order_by(Todo.content).all()
>>> todos = Todo.query.order_by(Todo.content.desc()).all()
# 取得第一筆資料
>>> todo = Todo.query.first()
# 取得 primary key=1 一筆資料
>>> todo = Todo.query.get(1)
```
分頁（Pagination）
```bash
>>> todos = Todo.query.paginate(1, 10)
# 總頁數
>>> todos.pages
# 上/下一頁
>>> todos.prev()
>>> todos.next()
>>>
```

條件查詢（Filter）
```bash
>>> todo = Todo.query.filter_by(content='hacking').first()
```

```bash
>>> todos = Todo.query.filter(Todo.id > 1).all()
```

3. 修改（Update）

```bash
>>> todo = Todo.query.filter_by(contant='hacking').update({
    'content': 'reading'
})
>>> db.session.commit()
```

4. 刪除（Delete）

```bash
>>> todo = Todo.query.filter_by(content='reading').first()
>>> db.session.delete(todo)
>>> db.session.commit()
```

# 資料庫關聯用法

在關聯式資料庫中，最重要的就是資料表之間的關聯，透過關聯的使用，可以讓我們取得我們想要的資料。舉例而言，一篇部落格文章通常會對應多則評論，所以若是建立好關係則可以透過文章去取得所有和這篇文章有關的評論。同理，一篇文章通常會有多個 tag，而一個 tag 通常對應多篇文章，所以是個多對多關係。

- 一對多

`models.py`
```python
# 建立資料表欄位
from main import db

class Todo(db.Model):
    # __table__name = 'user_table'，若不寫則看 class name
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))
    user_id = db.Column(db.String(80), db.ForeignKey('user.id))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Todo %r>' % self.content

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    todos = db.relationship(
        'Todo',
        backref='user', # ref 可以讓我們使用 Todo.user 進行對 User 操作
        lazy='dynamic' # 有使用才載入，提昇效能
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name
```

操作方式：

```bash
>>> user = User.query.get(1)
>>> new_todo = Todo('Booking')
>>> new_todo.user_id = user.id
>>> db.session.add(new_todo)
>>> db.session.commit()
>>> user.todos
```

- 多對多

`models.py`

```bash
tags = db.Table('todo_tags',
    db.Column('todo_id', db.Integer, db.ForeignKey('todo.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

# 建立資料表欄位
from main import db

class Post(db.Model):
    # __table__name = 'user_table'，若不寫則看小寫 class name
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(80))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Todo %r>' % self.content

class Tag(db.Model):
    # __table__name = 'user_table'，若不寫則看 class name
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Tag %r>' % self.title
```

操作方式：

```bash
# 創建 3 個 todo
>>> todo_1 = Todo('Python')
>>> todo_2 = Todo('JS')
>>> todo_3 = Todo('R')

>>> tag_1 = Tag('coding')
>>> tag_1.tags = [todo_1, todo_2]
>>> db.session.add()
>>> db.session.commit()
```

# Flask Migration（Alembic）使用

隨著網路應用程式的發展，我們的 models 會不斷變更，為了記錄所有有關 models 的改動，我們使用 Flask-Migrate 這個 extensions。所有 models 改動都會記錄在 migration 檔案中，就像是資料庫的 git 一樣方便版本控制。

#### 安裝 Flask-Migrate：
```bash
$ pip install Flask-Migrate
```


#### 將 db 加入 Flask-Migrate 控制：

`manage.py`

```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from main import app
from models import Todo

# 設定你的 app
manager = Manager(app)
# 設定 python manage.py db 來管理 models
manager.add_command('db', MigrateCommand)
# 設定 python manage.py runserver 為啟動 server 指令
manager.add_command('runserver', Server())

# 設定 python manage.py shell 為啟動互動式指令 shell 的指令 
@manager.shell
def make_shell_context():
    return dict(app=app, Todo=Todo)

if __name__ == '__main__':
    manager.run()
```

#### 使用 `Flask-Migrate` 操作 DB：

```bash
# 初始化
$ python manage.py db init
# 記錄 model 變化
$ python manage.py db migrate
# 更新同步到 db
$ python manage.py db upgrade
# 查詢指令
$ python manage.py db --help
```


# 總結

本文介紹了資料庫、關聯式資料庫、ORM 的概念，我們也實際使用了 Flask SQLAlchemy 和 Flask-Migrate 來操作我們的資料庫。在接下來章節中我們將持續介紹 Python Web Flask 實戰開發，並學習現代化網站開發的方方面面。


# See also

1. [Wiki MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

image via [basicsofwebdevelopment](https://basicsofwebdevelopment.files.wordpress.com/2015/01/mvc_role_diagram.png)

作者：[@kdchang](https://blog.kdchang.cc/)
