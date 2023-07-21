# 导入sys
import os
import sys

from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QMessageBox,QFileDialog,QTreeWidgetItem,QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QUrl
from qt_material import apply_stylesheet

from Main_window import Ui_Main
from Login_window import Ui_Login
from New_window import Ui_New
from Type_window import Ui_Type
from About_window import Ui_About

from user import Admin,User
from PWsql import RESERVED_THEME

import config

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(config.main_window_ico))
        self.beautify()

    def beautify(self):
        self.ui.search_btn.setIcon(QIcon(config.search_ico))
        self.ui.refresh_btn.setIcon(QIcon(config.refresh_ico))
        self.ui.add.setIcon(QIcon(config.add_ico))
        self.ui.remove.setIcon(QIcon(config.remove_ico))
        self.ui.update.setIcon(QIcon(config.update_ico))
        self.ui.start_btn.setIcon(QIcon(config.start_ico))
        self.ui.choose_btn.setIcon(QIcon(config.choose_ico))
        self.ui.new_type.setIcon(QIcon(config.add_type_ico))
        self.ui.remove_type.setIcon(QIcon(config.remove_type_ico))
        self.ui.about_btn.setIcon(QIcon(config.about_ico))
        self.ui.toolShowPW.setIcon(QIcon(config.show_ico))
        self.ui.toolClear.setIcon(QIcon(config.clear_ico))
        self.ui.toolNewFile.setIcon(QIcon(config.add_ico))
        self.ui.toolNewType.setIcon(QIcon(config.add_type_ico))
        self.ui.toolDelFile.setIcon(QIcon(config.remove_ico))
        self.ui.toolDelType.setIcon(QIcon(config.remove_type_ico))
        self.ui.toolUpdate.setIcon(QIcon(config.update_ico))



class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(config.login_window_ico))
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.beautify()

    def beautify(self):
        self.ui.login_btn.setIcon(QIcon(config.login_ico))
        self.ui.new_btn.setIcon(QIcon(config.sign_up_ico))

class NewWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_New()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(config.new_window_ico))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.beautify()

    def beautify(self):
        self.ui.ok_btn.setIcon(QIcon(config.ok_ico))

class TypeWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Type()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(config.type_window_ico))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.beautify()

    def beautify(self):
        self.ui.ok_btn.setIcon(QIcon(config.ok_ico))

class AboutWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(config.about_window_ico))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.about.load(QUrl.fromLocalFile(os.path.abspath(r"./src/html/README.html")))



user:User = None
newWindow:NewWidget = None
typeWindow:TypeWidget = None
aboutWindow:AboutWidget = None

def login():
    global loginWindow,mainWindow,admin,user
    name = loginWindow.ui.name_edit.text()
    pw = loginWindow.ui.pw_edit.text()
    if admin.login(name,pw):
        user = User(name, pw, "./src/db/pw.db",admin.get_item(name)[0][2])
        loginWindow.close()
        mainWindow.show()
        refresh_tree()
        clear_input()
    else:
        loginWindow.ui.state.setText("用户名、密码错误或用户不存在")

def new_user():
    global loginWindow, mainWindow, admin, user
    name = loginWindow.ui.name_edit.text()
    pw = loginWindow.ui.pw_edit.text()
    if name == "" or pw == "":
        loginWindow.ui.state.setText("用户名或密码不能为空")
        return
    if (" " in name) or (" " in pw):
        loginWindow.ui.state.setText("用户名或密码不能包含空格")
        return
    if name.isdigit():
        loginWindow.ui.state.setText("用户名不能为纯数字")
        return
    if admin.new_user(name,pw):
        QMessageBox.information(loginWindow,"注册消息","注册成功")
        return
    else:
        loginWindow.ui.state.setText("用户名已存在")
        return

def show_info(current, previous):
    global mainWindow, user
    if current != None:
        theme = current.text(1)
        if theme == "":
            return
        item = user.get_item(theme)
        mainWindow.ui.theme_edit.setText(item[0])
        mainWindow.ui.name_edit.setText(item[1])
        mainWindow.ui.pw_edit.setText(item[2])
        mainWindow.ui.description_edit.setText(item[3])
        mainWindow.ui.path_edit.setText(item[4])
        types = user.get_item(RESERVED_THEME)[5].split(",")[:-1]
        mainWindow.ui.type_box.clear()
        for each in types:
            mainWindow.ui.type_box.addItem(each)
        mainWindow.ui.type_box.setCurrentText(item[5])

def new_file():
    global mainWindow, user,newWindow
    newWindow = NewWidget()
    item = user.get_item(RESERVED_THEME)
    types = item[5].split(",")[:-1]
    for each in types:
        newWindow.ui.type_box.addItem(each)
    newWindow.ui.ok_btn.clicked.connect(ok)
    newWindow.show()

