# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'New_wind.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_New(object):
    def setupUi(self, New):
        if not New.objectName():
            New.setObjectName(u"New")
        New.resize(400, 300)
        self.verticalLayout = QVBoxLayout(New)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.theme = QLabel(New)
        self.theme.setObjectName(u"theme")
        self.theme.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.theme)

        self.theme_edit = QLineEdit(New)
        self.theme_edit.setObjectName(u"theme_edit")

        self.horizontalLayout.addWidget(self.theme_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name = QLabel(New)
        self.name.setObjectName(u"name")
        self.name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.name)

        self.name_edit = QLineEdit(New)
        self.name_edit.setObjectName(u"name_edit")

        self.horizontalLayout_2.addWidget(self.name_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pw = QLabel(New)
        self.pw.setObjectName(u"pw")
        self.pw.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.pw)

        self.pw_edit = QLineEdit(New)
        self.pw_edit.setObjectName(u"pw_edit")

        self.horizontalLayout_3.addWidget(self.pw_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.path = QLabel(New)
        self.path.setObjectName(u"path")

        self.horizontalLayout_5.addWidget(self.path)

        self.path_edit = QLineEdit(New)
        self.path_edit.setObjectName(u"path_edit")

        self.horizontalLayout_5.addWidget(self.path_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.type = QLabel(New)
        self.type.setObjectName(u"type")

        self.horizontalLayout_6.addWidget(self.type)

        self.type_box = QComboBox(New)
        self.type_box.setObjectName(u"type_box")

        self.horizontalLayout_6.addWidget(self.type_box)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.description = QLabel(New)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.description)

        self.description_edit = QTextEdit(New)
        self.description_edit.setObjectName(u"description_edit")

        self.verticalLayout_2.addWidget(self.description_edit)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.ok_btn = QPushButton(New)
        self.ok_btn.setObjectName(u"ok_btn")

        self.horizontalLayout_4.addWidget(self.ok_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(New)

        QMetaObject.connectSlotsByName(New)
    # setupUi

    def retranslateUi(self, New):
        New.setWindowTitle(QCoreApplication.translate("New", u"\u65b0\u5efa", None))
        self.theme.setText(QCoreApplication.translate("New", u"\u4e3b    \u9898\uff1a", None))
        self.name.setText(QCoreApplication.translate("New", u"\u7528\u6237\u540d\uff1a", None))
        self.pw.setText(QCoreApplication.translate("New", u"\u5bc6    \u7801\uff1a", None))
        self.path.setText(QCoreApplication.translate("New", u"\u8def    \u5f84\uff1a", None))
        self.path_edit.setPlaceholderText(QCoreApplication.translate("New", u"\u975e\u5fc5\u586b\u9879", None))
        self.type.setText(QCoreApplication.translate("New", u"\u5206\u7c7b\uff1a", None))
        self.description.setText(QCoreApplication.translate("New", u"\u63cf\u8ff0", None))
        self.description_edit.setPlaceholderText(QCoreApplication.translate("New", u"\u975e\u5fc5\u586b\u9879", None))
        self.ok_btn.setText(QCoreApplication.translate("New", u"\u786e\u5b9a", None))
    # retranslateUi

