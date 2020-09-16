"""
Creating a PyQt Application:

1- Create a UI file using the QtDesigner.

2- Convert the UI file to a Python file using the conversion tool:
    /package/eda/anaconda3/bin/pyuic5 <fileName.ui> -o <fileName.py>
   The generated file must NOT be modified, as indicated in the header warning!

3- Use the given file <blank.py> to create a consumer Python file, and write the code that drives the UI.

"""

# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from Lab11.calculator import *

class MathConsumer (QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btnCalculate.clicked.connect(self.performOperation)
    def performOperation (self):
        # if self.edtNumber1.text() == "" or self.edtNumber2.text() == "":
        #     self.edtResult.setText("E")
        #self.edtNumber1.text()
        #else:
        try:
            if self.cboOperation.currentText() == '+':
                self.edtResult.setText(str(float(self.edtNumber1.text())+float(self.edtNumber2.text())))
            if self.cboOperation.currentText() == '-':
                self.edtResult.setText(str(float(self.edtNumber1.text()) - float(self.edtNumber2.text())))
            if self.cboOperation.currentText() == '*':
                self.edtResult.setText(str(float(self.edtNumber1.text()) * float(self.edtNumber2.text())))
            if self.cboOperation.currentText() == '/':
                self.edtResult.setText(str(float(self.edtNumber1.text()) / float(self.edtNumber2.text())))
        except:
            self.edtResult.setText("E")
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    currentApp.exec_()

