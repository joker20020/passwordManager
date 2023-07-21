# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_wind2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QActionGroup, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QToolBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget,QToolButton)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(787, 558)
        self.actionupdate = QAction(Main)
        self.actionupdate.setObjectName(u"actionupdate")
        self.actionNewType = QAction(Main)
        self.actionNewType.setObjectName(u"actionNewType")
        self.actionNewFile = QAction(Main)
        self.actionNewFile.setObjectName(u"actionNewFile")
        self.actionDelType = QAction(Main)
        self.actionDelType.setObjectName(u"actionDelType")
        self.actionDelFile = QAction(Main)
        self.actionDelFile.setObjectName(u"actionDelFile")
        self.actionAbout = QAction(Main)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actiondark = QAction(Main)
        self.actiondark.setObjectName(u"actiondark")
        self.actiondark.setCheckable(True)
        self.actionlight = QAction(Main)
        self.themeGroup =QActionGroup(Main)
        self.themeGroup.addAction(self.actiondark)
        self.themeGroup.addAction(self.actionlight)
        self.actionlight.setObjectName(u"actionlight")
        self.actionlight.setCheckable(True)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Right = QVBoxLayout()
        self.Right.setObjectName(u"Right")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.theme = QLabel(self.centralwidget)
        self.theme.setObjectName(u"theme")

        self.horizontalLayout_6.addWidget(self.theme)

        self.theme_edit = QLineEdit(self.centralwidget)
        self.theme_edit.setObjectName(u"theme_edit")

        self.horizontalLayout_6.addWidget(self.theme_edit)


        self.Right.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")

        self.horizontalLayout.addWidget(self.name)

        self.name_edit = QLineEdit(self.centralwidget)
        self.name_edit.setObjectName(u"name_edit")

        self.horizontalLayout.addWidget(self.name_edit)


        self.Right.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pw = QLabel(self.centralwidget)
        self.pw.setObjectName(u"pw")

        self.horizontalLayout_3.addWidget(self.pw)

        self.pw_edit = QLineEdit(self.centralwidget)
        self.pw_edit.setObjectName(u"pw_edit")
        self.pw_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.pw_edit)


        self.Right.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.type = QLabel(self.centralwidget)
        self.type.setObjectName(u"type")

        self.horizontalLayout_10.addWidget(self.type)

        self.type_box = QComboBox(self.centralwidget)
        self.type_box.setObjectName(u"type_box")

        self.horizontalLayout_10.addWidget(self.type_box)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.Right.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.path = QLabel(self.centralwidget)
        self.path.setObjectName(u"path")

        self.horizontalLayout_7.addWidget(self.path)

        self.path_edit = QLineEdit(self.centralwidget)
        self.path_edit.setObjectName(u"path_edit")

        self.horizontalLayout_7.addWidget(self.path_edit)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_7.addWidget(self.start_btn)

        self.choose_btn = QPushButton(self.centralwidget)
        self.choose_btn.setObjectName(u"choose_btn")

        self.horizontalLayout_7.addWidget(self.choose_btn)


        self.Right.addLayout(self.horizontalLayout_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.description = QLabel(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.description)

        self.description_edit = QTextEdit(self.centralwidget)
        self.description_edit.setObjectName(u"description_edit")
        self.description_edit.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.description_edit)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.about_btn = QPushButton(self.centralwidget)
        self.about_btn.setObjectName(u"about_btn")

        self.horizontalLayout_8.addWidget(self.about_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.Right.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.Right)

        self.Left = QVBoxLayout()
        self.Left.setObjectName(u"Left")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.search_edit = QLineEdit(self.centralwidget)
        self.search_edit.setObjectName(u"search_edit")

        self.horizontalLayout_5.addWidget(self.search_edit)

        self.search_btn = QPushButton(self.centralwidget)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout_5.addWidget(self.search_btn)

        self.refresh_btn = QPushButton(self.centralwidget)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout_5.addWidget(self.refresh_btn)


        self.Left.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.new_type = QPushButton(self.centralwidget)
        self.new_type.setObjectName(u"new_type")

        self.horizontalLayout_9.addWidget(self.new_type)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.remove_type = QPushButton(self.centralwidget)
        self.remove_type.setObjectName(u"remove_type")

        self.horizontalLayout_9.addWidget(self.remove_type)


        self.Left.addLayout(self.horizontalLayout_9)

        self.tree = QTreeWidget(self.centralwidget)
        self.tree.setObjectName(u"tree")

        self.Left.addWidget(self.tree)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add = QPushButton(self.centralwidget)
        self.add.setObjectName(u"add")

        self.horizontalLayout_4.addWidget(self.add)

        self.remove = QPushButton(self.centralwidget)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout_4.addWidget(self.remove)

        self.update = QPushButton(self.centralwidget)
        self.update.setObjectName(u"update")

        self.horizontalLayout_4.addWidget(self.update)


        self.Left.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.Left)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 787, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.menuDel = QMenu(self.menuFile)
        self.menuDel.setObjectName(u"menuDel")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuTheme = QMenu(self.menuSetting)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Main.setMenuBar(self.menubar)
        self.toolBar = QToolBar(Main)
        self.toolBar.setObjectName(u"toolBar")

        self.toolShowPW = QToolButton(self.toolBar)
        self.toolShowPW.setCheckable(True)
        self.toolShowPW.setToolTip("显示密码")
        self.toolShowPW.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolShowPW)

        self.toolClear = QToolButton(self.toolBar)
        self.toolClear.setToolTip("清空所有输入")
        self.toolClear.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolClear)

        self.toolNewFile = QToolButton(self.toolBar)
        self.toolNewFile.setToolTip("新建密码文件")
        self.toolNewFile.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolNewFile)

        self.toolNewType = QToolButton(self.toolBar)
        self.toolNewType.setToolTip("新建分类")
        self.toolNewType.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolNewType)

        self.toolDelFile = QToolButton(self.toolBar)
        self.toolDelFile.setToolTip("删除当前密码文件")
        self.toolDelFile.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolDelFile)

        self.toolDelType = QToolButton(self.toolBar)
        self.toolDelType.setToolTip("删除当前分类")
        self.toolDelType.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolDelType)

        self.toolUpdate = QToolButton(self.toolBar)
        self.toolUpdate.setToolTip("修改当前密码文件")
        self.toolUpdate.setToolTipDuration(3000)
        self.toolBar.addWidget(self.toolUpdate)

        Main.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuDel.menuAction())
        self.menuFile.addAction(self.actionupdate)
        self.menuNew.addAction(self.actionNewType)
        self.menuNew.addAction(self.actionNewFile)
        self.menuDel.addAction(self.actionDelType)
        self.menuDel.addAction(self.actionDelFile)
        self.menuSetting.addAction(self.menuTheme.menuAction())
        self.menuTheme.addAction(self.actiondark)
        self.menuTheme.addAction(self.actionlight)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\u5bc6\u7801\u7ba1\u7406\u5668", None))
        self.actionupdate.setText(QCoreApplication.translate("Main", u"\u4fee\u6539", None))
        self.actionNewType.setText(QCoreApplication.translate("Main", u"\u65b0\u5efa\u5206\u7c7b", None))
