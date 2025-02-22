# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Base(object):
    def setupUi(self, Base):
        Base.setObjectName("Base")
        Base.resize(999, 863)
        Base.setWindowTitle("")
        Base.setStyleSheet("QWidget{\n"
"    background-color : rgb(221, 223, 237)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Base)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(140, 10, 631, 631))
        self.photo.setStyleSheet("")
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(820, 0, 231, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbbright = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pbbright.setFont(font)
        self.pbbright.setStyleSheet("")
        self.pbbright.setObjectName("pbbright")
        self.verticalLayout.addWidget(self.pbbright)
        self.pbcontrast = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbcontrast.setFont(font)
        self.pbcontrast.setObjectName("pbcontrast")
        self.verticalLayout.addWidget(self.pbcontrast)
        self.pbsaturation = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbsaturation.setFont(font)
        self.pbsaturation.setObjectName("pbsaturation")
        self.verticalLayout.addWidget(self.pbsaturation)
        self.pbred = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbred.setFont(font)
        self.pbred.setObjectName("pbred")
        self.verticalLayout.addWidget(self.pbred)
        self.pbblue = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbblue.setFont(font)
        self.pbblue.setObjectName("pbblue")
        self.verticalLayout.addWidget(self.pbblue)
        self.pbgreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbgreen.setFont(font)
        self.pbgreen.setObjectName("pbgreen")
        self.verticalLayout.addWidget(self.pbgreen)
        self.pbsharpness = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbsharpness.setFont(font)
        self.pbsharpness.setObjectName("pbsharpness")
        self.verticalLayout.addWidget(self.pbsharpness)
        self.pbfilters = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbfilters.setFont(font)
        self.pbfilters.setObjectName("pbfilters")
        self.verticalLayout.addWidget(self.pbfilters)
        self.pbreflect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbreflect.setFont(font)
        self.pbreflect.setObjectName("pbreflect")
        self.verticalLayout.addWidget(self.pbreflect)
        self.pbturn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbturn.setFont(font)
        self.pbturn.setObjectName("pbturn")
        self.verticalLayout.addWidget(self.pbturn)
        self.pbsize = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        self.pbsize.setFont(font)
        self.pbsize.setObjectName("pbsize")
        self.verticalLayout.addWidget(self.pbsize)
        self.rofcontrast = QtWidgets.QSlider(self.centralwidget)
        self.rofcontrast.setGeometry(QtCore.QRect(70, 710, 851, 61))
        self.rofcontrast.setMinimum(20)
        self.rofcontrast.setMaximum(180)
        self.rofcontrast.setSingleStep(1)
        self.rofcontrast.setPageStep(1)
        self.rofcontrast.setProperty("value", 100)
        self.rofcontrast.setOrientation(QtCore.Qt.Horizontal)
        self.rofcontrast.setObjectName("rofcontrast")
        self.nameofr = QtWidgets.QLabel(self.centralwidget)
        self.nameofr.setGeometry(QtCore.QRect(50, 660, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Aparajita")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.nameofr.setFont(font)
        self.nameofr.setText("")
        self.nameofr.setObjectName("nameofr")
        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setGeometry(QtCore.QRect(620, 770, 75, 23))
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QPushButton(self.centralwidget)
        self.no.setGeometry(QtCore.QRect(730, 770, 75, 23))
        self.no.setObjectName("no")
        self.rofbright = QtWidgets.QSlider(self.centralwidget)
        self.rofbright.setGeometry(QtCore.QRect(70, 710, 851, 61))
        self.rofbright.setMinimum(20)
        self.rofbright.setMaximum(180)
        self.rofbright.setProperty("value", 100)
        self.rofbright.setOrientation(QtCore.Qt.Horizontal)
        self.rofbright.setObjectName("rofbright")
        self.rofsat = QtWidgets.QSlider(self.centralwidget)
        self.rofsat.setGeometry(QtCore.QRect(70, 710, 851, 61))
        self.rofsat.setMinimum(20)
        self.rofsat.setMaximum(180)
        self.rofsat.setProperty("value", 100)
        self.rofsat.setOrientation(QtCore.Qt.Horizontal)
        self.rofsat.setObjectName("rofsat")
        self.textred = QtWidgets.QLabel(self.centralwidget)
        self.textred.setGeometry(QtCore.QRect(170, 700, 81, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textred.setFont(font)
        self.textred.setObjectName("textred")
        self.textgreen = QtWidgets.QLabel(self.centralwidget)
        self.textgreen.setGeometry(QtCore.QRect(180, 700, 81, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textgreen.setFont(font)
        self.textgreen.setObjectName("textgreen")
        self.textblue = QtWidgets.QLabel(self.centralwidget)
        self.textblue.setGeometry(QtCore.QRect(180, 700, 111, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textblue.setFont(font)
        self.textblue.setObjectName("textblue")
        self.rofred = QtWidgets.QSlider(self.centralwidget)
        self.rofred.setGeometry(QtCore.QRect(50, 730, 291, 20))
        self.rofred.setMinimum(-100)
        self.rofred.setMaximum(100)
        self.rofred.setOrientation(QtCore.Qt.Horizontal)
        self.rofred.setObjectName("rofred")
        self.rofgreen = QtWidgets.QSlider(self.centralwidget)
        self.rofgreen.setGeometry(QtCore.QRect(50, 730, 291, 20))
        self.rofgreen.setMinimum(-100)
        self.rofgreen.setMaximum(100)
        self.rofgreen.setOrientation(QtCore.Qt.Horizontal)
        self.rofgreen.setObjectName("rofgreen")
        self.rofblue = QtWidgets.QSlider(self.centralwidget)
        self.rofblue.setGeometry(QtCore.QRect(60, 730, 281, 20))
        self.rofblue.setMinimum(-100)
        self.rofblue.setMaximum(100)
        self.rofblue.setOrientation(QtCore.Qt.Horizontal)
        self.rofblue.setObjectName("rofblue")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(410, 702, 71, 21))
        self.ok.setObjectName("ok")
        self.top = QtWidgets.QLineEdit(self.centralwidget)
        self.top.setGeometry(QtCore.QRect(410, 680, 71, 21))
        self.top.setStyleSheet("QLineEdit{\n"
"    background-color : rgb(255, 255, 255)\n"
"}")
        self.top.setObjectName("top")
        self.left = QtWidgets.QLineEdit(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(350, 700, 61, 20))
        self.left.setStyleSheet("QLineEdit{\n"
"    background-color : rgb(255, 255, 255)\n"
"}\n"
"")
        self.left.setObjectName("left")
        self.right = QtWidgets.QLineEdit(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(480, 700, 61, 20))
        self.right.setStyleSheet("QLineEdit{\n"
"    background-color : rgb(255, 255, 255)\n"
"}")
        self.right.setObjectName("right")
        self.bottom = QtWidgets.QLineEdit(self.centralwidget)
        self.bottom.setGeometry(QtCore.QRect(410, 720, 71, 20))
        self.bottom.setStyleSheet("QLineEdit{\n"
"    background-color : rgb(255, 255, 255)\n"
"}")
        self.bottom.setObjectName("bottom")
        self.rofsharpness = QtWidgets.QSlider(self.centralwidget)
        self.rofsharpness.setGeometry(QtCore.QRect(70, 690, 861, 51))
        self.rofsharpness.setMinimum(0)
        self.rofsharpness.setMaximum(200)
        self.rofsharpness.setProperty("value", 100)
        self.rofsharpness.setOrientation(QtCore.Qt.Horizontal)
        self.rofsharpness.setObjectName("rofsharpness")
        self.horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.horizontal.setGeometry(QtCore.QRect(330, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.horizontal.setFont(font)
        self.horizontal.setObjectName("horizontal")
        self.vertical = QtWidgets.QPushButton(self.centralwidget)
        self.vertical.setGeometry(QtCore.QRect(480, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vertical.setFont(font)
        self.vertical.setObjectName("vertical")
        self.turnl = QtWidgets.QPushButton(self.centralwidget)
        self.turnl.setGeometry(QtCore.QRect(330, 712, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.turnl.setFont(font)
        self.turnl.setObjectName("turnl")
        self.turnr = QtWidgets.QPushButton(self.centralwidget)
        self.turnr.setGeometry(QtCore.QRect(480, 712, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.turnr.setFont(font)
        self.turnr.setObjectName("turnr")
        self.filterbw = QtWidgets.QPushButton(self.centralwidget)
        self.filterbw.setGeometry(QtCore.QRect(110, 690, 75, 23))
        self.filterbw.setObjectName("filterbw")
        self.stf = QtWidgets.QPushButton(self.centralwidget)
        self.stf.setGeometry(QtCore.QRect(110, 750, 75, 23))
        self.stf.setObjectName("stf")
        self.fcontour = QtWidgets.QPushButton(self.centralwidget)
        self.fcontour.setGeometry(QtCore.QRect(230, 690, 75, 23))
        self.fcontour.setObjectName("fcontour")
        self.femboss = QtWidgets.QPushButton(self.centralwidget)
        self.femboss.setGeometry(QtCore.QRect(230, 750, 75, 23))
        self.femboss.setObjectName("femboss")
        self.frank = QtWidgets.QPushButton(self.centralwidget)
        self.frank.setGeometry(QtCore.QRect(350, 690, 75, 23))
        self.frank.setObjectName("frank")
        self.funsharp = QtWidgets.QPushButton(self.centralwidget)
        self.funsharp.setGeometry(QtCore.QRect(350, 750, 75, 23))
        self.funsharp.setObjectName("funsharp")
        self.fmode = QtWidgets.QPushButton(self.centralwidget)
        self.fmode.setGeometry(QtCore.QRect(470, 690, 75, 23))
        self.fmode.setObjectName("fmode")
        self.linef = QtWidgets.QPushButton(self.centralwidget)
        self.linef.setGeometry(QtCore.QRect(470, 750, 75, 23))
        self.linef.setObjectName("linef")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 77, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.back = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.verticalLayout_2.addWidget(self.back)
        self.pbopen = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(10)
        self.pbopen.setFont(font)
        self.pbopen.setObjectName("pbopen")
        self.verticalLayout_2.addWidget(self.pbopen)
        self.pbsave = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(10)
        self.pbsave.setFont(font)
        self.pbsave.setObjectName("pbsave")
        self.verticalLayout_2.addWidget(self.pbsave)
        self.ok.raise_()
        self.vertical.raise_()
        self.turnr.raise_()
        self.horizontal.raise_()
        self.turnl.raise_()
        self.rofcontrast.raise_()
        self.rofsharpness.raise_()
        self.rofbright.raise_()
        self.rofsat.raise_()
        self.right.raise_()
        self.fmode.raise_()
        self.left.raise_()
        self.frank.raise_()
        self.top.raise_()
        self.bottom.raise_()
        self.photo.raise_()
        self.verticalLayoutWidget.raise_()
        self.nameofr.raise_()
        self.yes.raise_()
        self.no.raise_()
        self.textred.raise_()
        self.textgreen.raise_()
        self.textblue.raise_()
        self.rofred.raise_()
        self.rofgreen.raise_()
        self.rofblue.raise_()
        self.filterbw.raise_()
        self.stf.raise_()
        self.fcontour.raise_()
        self.femboss.raise_()
        self.funsharp.raise_()
        self.linef.raise_()
        self.verticalLayoutWidget_2.raise_()
        Base.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Base)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 21))
        self.menubar.setObjectName("menubar")
        Base.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Base)
        self.statusbar.setObjectName("statusbar")
        Base.setStatusBar(self.statusbar)

        self.retranslateUi(Base)
        QtCore.QMetaObject.connectSlotsByName(Base)

    def retranslateUi(self, Base):
        _translate = QtCore.QCoreApplication.translate
        self.pbbright.setText(_translate("Base", "Яркость"))
        self.pbcontrast.setText(_translate("Base", "Контрастность"))
        self.pbsaturation.setText(_translate("Base", "Насыщенность"))
        self.pbred.setText(_translate("Base", "Красный"))
        self.pbblue.setText(_translate("Base", "Синий"))
        self.pbgreen.setText(_translate("Base", "Зеленый"))
        self.pbsharpness.setText(_translate("Base", "Резкость"))
        self.pbfilters.setText(_translate("Base", "Фильтры"))
        self.pbreflect.setText(_translate("Base", "Отразить"))
        self.pbturn.setText(_translate("Base", "Повернуть"))
        self.pbsize.setText(_translate("Base", "Обрезать"))
        self.yes.setText(_translate("Base", "сохранить"))
        self.no.setText(_translate("Base", "отмена"))
        self.textred.setText(_translate("Base", "Красный"))
        self.textgreen.setText(_translate("Base", "Зеленый"))
        self.textblue.setText(_translate("Base", "Синий"))
        self.ok.setText(_translate("Base", "ok"))
        self.horizontal.setText(_translate("Base", "горизонтально"))
        self.vertical.setText(_translate("Base", "вертикально"))
        self.turnl.setText(_translate("Base", "влево"))
        self.turnr.setText(_translate("Base", "вправо"))
        self.filterbw.setText(_translate("Base", "Черно-белый"))
        self.stf.setText(_translate("Base", "Filter 1"))
        self.fcontour.setText(_translate("Base", "Контур"))
        self.femboss.setText(_translate("Base", "Тиснение"))
        self.frank.setText(_translate("Base", "Rank"))
        self.funsharp.setText(_translate("Base", "Нерезкий"))
        self.fmode.setText(_translate("Base", "Mode"))
        self.linef.setText(_translate("Base", "Filter 2"))
        self.back.setText(_translate("Base", "Меню"))
        self.pbopen.setText(_translate("Base", "Открыть"))
        self.pbsave.setText(_translate("Base", "Сохранить"))
