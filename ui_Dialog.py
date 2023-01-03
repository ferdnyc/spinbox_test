# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(183, 207)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spinBox1 = QSpinBox(Dialog)
        self.spinBox1.setObjectName(u"spinBox1")
        self.spinBox1.setMinimumSize(QSize(100, 0))
        self.spinBox1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox1.setMaximum(100)

        self.verticalLayout.addWidget(self.spinBox1)

        self.spinBox2 = QSpinBox(Dialog)
        self.spinBox2.setObjectName(u"spinBox2")
        self.spinBox2.setMinimumSize(QSize(100, 0))
        self.spinBox2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox2.setMaximum(100)

        self.verticalLayout.addWidget(self.spinBox2)

        self.checkUpdateAll = QCheckBox(Dialog)
        self.checkUpdateAll.setObjectName(u"checkUpdateAll")

        self.verticalLayout.addWidget(self.checkUpdateAll)

        self.checkBlock = QCheckBox(Dialog)
        self.checkBlock.setObjectName(u"checkBlock")

        self.verticalLayout.addWidget(self.checkBlock)

        self.labelOutput = QLabel(Dialog)
        self.labelOutput.setObjectName(u"labelOutput")
        self.labelOutput.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelOutput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkUpdateAll.setText(QCoreApplication.translate("Dialog", u"Update all spinboxes", None))
        self.checkBlock.setText(QCoreApplication.translate("Dialog", u"Updates block signals", None))
        self.labelOutput.setText(QCoreApplication.translate("Dialog", u"Box totals: ", None))
    # retranslateUi

