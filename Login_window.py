# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_wind.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(402, 300)
        self.verticalLayout_2 = QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name = QLabel(Login)
        self.name.setObjectName(u"name")
        self.name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.name)

        self.name_edit = QLineEdit(Login)
        self.name_edit.setObjectName(u"name_edit")

        self.horizontalLayout.addWidget(self.name_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pw = QLabel(Login)
        self.pw.setObjectName(u"pw")
        self.pw.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.pw)

        self.pw_edit = QLineEdit(Login)
        self.pw_edit.setObjectName(u"pw_edit")

        self.horizontalLayout_2.addWidget(self.pw_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.state = QLabel(Login)
        self.state.setObjectName(u"state")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state.sizePolicy().hasHeightForWidth())
        self.state.setSizePolicy(sizePolicy)
        self.state.setAlignment(Qt.AlignCenter)
        palette = QPalette()
        palette.setColor(QPalette.WindowText,Qt.red)
        self.state.setPalette(palette)

        self.verticalLayout_2.addWidget(self.state)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.login_btn = QPushButton(Login)
        self.login_btn.setObjectName(u"login_btn")

        self.horizontalLayout_3.addWidget(self.login_btn)

        self.new_btn = QPushButton(Login)
        self.new_btn.setObjectName(u"new_btn")

        self.horizontalLayout_3.addWidget(self.new_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.name.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d", None))
        self.pw.setText(QCoreApplication.translate("Login", u"\u5bc6    \u7801", None))
        self.state.setText("")
        self.login_btn.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.new_btn.setText(QCoreApplication.translate("Login", u"\u65b0\u5efa\u7528\u6237", None))
    # retranslateUi