#if QT_CONFIG(shortcut)
        self.actionNewType.setShortcut(QCoreApplication.translate("Main", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionNewFile.setText(QCoreApplication.translate("Main", u"\u65b0\u5efa\u5bc6\u7801\u6587\u4ef6", None))
#if QT_CONFIG(shortcut)
        self.actionNewFile.setShortcut(QCoreApplication.translate("Main", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelType.setText(QCoreApplication.translate("Main", u"\u5220\u9664\u5206\u7c7b", None))
#if QT_CONFIG(shortcut)
        self.actionDelType.setShortcut(QCoreApplication.translate("Main", u"Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelFile.setText(QCoreApplication.translate("Main", u"\u5220\u9664\u5bc6\u7801\u6587\u4ef6", None))
#if QT_CONFIG(shortcut)
        self.actionDelFile.setShortcut(QCoreApplication.translate("Main", u"Shift+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("Main", u"\u5173\u4e8e", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("Main", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actiondark.setText(QCoreApplication.translate("Main", u"dark", None))
        self.actionlight.setText(QCoreApplication.translate("Main", u"light", None))
        self.theme.setText(QCoreApplication.translate("Main", u"\u4e3b    \u9898\uff1a", None))
        self.name.setText(QCoreApplication.translate("Main", u"\u7528\u6237\u540d\uff1a", None))
        self.pw.setText(QCoreApplication.translate("Main", u"\u5bc6    \u7801\uff1a", None))
        self.type.setText(QCoreApplication.translate("Main", u"\u5206    \u7c7b\uff1a", None))
        self.path.setText(QCoreApplication.translate("Main", u"\u8def    \u5f84\uff1a", None))
        self.start_btn.setText(QCoreApplication.translate("Main", u"\u6253\u5f00", None))
        self.choose_btn.setText(QCoreApplication.translate("Main", u"\u9009\u62e9\u542f\u52a8\u8def\u5f84", None))
        self.description.setText(QCoreApplication.translate("Main", u"\u63cf\u8ff0", None))
        self.description_edit.setPlaceholderText("")
        self.about_btn.setText(QCoreApplication.translate("Main", u"\u5173\u4e8e", None))
        self.search_btn.setText(QCoreApplication.translate("Main", u"\u641c\u7d22", None))
        self.refresh_btn.setText("")
        self.new_type.setText(QCoreApplication.translate("Main", u"\u65b0\u5efa\u5206\u7c7b", None))
        self.remove_type.setText(QCoreApplication.translate("Main", u"\u5220\u9664\u5206\u7c7b", None))
        ___qtreewidgetitem = self.tree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Main", u"\u4e3b\u9898", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Main", u"\u5206\u7c7b", None));
        self.add.setText(QCoreApplication.translate("Main", u"\u65b0\u589e", None))
        self.remove.setText(QCoreApplication.translate("Main", u"\u5220\u9664", None))
        self.update.setText(QCoreApplication.translate("Main", u"\u4fee\u6539", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"\u6587\u4ef6", None))
        self.menuNew.setTitle(QCoreApplication.translate("Main", u"\u65b0\u5efa", None))
        self.menuDel.setTitle(QCoreApplication.translate("Main", u"\u5220\u9664", None))
        self.menuSetting.setTitle(QCoreApplication.translate("Main", u"\u8bbe\u7f6e", None))
        self.menuTheme.setTitle(QCoreApplication.translate("Main", u"选择窗口主题", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Main", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Main", u"toolBar", None))
    # retranslateUi