def ok():
    global user,newWindow
    theme = newWindow.ui.theme_edit.text()
    name = newWindow.ui.name_edit.text()
    pw = newWindow.ui.pw_edit.text()
    if len(user.get_item(theme)):
        QMessageBox.warning(mainWindow, "新建消息", f"主题为{theme}的密码文件已存在！")
        return
    if theme == "" or name == "" or pw == "":
        QMessageBox.warning(mainWindow, "新建消息", "主题、用户名、密码均不能为空")
        return
    if (" " in theme) or (" " in name) or (" " in pw):
        QMessageBox.warning(mainWindow, "新建消息", "主题、用户名、密码均不能包含空格")
        return
    description = newWindow.ui.description_edit.toPlainText()
    path = newWindow.ui.path_edit.text()
    Itype = newWindow.ui.type_box.currentText()
    user.add_item(theme,name,pw,description,path,Itype)
    newWindow.close()
    QMessageBox.information(mainWindow,"新建消息",f"新建主题为{theme}的密码文件成功！")
    refresh_tree()
    clear_input()

def refresh_tree():
    global mainWindow
    items = user.get_all()
    mainWindow.ui.tree.clear()
    types = user.get_item(RESERVED_THEME)[5].split(",")[:-1]
    mainWindow.ui.type_box.clear()
    for each in types:
        mainWindow.ui.type_box.addItem(each)
    mainWindow.ui.type_box.setCurrentText("未分类")
    for each in types:
        top = QTreeWidgetItem([each])
        top.setIcon(0,QIcon(config.type_ico))
        mainWindow.ui.tree.addTopLevelItem(top)
    for item in items:
        try:
            child = QTreeWidgetItem(["",item[0]])
            child.setIcon(0,QIcon(config.file_ico))
            mainWindow.ui.tree.findItems(item[1],Qt.MatchFlag.MatchExactly)[0].addChild(child)
        except Exception as e:
            pass


def remove():
    global mainWindow
    theme = mainWindow.ui.tree.currentItem().text(1)
    if theme == "":
        return
    yes = QMessageBox.warning(mainWindow,"删除消息",f"是否删除主题为{theme}的密码文件",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Cancel)
    if yes == QMessageBox.StandardButton.Ok:
        user.remove_item(theme)
        refresh_tree()
        clear_input()

def update():
    global mainWindow,user
    theme = mainWindow.ui.tree.currentItem().text(1)
    if theme == "":
        return
    yes = QMessageBox.warning(mainWindow, "修改消息", f"是否修改主题为{theme}的密码文件,请注意主题不支持修改", QMessageBox.StandardButton.Ok,
                              QMessageBox.StandardButton.Cancel)
    if yes == QMessageBox.StandardButton.Ok:
        name = mainWindow.ui.name_edit.text()
        pw = mainWindow.ui.pw_edit.text()
        description = mainWindow.ui.description_edit.toPlainText()
        path = mainWindow.ui.path_edit.text()
        Itype = mainWindow.ui.type_box.currentText()
        user.update(theme,NAME=name,PASSWORD=pw,DESCRIPTION=description,PATH=path,TYPE=Itype)
        QMessageBox.information(mainWindow, "修改消息", f"修改主题为{theme}的密码文件成功！")
        refresh_tree()
        clear_input()

def search():
    global mainWindow,user
    keywords = mainWindow.ui.search_edit.text()
    items = user.search(keywords)
    mainWindow.ui.tree.clear()
    types = user.get_item(RESERVED_THEME)[5].split(",")[:-1]
    for each in types:
        top = QTreeWidgetItem([each])
        top.setIcon(0, QIcon(config.type_ico))
        mainWindow.ui.tree.addTopLevelItem(top)
    for item in items:
        try:
            child = QTreeWidgetItem(["", item[0]])
            child.setIcon(0, QIcon(config.file_ico))
            mainWindow.ui.tree.findItems(item[1], Qt.MatchFlag.MatchExactly)[0].addChild(child)
        except Exception as e:
            pass

def start_file():
    global mainWindow,user
    theme = mainWindow.ui.tree.currentItem().text(1)
    if theme == "":
        return
    path = user.get_item(theme)[4]
    try:
        os.startfile(path)
    except FileNotFoundError as e:
        QMessageBox.warning(mainWindow, "打开文件消息", f"主题为{theme}的密码文件,路径{e.filename}错误",
                                  QMessageBox.StandardButton.Ok,
                                  QMessageBox.StandardButton.Cancel)

def choose_file():
    global mainWindow
    path = QFileDialog.getOpenFileName(mainWindow,"选择启动路径", "../", "Exe Files (*.exe)")[0]
    mainWindow.ui.path_edit.setText(path)

def new_type():
    global mainWindow, user, typeWindow
    typeWindow = TypeWidget()
    typeWindow.ui.ok_btn.clicked.connect(ok_type)
    typeWindow.ui.cancel_btn.clicked.connect(cancel_type)
    typeWindow.show()

