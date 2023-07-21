[toc]

# passwordManager
以Python为编程语言，使用了Crypto、pyside6、sqlite3等，开发的简单密码管理程序。

# 作用

主要用于对密码信息进行存储，方便在本地对多个密码进行管理，提高安全性。

# 数据结构

程序使用的密码文件数据由6个字段组成，分别为主题、用户名、密码、描述、启动路径、分类

1. 主题字段用于对该文件进行简要描述，便于对密码文件进行识别，该字段为密码搜索时使用的字段。
2. 用户名字段用于存储密码文件的用户名信息
3. 密码字段以密文形式对密码进行存储
4. 描述字段用于对密码文件进行详细描述和补充说明，用于弥补主题字段的不足
5. 启动路径字段可以为网页url或.exe文件路径，便于直接启动程序
6. 分类字段用于对密码文件进行简单的归类，便于文件的管理，其中有一类别为“未分类”为保留值，不可删除，当某一类别被删除后，该类所有文件分类均会被设置为未分类

以下为一例数据结构

| 主题 | 用户名 |  密码  |       描述       | 启动路径   |   分类   |
| :--: | :----: | :----: | :--------------: | ---------- | :------: |
| test | test1  | 123456 | This is a test ! | ./test.exe | “未分类” |

# 使用方法

1. 首先通过登录界面进行登录，若没有账号需要先在登录界面进行注册（！！！账号注册后只能通过数据库操作进行删除，且密码不进行存储，无法找回）
2. 进入主界面后，右侧为密码文件及类别的增、删、查、改（查、改不可对类别进行）操作、左侧为文件信息的具体显示，且能够打开当前文件对应的网页及应用程序
3. 主界面上方菜单栏提供了对文件及分类的操作，窗口主题颜色的修改、及打开本帮助文档的功能。菜单栏下方工具栏提供文件与类别的增删改功能，以及密码的显示、输入框的清空功能，且支持拖拽放置与浮动。
4. 请注意，在对文件的路径、用户名、密码、描述等进行修改后必须点击修改按钮，否则所有修改都不会保存。此外，文件的主题新建后不可修改，新建时请注意

# 致谢

感谢xyn同学对第一版程序提出的展示形式及界面设计的建议，第一版程序着实简陋，到第二版能够勉强看得下去她功不可没。

