# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizard.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QToolButton, QWidget)

class Ui_widget_wizard(object):
    def setupUi(self, widget_wizard):
        if not widget_wizard.objectName():
            widget_wizard.setObjectName(u"widget_wizard")
        widget_wizard.resize(1072, 592)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_wizard.sizePolicy().hasHeightForWidth())
        widget_wizard.setSizePolicy(sizePolicy)
        widget_wizard.setMinimumSize(QSize(1072, 592))
        widget_wizard.setMaximumSize(QSize(1072, 592))
        self.listview_recent_proj_hist = QListView(widget_wizard)
        self.listview_recent_proj_hist.setObjectName(u"listview_recent_proj_hist")
        self.listview_recent_proj_hist.setGeometry(QRect(360, 270, 361, 211))
        self.btn_create_new_project = QPushButton(widget_wizard)
        self.btn_create_new_project.setObjectName(u"btn_create_new_project")
        self.btn_create_new_project.setGeometry(QRect(120, 290, 191, 38))
        self.btn_open_existing_proj = QPushButton(widget_wizard)
        self.btn_open_existing_proj.setObjectName(u"btn_open_existing_proj")
        self.btn_open_existing_proj.setGeometry(QRect(120, 360, 191, 38))
        self.btn_clear_recent_proj_hist = QToolButton(widget_wizard)
        self.btn_clear_recent_proj_hist.setObjectName(u"btn_clear_recent_proj_hist")
        self.btn_clear_recent_proj_hist.setGeometry(QRect(640, 220, 81, 38))
        self.label_title_welcome = QLabel(widget_wizard)
        self.label_title_welcome.setObjectName(u"label_title_welcome")
        self.label_title_welcome.setGeometry(QRect(0, 81, 1071, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title_welcome.setFont(font)
        self.label_title_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_welcome_desc = QLabel(widget_wizard)
        self.label_welcome_desc.setObjectName(u"label_welcome_desc")
        self.label_welcome_desc.setGeometry(QRect(0, 120, 1071, 41))
        self.label_welcome_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title_recent_proj_hist = QLabel(widget_wizard)
        self.label_title_recent_proj_hist.setObjectName(u"label_title_recent_proj_hist")
        self.label_title_recent_proj_hist.setGeometry(QRect(360, 230, 221, 22))
        font1 = QFont()
        font1.setBold(True)
        self.label_title_recent_proj_hist.setFont(font1)
        self.label_title_help = QLabel(widget_wizard)
        self.label_title_help.setObjectName(u"label_title_help")
        self.label_title_help.setGeometry(QRect(770, 250, 81, 22))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_title_help.setFont(font2)
        self.label_clickable_open_homepage = QLabel(widget_wizard)
        self.label_clickable_open_homepage.setObjectName(u"label_clickable_open_homepage")
        self.label_clickable_open_homepage.setGeometry(QRect(770, 290, 161, 22))
        font3 = QFont()
        font3.setItalic(True)
        font3.setUnderline(True)
        self.label_clickable_open_homepage.setFont(font3)
        self.label_clickable_open_homepage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_clickable_open_handbook = QLabel(widget_wizard)
        self.label_clickable_open_handbook.setObjectName(u"label_clickable_open_handbook")
        self.label_clickable_open_handbook.setGeometry(QRect(770, 330, 161, 22))
        self.label_clickable_open_handbook.setFont(font3)
        self.label_clickable_open_handbook.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(widget_wizard)

        QMetaObject.connectSlotsByName(widget_wizard)
    # setupUi

    def retranslateUi(self, widget_wizard):
        widget_wizard.setWindowTitle(QCoreApplication.translate("widget_wizard", u"\u3088\u3046\u3053\u305d", None))
        self.btn_create_new_project.setText(QCoreApplication.translate("widget_wizard", u"\u65b0\u3057\u3044\u30d7\u30ed\u30b8\u30a7\u30af\u30c8", None))
        self.btn_open_existing_proj.setText(QCoreApplication.translate("widget_wizard", u"\u30d7\u30ed\u30b8\u30a7\u30af\u30c8\u3092\u958b\u304f...", None))
        self.btn_clear_recent_proj_hist.setText(QCoreApplication.translate("widget_wizard", u"\u30af\u30ea\u30a2", None))
        self.label_title_welcome.setText(QCoreApplication.translate("widget_wizard", u"messimg \u3078\u3088\u3046\u3053\u305d", None))
        self.label_welcome_desc.setText(QCoreApplication.translate("widget_wizard", u"Android ROM \u306e\u7de8\u96c6\u30c4\u30fc\u30eb", None))
        self.label_title_recent_proj_hist.setText(QCoreApplication.translate("widget_wizard", u"\u6700\u8fd1\u306e\u30d7\u30ed\u30b8\u30a7\u30af\u30c8\uff1a", None))
        self.label_title_help.setText(QCoreApplication.translate("widget_wizard", u"\u30d8\u30eb\u30d7", None))
        self.label_clickable_open_homepage.setText(QCoreApplication.translate("widget_wizard", u"\u30db\u30fc\u30e0\u30da\u30fc\u30b8\u3092\u958b\u304f", None))
        self.label_clickable_open_handbook.setText(QCoreApplication.translate("widget_wizard", u"\u30cf\u30f3\u30c9\u30d6\u30c3\u30af\u3092\u8aad\u3080", None))
    # retranslateUi

