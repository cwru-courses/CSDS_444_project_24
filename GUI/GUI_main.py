import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI_menu import Ui_MainWindow
from GUI_txt import txt_MainWindow
from GUI_pic import pic_MainWindow
from GUI_vedio import vedio_MainWindow


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


class txtWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child = txt_MainWindow()
        self.child.setupUi(self)
        # self.child.pushButton_decrypt.clicked.connect(self.decryption)

    # def decryption(self):
    #     self.textEdit_key.setEnabled(True)
    #
    #     if self.radioButton_2.isChecked():
    #         print('Vcipher')
    #     elif self.radioButton_4.isChecked():
    #         print('DES')
    #     elif self.radioButton_5.isChecked():
    #         print('MD5')
    #     elif self.radioButton.isChecked():
    #         print('Pailler')
    #     elif self.radioButton_3.isChecked():
    #         print('RSA')
    #     else:
    #         self.messageDialog()
    #     print(self.textEdit_key.text)


class picWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child = pic_MainWindow()
        self.child.setupUi(self)


class videoWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child = vedio_MainWindow()
        self.child.setupUi(self)





if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    app = QApplication(sys.argv)
    window = parentWindow()
    txt_child = txtWindow()
    # 通过toolButton将两个窗体关联
    btn = window.main_ui.pushButton
    btn.clicked.connect(txt_child.show)
    pic_child = picWindow()
    # 通过toolButton将两个窗体关联
    btn2 = window.main_ui.pushButton_2
    btn2.clicked.connect(pic_child.show)
    video_child = videoWindow()
    # 通过toolButton将两个窗体关联
    btn3 = window.main_ui.pushButton_3
    btn3.clicked.connect(video_child.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
