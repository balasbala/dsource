# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dsource.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(681, 601)
        self.button_RED = QtWidgets.QCheckBox(form)
        self.button_RED.setGeometry(QtCore.QRect(30, 40, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_RED.setFont(font)
        self.button_RED.setText("")
        self.button_RED.setObjectName("button_RED")
        self.button_GREEN = QtWidgets.QCheckBox(form)
        self.button_GREEN.setGeometry(QtCore.QRect(30, 100, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_GREEN.setFont(font)
        self.button_GREEN.setText("")
        self.button_GREEN.setObjectName("button_GREEN")
        self.button_BLUE = QtWidgets.QCheckBox(form)
        self.button_BLUE.setGeometry(QtCore.QRect(30, 160, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_BLUE.setFont(font)
        self.button_BLUE.setText("")
        self.button_BLUE.setObjectName("button_BLUE")
        self.button_temp = QtWidgets.QPushButton(form)
        self.button_temp.setGeometry(QtCore.QRect(240, 300, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_temp.setFont(font)
        self.button_temp.setObjectName("button_temp")
        self.button_humid = QtWidgets.QPushButton(form)
        self.button_humid.setGeometry(QtCore.QRect(240, 370, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_humid.setFont(font)
        self.button_humid.setObjectName("button_humid")
        self.label_temp = QtWidgets.QLabel(form)
        self.label_temp.setGeometry(QtCore.QRect(190, 300, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp.setFont(font)
        self.label_temp.setObjectName("label_temp")
        self.label_humid = QtWidgets.QLabel(form)
        self.label_humid.setGeometry(QtCore.QRect(190, 380, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_humid.setFont(font)
        self.label_humid.setObjectName("label_humid")
        self.button_refresh = QtWidgets.QPushButton(form)
        self.button_refresh.setGeometry(QtCore.QRect(350, 350, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.button_refresh.setFont(font)
        self.button_refresh.setObjectName("button_refresh")
        self.button_amb_r = QtWidgets.QPushButton(form)
        self.button_amb_r.setGeometry(QtCore.QRect(60, 270, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_amb_r.setFont(font)
        self.button_amb_r.setAutoFillBackground(True)
        self.button_amb_r.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button_amb_r.setObjectName("button_amb_r")
        self.button_amb_g = QtWidgets.QPushButton(form)
        self.button_amb_g.setGeometry(QtCore.QRect(60, 340, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_amb_g.setFont(font)
        self.button_amb_g.setAutoFillBackground(True)
        self.button_amb_g.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button_amb_g.setObjectName("button_amb_g")
        self.button_amb_b = QtWidgets.QPushButton(form)
        self.button_amb_b.setGeometry(QtCore.QRect(60, 410, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_amb_b.setFont(font)
        self.button_amb_b.setAutoFillBackground(True)
        self.button_amb_b.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.button_amb_b.setObjectName("button_amb_b")
        self.label_amb_red = QtWidgets.QLabel(form)
        self.label_amb_red.setGeometry(QtCore.QRect(30, 280, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_amb_red.setFont(font)
        self.label_amb_red.setObjectName("label_amb_red")
        self.label_amb_green = QtWidgets.QLabel(form)
        self.label_amb_green.setGeometry(QtCore.QRect(30, 350, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_amb_green.setFont(font)
        self.label_amb_green.setObjectName("label_amb_green")
        self.label_amb_blue = QtWidgets.QLabel(form)
        self.label_amb_blue.setGeometry(QtCore.QRect(30, 410, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_amb_blue.setFont(font)
        self.label_amb_blue.setObjectName("label_amb_blue")
        self.keypad_1 = QtWidgets.QPushButton(form)
        self.keypad_1.setGeometry(QtCore.QRect(450, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_1.setFont(font)
        self.keypad_1.setObjectName("keypad_1")
        self.keypad_4 = QtWidgets.QPushButton(form)
        self.keypad_4.setGeometry(QtCore.QRect(450, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_4.setFont(font)
        self.keypad_4.setObjectName("keypad_4")
        self.keypad_7 = QtWidgets.QPushButton(form)
        self.keypad_7.setGeometry(QtCore.QRect(450, 380, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_7.setFont(font)
        self.keypad_7.setObjectName("keypad_7")
        self.keypad_star = QtWidgets.QPushButton(form)
        self.keypad_star.setGeometry(QtCore.QRect(450, 440, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_star.setFont(font)
        self.keypad_star.setObjectName("keypad_star")
        self.slider = QtWidgets.QSlider(form)
        self.slider.setGeometry(QtCore.QRect(160, 540, 481, 31))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.label_dac = QtWidgets.QLabel(form)
        self.label_dac.setGeometry(QtCore.QRect(80, 530, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_dac.setFont(font)
        self.label_dac.setObjectName("label_dac")
        self.keypad_5 = QtWidgets.QPushButton(form)
        self.keypad_5.setGeometry(QtCore.QRect(500, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_5.setFont(font)
        self.keypad_5.setObjectName("keypad_5")
        self.keypad_8 = QtWidgets.QPushButton(form)
        self.keypad_8.setGeometry(QtCore.QRect(500, 380, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_8.setFont(font)
        self.keypad_8.setObjectName("keypad_8")
        self.keypad_2 = QtWidgets.QPushButton(form)
        self.keypad_2.setGeometry(QtCore.QRect(500, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_2.setFont(font)
        self.keypad_2.setObjectName("keypad_2")
        self.keypad_0 = QtWidgets.QPushButton(form)
        self.keypad_0.setGeometry(QtCore.QRect(500, 440, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_0.setFont(font)
        self.keypad_0.setObjectName("keypad_0")
        self.keypad_6 = QtWidgets.QPushButton(form)
        self.keypad_6.setGeometry(QtCore.QRect(550, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_6.setFont(font)
        self.keypad_6.setObjectName("keypad_6")
        self.keypad_9 = QtWidgets.QPushButton(form)
        self.keypad_9.setGeometry(QtCore.QRect(550, 380, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_9.setFont(font)
        self.keypad_9.setObjectName("keypad_9")
        self.keypad_3 = QtWidgets.QPushButton(form)
        self.keypad_3.setGeometry(QtCore.QRect(550, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_3.setFont(font)
        self.keypad_3.setObjectName("keypad_3")
        self.keypad_hash = QtWidgets.QPushButton(form)
        self.keypad_hash.setGeometry(QtCore.QRect(550, 440, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_hash.setFont(font)
        self.keypad_hash.setObjectName("keypad_hash")
        self.keypad_b = QtWidgets.QPushButton(form)
        self.keypad_b.setGeometry(QtCore.QRect(600, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_b.setFont(font)
        self.keypad_b.setObjectName("keypad_b")
        self.keypad_c = QtWidgets.QPushButton(form)
        self.keypad_c.setGeometry(QtCore.QRect(600, 380, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_c.setFont(font)
        self.keypad_c.setObjectName("keypad_c")
        self.keypad_a = QtWidgets.QPushButton(form)
        self.keypad_a.setGeometry(QtCore.QRect(600, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_a.setFont(font)
        self.keypad_a.setObjectName("keypad_a")
        self.keypad_d = QtWidgets.QPushButton(form)
        self.keypad_d.setGeometry(QtCore.QRect(600, 440, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keypad_d.setFont(font)
        self.keypad_d.setObjectName("keypad_d")
        self.label_RED = QtWidgets.QLabel(form)
        self.label_RED.setGeometry(QtCore.QRect(50, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_RED.setFont(font)
        self.label_RED.setObjectName("label_RED")
        self.label_GREEN = QtWidgets.QLabel(form)
        self.label_GREEN.setGeometry(QtCore.QRect(50, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_GREEN.setFont(font)
        self.label_GREEN.setObjectName("label_GREEN")
        self.label_BLUE = QtWidgets.QLabel(form)
        self.label_BLUE.setGeometry(QtCore.QRect(50, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_BLUE.setFont(font)
        self.label_BLUE.setObjectName("label_BLUE")
        self.keypadLCD = QtWidgets.QLineEdit(form)
        self.keypadLCD.setGeometry(QtCore.QRect(530, 219, 113, 31))
        self.keypadLCD.setObjectName("keypadLCD")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "PiHAT_UI"))
        self.button_temp.setText(_translate("form", "Temp"))
        self.button_humid.setText(_translate("form", "Humid"))
        self.label_temp.setText(_translate("form", "TEMP-"))
        self.label_humid.setText(_translate("form", "HUMD-"))
        self.button_refresh.setText(_translate("form", "Refresh"))
        self.button_amb_r.setText(_translate("form", "RED"))
        self.button_amb_g.setText(_translate("form", "GREEN"))
        self.button_amb_b.setText(_translate("form", "BLUE"))
        self.label_amb_red.setText(_translate("form", "R"))
        self.label_amb_green.setText(_translate("form", "G"))
        self.label_amb_blue.setText(_translate("form", "B"))
        self.keypad_1.setText(_translate("form", "1"))
        self.keypad_4.setText(_translate("form", "4"))
        self.keypad_7.setText(_translate("form", "7"))
        self.keypad_star.setText(_translate("form", "*"))
        self.label_dac.setText(_translate("form", "DAC"))
        self.keypad_5.setText(_translate("form", "5"))
        self.keypad_8.setText(_translate("form", "8"))
        self.keypad_2.setText(_translate("form", "2"))
        self.keypad_0.setText(_translate("form", "0"))
        self.keypad_6.setText(_translate("form", "6"))
        self.keypad_9.setText(_translate("form", "9"))
        self.keypad_3.setText(_translate("form", "3"))
        self.keypad_hash.setText(_translate("form", "#"))
        self.keypad_b.setText(_translate("form", "B"))
        self.keypad_c.setText(_translate("form", "C"))
        self.keypad_a.setText(_translate("form", "A"))
        self.keypad_d.setText(_translate("form", "D"))
        self.label_RED.setText(_translate("form", "RED"))
        self.label_GREEN.setText(_translate("form", "GREEN"))
        self.label_BLUE.setText(_translate("form", "BLUE"))
