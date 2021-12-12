# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_txt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
#from DES12111 import DES
import time

from Vcipher.Vcipherencapsule import Vigenere

class txt_MainWindow(object):

    def __init__(self):
        self.txt_path = None
        self.key_path = None

    def setupUi(self, MainWindow):
        self.cpath = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 708)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 130, 161, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 470, 161, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openfile)

        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_encrypt = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_encrypt.setObjectName("pushButton")
        self.pushButton_encrypt.clicked.connect(self.encryption)
        self.verticalLayout_2.addWidget(self.pushButton_encrypt)
        self.pushButton_decrypt = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_decrypt.setObjectName("pushButton_2")
        self.pushButton_decrypt.clicked.connect(self.decryption)

        self.verticalLayout_2.addWidget(self.pushButton_decrypt)
        self.textEdit_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_txt.setEnabled(False)
        self.textEdit_txt.setGeometry(QtCore.QRect(350, 120, 421, 221))
        self.textEdit_txt.setObjectName("textEdit")
        self.textEdit_result = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_result.setEnabled(False)
        self.textEdit_result.setGeometry(QtCore.QRect(350, 380, 431, 171))
        self.textEdit_result.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 100, 221, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 350, 171, 21))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 20, 161, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.open_key_file)

        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.textEdit_key = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_key.setEnabled(False)
        self.textEdit_key.setGeometry(QtCore.QRect(350, 20, 421, 87))
        self.textEdit_key.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 590, 141, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_execution = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_execution.setEnabled(False)
        self.textEdit_execution.setGeometry(QtCore.QRect(510, 570, 261, 51))
        self.textEdit_execution.setObjectName("textEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_2.setText(_translate("MainWindow", "Vcipher"))
        self.radioButton_4.setText(_translate("MainWindow", "DES"))
        self.radioButton_5.setText(_translate("MainWindow", "MD5"))
        self.radioButton_3.setText(_translate("MainWindow", "RSA"))
        self.radioButton.setText(_translate("MainWindow", "Pailler"))
        self.pushButton_3.setText(_translate("MainWindow", "Open file"))
        self.pushButton_encrypt.setText(_translate("MainWindow", "Encryption"))
        self.pushButton_decrypt.setText(_translate("MainWindow", "Decryption"))
        self.label.setText(_translate("MainWindow", "Plaintext/Cipher text"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.pushButton_4.setText(_translate("MainWindow", "Generate"))
        self.pushButton_5.setText(_translate("MainWindow", "Open Key file"))
        self.label_3.setText(_translate("MainWindow", "Exectution time"))

    def openfile(self):
        directory1 = QFileDialog.getOpenFileName(None, "select file",'./key/', "(*.txt))")
        print(directory1)
        path = directory1[0]
        if path != '':
            self.txt_path=path
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.textEdit_txt.setPlainText(file.read())
        else:
            self.textEdit_txt.setPlainText('')

    def open_key_file(self):
        directory1 = QFileDialog.getOpenFileName(None, "select file",'./key/', "(*.txt))")

        path = directory1[0]
        print(directory1)
        if path != '':
            self.key_path = path
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.textEdit_key.setPlainText(file.read())
        else:
            self.textEdit_key.setPlainText('')
    '''encryption operation'''
    def encryption(self):
        self.textEdit_key.setEnabled(True)
        key = self.textEdit_key.toPlainText()
        txt = self.textEdit_txt.toPlainText()
        if self.radioButton_2.isChecked():
            if key != '' and txt != '':
                start = time.time()
                Vc = Vigenere()
                file_path = self.txt_path
                Vc_result = Vc.cipher_Text(file_path,key)
                end = time.time()
                self.textEdit_execution.setText(str(end-start))
                self.textEdit_result.setText(Vc_result)
                print(self.txt_path)
            else:
                self.empty_messageDialog()
        # elif self.radioButton_4.isChecked():
        #     if key != '' and txt != '':
        #         start = time.time()
        #         des = DES()
        #         DES_result = des.encryption(key, txt, 1)
        #         end = time.time()
        #         self.textEdit_result.setText(DES_result)
        #         self.textEdit_execution.setText(str(end - start))
        #     else:
        #         self.empty_messageDialog()
        elif self.radioButton_5.isChecked():
            if txt != '':
                print('MD5')
            else:
                self.empty_messageDialog2()
        elif self.radioButton.isChecked():
            if txt != '':
                print('Pailler')
            else:
                self.empty_messageDialog2()
        elif self.radioButton_3.isChecked():
            if txt != '':
                print('RSA')
            else:
                self.empty_messageDialog2()
        else:
            self.messageDialog()

    '''decryption operation'''
    def decryption(self):
        self.textEdit_key.setEnabled(True)
        key = self.textEdit_key.toPlainText() # get key from txt file
        txt = self.textEdit_txt.toPlainText()  # get cipher text or plain text from txt file
        if self.radioButton_2.isChecked():
            if key != '' and txt != '':
                start = time.time()
                Vc = Vigenere()
                Vc_result = Vc.decrypt_text(key)
                end = time.time()
                self.textEdit_execution.setText(str(end-start))
                self.textEdit_result.setText(Vc_result)
                print('VC')
            else:
                self.empty_messageDialog()
        elif self.radioButton_4.isChecked():
            if key != '' and txt != '':
                start = time.time()
                des = DES()
                DES_result = des.decryption(key, txt, 1)
                end = time.time()
                self.textEdit_result.setText(DES_result) # show the result of the encryption or the decryption
                self.textEdit_execution.setText(str(end-start)) #show the execution time
            else:
                self.empty_messageDialog()
        elif self.radioButton_5.isChecked(): # no key check
            if txt != '':
                print('MD5')
            else:
                self.empty_messageDialog2()
        elif self.radioButton.isChecked():  # no key check
            if txt != '':
                print('Pailler')
            else:
                self.empty_messageDialog2()
        elif self.radioButton_3.isChecked(): # no key check
            if txt != '':
                print('RSA')
            else:
                self.empty_messageDialog2()
        else:
            self.messageDialog()

    def messageDialog(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'warning', 'click the algorithm')
        msg_box.exec_()

    def empty_messageDialog(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'warning', 'no key or text')
        msg_box.exec_()

    def empty_messageDialog2(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'warning', 'no text')
        msg_box.exec_()
