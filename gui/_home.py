# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_window_home(object):
    def setupUi(self, window_home):
        if not window_home.objectName():
            window_home.setObjectName(u"window_home")
        window_home.resize(1072, 652)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window_home.sizePolicy().hasHeightForWidth())
        window_home.setSizePolicy(sizePolicy)
        window_home.setMinimumSize(QSize(1072, 652))
        window_home.setMaximumSize(QSize(1072, 652))
        self.root = QWidget(window_home)
        self.root.setObjectName(u"root")
        window_home.setCentralWidget(self.root)
        self.bar_menu = QMenuBar(window_home)
        self.bar_menu.setObjectName(u"bar_menu")
        self.bar_menu.setGeometry(QRect(0, 0, 1072, 34))
        self.menu_close_proj = QMenu(self.bar_menu)
        self.menu_close_proj.setObjectName(u"menu_close_proj")
        self.menu_close_proj.setEnabled(False)
        self.menu_open_proj_dir = QMenu(self.bar_menu)
        self.menu_open_proj_dir.setObjectName(u"menu_open_proj_dir")
        self.menu_open_proj_dir.setEnabled(False)
        self.menu_abt = QMenu(self.bar_menu)
        self.menu_abt.setObjectName(u"menu_abt")
        window_home.setMenuBar(self.bar_menu)
        self.bar_status = QStatusBar(window_home)
        self.bar_status.setObjectName(u"bar_status")
        self.bar_status.setSizeGripEnabled(False)
        window_home.setStatusBar(self.bar_status)

        self.bar_menu.addAction(self.menu_close_proj.menuAction())
        self.bar_menu.addAction(self.menu_open_proj_dir.menuAction())
        self.bar_menu.addAction(self.menu_abt.menuAction())

        self.retranslateUi(window_home)

        QMetaObject.connectSlotsByName(window_home)
    # setupUi

    def retranslateUi(self, window_home):
        window_home.setWindowTitle(QCoreApplication.translate("window_home", u"messimg", None))
        self.menu_close_proj.setTitle(QCoreApplication.translate("window_home", u"\u30d7\u30ed\u30b8\u30a7\u30af\u30c8\u3092\u9589\u3058\u308b", None))
        self.menu_open_proj_dir.setTitle(QCoreApplication.translate("window_home", u"\u30d5\u30a9\u30eb\u30c0\u3092\u8868\u793a", None))
        self.menu_abt.setTitle(QCoreApplication.translate("window_home", u"\u3053\u306e\u30a2\u30d7\u30ea\u306b\u3064\u3044\u3066", None))
    # retranslateUi

