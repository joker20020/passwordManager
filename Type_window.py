# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Type_wind.ui'
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

class Ui_Type(object):
    def setupUi(self, Type):
        if not Type.objectName():
            Type.setObjectName(u"Type")
        Type.resize(400, 134)
        self.verticalLayout = QVBoxLayout(Type)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.type = QLabel(Type)
        self.type.setObjectName(u"type")

        self.horizontalLayout.addWidget(self.type)

        self.type_edit = QLineEdit(Type)
        self.type_edit.setObjectName(u"type_edit")

        self.horizontalLayout.addWidget(self.type_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ok_btn = QPushButton(Type)
        self.ok_btn.setObjectName(u"ok_btn")

        self.horizontalLayout_2.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton(Type)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Type)

        QMetaObject.connectSlotsByName(Type)
    # setupUi

    def retranslateUi(self, Type):
        Type.setWindowTitle(QCoreApplication.translate("Type", u"新建分类", None))
        self.type.setText(QCoreApplication.translate("Type", u"\u521b\u5efa\u5206\u7c7b\u540d\u79f0:", None))
        self.ok_btn.setText(QCoreApplication.translate("Type", u"\u521b\u5efa", None))
        self.cancel_btn.setText(QCoreApplication.translate("Type", u"\u53d6\u6d88", None))
    # retranslateUi