def remove_type():
    global mainWindow,user
    Itype = mainWindow.ui.tree.currentItem().text(0)
    if Itype == "":
        return
    yes = QMessageBox.warning(mainWindow, "删除消息", f"是否删除分类：{Itype}", QMessageBox.StandardButton.Ok,
                              QMessageBox.StandardButton.Cancel)
    if yes == QMessageBox.StandardButton.Ok:
        if Itype == "未分类":
            QMessageBox.warning(typeWindow, "删除消息", f"“未分类”类别不可删除！")
            return
        user.update_type("未分类",Itype)
        types = user.get_item(RESERVED_THEME)
        Itype = types[5].replace(Itype+",","")
        user.update(RESERVED_THEME,TYPE=Itype)
        refresh_tree()
        clear_input()

def ok_type():
    global typeWindow,user
    Itype = typeWindow.ui.type_edit.text()
    types = user.get_item(RESERVED_THEME)[5]
    if Itype in types:
        QMessageBox.warning(typeWindow, "新建消息", f"分类：{Itype}已存在！")
        return
    Itype = types + Itype + ","
    user.update_type(Itype, types)
    refresh_tree()
    clear_input()
    typeWindow.close()

def cancel_type():
    global typeWindow
    typeWindow.close()

def about():
    global aboutWindow
    aboutWindow = AboutWidget()
    aboutWindow.show()

def show_pw():
    global mainWindow
    if mainWindow.ui.toolShowPW.isChecked() and mainWindow.ui.pw_edit.echoMode() == QLineEdit.Password:
        mainWindow.ui.pw_edit.setEchoMode(QLineEdit.Normal)
    elif not mainWindow.ui.toolShowPW.isChecked() and mainWindow.ui.pw_edit.echoMode() == QLineEdit.Normal:
        mainWindow.ui.pw_edit.setEchoMode(QLineEdit.Password)

def clear_input():
    global mainWindow, user
    mainWindow.ui.theme_edit.clear()
    mainWindow.ui.name_edit.clear()
    mainWindow.ui.pw_edit.clear()
    mainWindow.ui.description_edit.clear()
    mainWindow.ui.path_edit.clear()

def choose_window_theme():
    global mainWindow
    theme = mainWindow.ui.themeGroup.checkedAction().text()
    with open("./src/theme","w") as f:
        f.write(theme)
    QMessageBox.information(mainWindow, "设置消息", f"成功设置窗口主题为{theme}，重启后生效！")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)

    admin = Admin("./src/db/users.db")
    loginWindow = LoginWidget()
    mainWindow = MainWidget()
    if config.WINDOWTHEME == "dark":
        apply_stylesheet(app,theme='dark_teal.xml')
        mainWindow.ui.actiondark.setChecked(True)
    else:
        apply_stylesheet(app, theme='light_teal.xml')
        mainWindow.ui.actionlight.setChecked(True)
    loginWindow.show()

    # 按钮事件绑定
    loginWindow.ui.login_btn.clicked.connect(login)
    loginWindow.ui.new_btn.clicked.connect(new_user)


    mainWindow.ui.tree.currentItemChanged.connect(show_info)
    mainWindow.ui.add.clicked.connect(new_file)
    mainWindow.ui.remove.clicked.connect(remove)
    mainWindow.ui.update.clicked.connect(update)
    mainWindow.ui.search_btn.clicked.connect(search)
    mainWindow.ui.refresh_btn.clicked.connect(refresh_tree)
    mainWindow.ui.start_btn.clicked.connect(start_file)
    mainWindow.ui.choose_btn.clicked.connect(choose_file)
    mainWindow.ui.new_type.clicked.connect(new_type)
    mainWindow.ui.remove_type.clicked.connect(remove_type)
    mainWindow.ui.about_btn.clicked.connect(about)
    mainWindow.ui.actionNewFile.triggered.connect(new_file)
    mainWindow.ui.actionDelFile.triggered.connect(remove)
    mainWindow.ui.actionNewType.triggered.connect(new_type)
    mainWindow.ui.actionDelType.triggered.connect(remove_type)
    mainWindow.ui.actionupdate.triggered.connect(update)
    mainWindow.ui.actionAbout.triggered.connect(about)
    mainWindow.ui.toolShowPW.clicked.connect(show_pw)
    mainWindow.ui.toolClear.clicked.connect(clear_input)
    mainWindow.ui.toolNewFile.clicked.connect(new_file)
    mainWindow.ui.toolNewType.clicked.connect(new_type)
    mainWindow.ui.toolDelFile.clicked.connect(remove)
    mainWindow.ui.toolDelType.clicked.connect(remove_type)
    mainWindow.ui.toolUpdate.clicked.connect(update)
    mainWindow.ui.themeGroup.triggered.connect(choose_window_theme)



    # 展示界面
    # mainWindow.show()

    # loginWindow.close()


    # 结束QApplication
    app.exec()

