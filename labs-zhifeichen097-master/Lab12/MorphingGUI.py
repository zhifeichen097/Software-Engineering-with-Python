# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MorphingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(975, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gfxRight = QtWidgets.QGraphicsView(self.centralwidget)
        self.gfxRight.setEnabled(True)
        self.gfxRight.setGeometry(QtCore.QRect(530, 50, 400, 300))
        self.gfxRight.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gfxRight.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gfxRight.setObjectName("gfxRight")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 360, 120, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gfxBlendImg = QtWidgets.QGraphicsView(self.centralwidget)
        self.gfxBlendImg.setGeometry(QtCore.QRect(280, 430, 400, 300))
        self.gfxBlendImg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gfxBlendImg.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gfxBlendImg.setObjectName("gfxBlendImg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 750, 120, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnBlend = QtWidgets.QPushButton(self.centralwidget)
        self.btnBlend.setEnabled(False)
        self.btnBlend.setGeometry(QtCore.QRect(430, 770, 90, 27))
        self.btnBlend.setObjectName("btnBlend")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 395, 40, 17))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.txtAlpha = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAlpha.setEnabled(False)
        self.txtAlpha.setGeometry(QtCore.QRect(880, 390, 50, 27))
        self.txtAlpha.setMaximumSize(QtCore.QSize(50, 27))
        self.txtAlpha.setMouseTracking(True)
        self.txtAlpha.setInputMask("")
        self.txtAlpha.setAlignment(QtCore.Qt.AlignCenter)
        self.txtAlpha.setReadOnly(True)
        self.txtAlpha.setObjectName("txtAlpha")
        self.sliderAlpha = QtWidgets.QSlider(self.centralwidget)
        self.sliderAlpha.setEnabled(False)
        self.sliderAlpha.setGeometry(QtCore.QRect(60, 390, 810, 24))
        self.sliderAlpha.setMaximum(20)
        self.sliderAlpha.setPageStep(10)
        self.sliderAlpha.setProperty("value", 0)
        self.sliderAlpha.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAlpha.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderAlpha.setTickInterval(2)
        self.sliderAlpha.setObjectName("sliderAlpha")
        self.Min = QtWidgets.QLabel(self.centralwidget)
        self.Min.setGeometry(QtCore.QRect(60, 420, 20, 17))
        self.Min.setAlignment(QtCore.Qt.AlignCenter)
        self.Min.setObjectName("Min")
        self.Max = QtWidgets.QLabel(self.centralwidget)
        self.Max.setGeometry(QtCore.QRect(850, 420, 20, 17))
        self.Max.setAlignment(QtCore.Qt.AlignCenter)
        self.Max.setObjectName("Max")
        self.gfxLeft = QtWidgets.QGraphicsView(self.centralwidget)
        self.gfxLeft.setGeometry(QtCore.QRect(50, 50, 400, 300))
        self.gfxLeft.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gfxLeft.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gfxLeft.setObjectName("gfxLeft")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 360, 120, 17))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnStartImg = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartImg.setGeometry(QtCore.QRect(50, 10, 165, 27))
        self.btnStartImg.setObjectName("btnStartImg")
        self.chkTriangles = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTriangles.setEnabled(False)
        self.chkTriangles.setGeometry(QtCore.QRect(410, 360, 125, 22))
        self.chkTriangles.setObjectName("chkTriangles")
        self.btnEndImg = QtWidgets.QPushButton(self.centralwidget)
        self.btnEndImg.setGeometry(QtCore.QRect(530, 10, 158, 27))
        self.btnEndImg.setObjectName("btnEndImg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBlend.setText(_translate("MainWindow", "Blend"))
        self.label_4.setText(_translate("MainWindow", "Alpha"))
        self.txtAlpha.setText(_translate("MainWindow", "0.0"))
        self.Min.setText(_translate("MainWindow", "0.0"))
        self.Max.setText(_translate("MainWindow", "1.0"))
        self.btnStartImg.setText(_translate("MainWindow", "Load Starting Image ..."))
        self.chkTriangles.setText(_translate("MainWindow", "Show Triangles"))
        self.btnEndImg.setText(_translate("MainWindow", "Load Ending Image ..."))

