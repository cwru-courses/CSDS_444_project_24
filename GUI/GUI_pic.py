# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_pic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import scipy.io as io
import os
import time

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor, QPixmap
from PyQt5.QtWidgets import QFileDialog, QDialog, QLabel, QMessageBox

from Data_Encryption_Standard.Des import DES
from Vcipher.Vcipherencapsule import Vigenere
from RSA.RSA_GUI_V1 import KeyGenerator
from Paillier.Pimg import Paillier_Img

class pic_MainWindow(object):
    def __init__(self):
        self.pic_path = None              # picture path
        self.key_path = None              # key path
        self.pubKey = None                # pubKey
        self.priKey = None               # priKey
        self.public_key = None
        self.private_key = None
        self.encodeimg = None
        self.cipher_image = None
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_key = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_key.setEnabled(False)
        self.textEdit_key.setGeometry(QtCore.QRect(340, 20, 441, 87))
        self.textEdit_key.setObjectName("textEdit_3")
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setEnabled(False)
        self.textEdit_pic.setGeometry(QtCore.QRect(340, 150, 441, 281))
        self.textEdit_pic.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 130, 161, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.textEdit_execution = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_execution.setEnabled(False)
        self.textEdit_execution.setGeometry(QtCore.QRect(480, 530, 261, 51))
        self.textEdit_execution.setObjectName("textEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 120, 221, 31))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(60, 20, 161, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.clicked.connect(self.generateKey)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_key = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_key.setObjectName("pushButton_5")
        self.pushButton_key.clicked.connect(self.openkey)
        self.verticalLayout_4.addWidget(self.pushButton_key)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 540, 141, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 470, 161, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_pic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_pic.setObjectName("pushButton_3")
        self.pushButton_pic.clicked.connect(self.openpic)
        self.verticalLayout_3.addWidget(self.pushButton_pic)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.clicked.connect(self.encryption)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.clicked.connect(self.decryption)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 26))
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
        self.radioButton_3.setText(_translate("MainWindow", "RSA"))
        self.radioButton.setText(_translate("MainWindow", "Pailler"))
        self.label.setText(_translate("MainWindow", "Plaintext/Cipher text"))
        self.pushButton_4.setText(_translate("MainWindow", "Generate"))
        self.pushButton_key.setText(_translate("MainWindow", "Open Key file"))
        self.label_3.setText(_translate("MainWindow", "Exectution time"))
        self.pushButton_pic.setText(_translate("MainWindow", "Open file"))
        self.pushButton.setText(_translate("MainWindow", "Encryption"))
        self.pushButton_2.setText(_translate("MainWindow", "Decryption"))

    def openkey(self):
        directory1 = QFileDialog.getOpenFileName(None, "select file", './key/', "(*.txt))")
        print(directory1)
        path = directory1[0]
        if path != '':
            self.key_path = path
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.textEdit_key.setPlainText(file.read())
        else:
            self.textEdit_key.setPlainText('')

    def openpic(self):
        directory1 = QFileDialog.getOpenFileName(None, "select file", '', "")
        print(directory1)
        path = directory1[0]
        print(path)

        if path != '':
            if 'mat' in path:
                self.cipher_image = io.loadmat('cipher_galaxy.mat')
                self.empty_messageDialog3()
            else:
                self.pic_path = path
                document = self.textEdit_pic.document()
                cursor = QTextCursor(document)
                cursor.insertImage(path)

                dialog_fault = QDialog()
                image_path = path
                pic = QPixmap(image_path)
                label_pic = QLabel("show", dialog_fault)
                label_pic.setPixmap(pic)
                label_pic.setGeometry(10, 10, 1019, 537)
                # label_pic.setStyleSheet("border: 2px solid blue")
                label_pic.setScaledContents(True)

                dialog_fault.exec_()
        else:
            self.textEdit_pic.setPlainText('')

    '''encryption operation'''

    def encryption(self):
        self.textEdit_key.setEnabled(True)
        key = self.textEdit_key.toPlainText()

        if self.radioButton_2.isChecked():
            if key != '' and self.pic_path != '':
                start = time.time()
                Vc = Vigenere()
                img_path = self.pic_path
                Vc.encrypt_img(img_path,key)
                end = time.time()

                self.textEdit_execution.setText(str(end-start))

                print(self.pic_path)
            else:
                self.empty_messageDialog()
        elif self.radioButton_4.isChecked():
            if key != '' and self.pic_path != '':
                start = time.time()
                plain_image = cv2.imread(self.pic_path)
                des = DES()
                cipher = des.encryption(key, plain_image, 0)
                end = time.time()
                dialog_fault = QDialog()
                self.textEdit_execution.setText(str(end - start))
                label_pic = QLabel("show", dialog_fault)
                image_path = 'cipher_galaxy.png'
                pic = QPixmap(image_path)
                label_pic.setPixmap(pic)
                label_pic.setGeometry(10, 10, 1019, 537)
                # label_pic.setStyleSheet("border: 2px solid blue")
                label_pic.setScaledContents(True)
                dialog_fault.exec_()
            else:
                self.empty_messageDialog()
        elif self.radioButton.isChecked():
            if self.pic_path != '':
                start = time.time()
    
                p = Paillier_Img()
                p.getKeys()
                self.private_key=p.privateKey
                self.public_key=p.publicKey
            
                img_path = self.pic_path    
                img = p.imgEncode(img_path)
                self.encodeimg = img
    
                end = time.time()
                self.textEdit_execution.setText(str(end-start))
                                
                print('Pailler')
            else:
                self.empty_messageDialog2()
        elif self.radioButton_3.isChecked():
            if self.pic_path != '':
                print('RSA')
            else:
                self.empty_messageDialog2()
        else:
            self.messageDialog()

    '''decryption operation'''

    def decryption(self):
        if self.cipher_image is not None:
            key = self.cipher_image
        else:
            self.textEdit_key.setEnabled(True)
            key = self.textEdit_key.toPlainText()  # get key from txt file

        if self.radioButton_2.isChecked():
            if key != '' and self.pic_path != '':
                start = time.time()
                Vc = Vigenere()
                Vc.decrypt_img(key)
                end = time.time()
                self.textEdit_execution.setText(str(end-start))
                dialog_fault = QDialog()
                self.textEdit_execution.setText(str(end - start))
                label_pic = QLabel("show", dialog_fault)
                image_path = 'originalImage.jpg'
                pic = QPixmap(image_path)
                label_pic.setPixmap(pic)
                label_pic.setGeometry(10, 10, 1019, 537)
                # label_pic.setStyleSheet("border: 2px solid blue")
                label_pic.setScaledContents(True)
                dialog_fault.exec_()
                self.cipher_image = None
            else:
                self.empty_messageDialog()
        elif self.radioButton_4.isChecked():
            if key != '' and self.pic_path != '':
                start = time.time()
                plain_image = cv2.imread(self.pic_path)
                des = DES()
                cipher = des.decryption(key, plain_image, 0)
                end = time.time()
                dialog_fault = QDialog()
                self.textEdit_execution.setText(str(end - start))
                label_pic = QLabel("show", dialog_fault)
                image_path = 'final_galaxy.png'
                pic = QPixmap(image_path)
                label_pic.setPixmap(pic)
                label_pic.setGeometry(10, 10, 1019, 537)
                # label_pic.setStyleSheet("border: 2px solid blue")
                label_pic.setScaledContents(True)
                dialog_fault.exec_()
            else:
                self.empty_messageDialog()
        elif self.radioButton.isChecked():  # no key check
            if self.pic_path != '':
                 start = time.time()    
                 p = Paillier_Img()

                 p.publicKey = self.public_key
                 p.privateKey = self.private_key

                 img_d = p.imgDecode(self.encodeimg)
                 
                 img_d.save('decodeImg.png')
                 dialog_fault = QDialog()
                 label_pic = QLabel("show", dialog_fault)
                 image_path = 'decodeImg.png'
                 pic = QPixmap(image_path)
                 label_pic.setPixmap(pic)
                 label_pic.setGeometry(10, 10, 1019, 537)
                # label_pic.setStyleSheet("border: 2px solid blue")
                 label_pic.setScaledContents(True)
                 dialog_fault.exec_()   
    
                 end = time.time()
                 self.textEdit_execution.setText(str(end-start))

            else:
                self.empty_messageDialog2()
        elif self.radioButton_3.isChecked():  # no key check
            if self.pic_path != '':
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

    def empty_messageDialog3(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'warning', 'mat file!')
        msg_box.exec_()

    # generate private key and public key
    def generateKey(self):
        self.pubKey = ''  # pubKey
        self.priKey = ''  # priKey
        self.textEdit_key.setPlainText('public key:' + self.pubKey + '\n' + 'private key:' + self.priKey + '\n')