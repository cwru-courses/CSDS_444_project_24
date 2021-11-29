from tkinter import *
from tkinter import filedialog, dialog
import os
from DES import DES
from VC import Vigenere
from pailliar import Paillier
from MD5 import MD5_State


def Algorithm_func():
    mg = ''
    mg += str(algorithm_value.get())

    algorithm_text["state"] = NORMAL
    algorithm_text.delete(0.0, END)
    if mg == '1':
        algorithm_text.insert('insert', 'Algorithm: VG')
    elif mg == '2':
        algorithm_text.insert('insert', 'Algorithm: DES')
    elif mg == '3':
        algorithm_text.insert('insert', 'Algorithm: MD5')
    elif mg == '4':
        algorithm_text.insert('insert', 'Algorithm: RSA')
    else:
        algorithm_text.insert('insert', 'Algorithm: Pailliar')
    algorithm_text["state"] = DISABLED


def work_fuc():
    mg = ''
    mg += str(algorithm_value.get())
    mg2 = ''
    mg2 += str(work.get())
    print(mg, mg2)
    key_text['state'] = NORMAL
    text_text['state'] = NORMAL
    result_text['state'] = NORMAL

    # Encryption
    if (mg != '0') & (mg2 == '2'):
        if mg == '1':
            result_text.delete(0.0, END)
            Vc = Vigenere()
            Vc_string = text_text.get("1.0", "end")
            print(Vc_string)
            Vc_string = Vc_string.replace("\n", "")
            bytestring = bytearray(Vc_string, 'utf-8')
            print(bytestring)

            Vc.key = key_text.get("1.0", "end")
            Vc.key = Vc.key.replace("\n", "")
            CipherText = Vc.cipherText(Vc_string, Vc.key)
            print("CipherText:", CipherText)
            result_text.insert('insert', CipherText)
        elif mg == '2':
            result_text.delete(0.0, END)
            des = DES()
            des_text = text_text.get("1.0", "end")
            des_text = ''.join(des_text.replace("\n", ""))
            print(des_text)
            des_key = key_text.get("1.0", "end")
            des_key = ''.join(des_key.replace("\n", ""))
            desText = des.encryption(des_key, des_text)
            print(desText)
            result_text.insert('insert', desText)
        elif mg == '3':
            result_text.delete(0.0, END)
            print('3')
        elif mg == '4':
            result_text.delete(0.0, END)
            print('4')
        elif mg == '5':
            result_text.delete(0.0, END)
            print('5')
            key = text_text.get("1.0", "end")
            key = key.replace("\n", "")
            paill = Paillier()
            p = Paillier()
            p.__key_gen__()
            # Key = p.pubKey
            byte = bytes(key, 'utf-8')
            plaintext = byte
            print("Plaintext:", plaintext)
            ciphertext = p.encrypt(plaintext)
            print("Ciphertext:", ciphertext)
            result_text.insert('insert', ciphertext)
        else:
            result_text.delete(0.0, END)
            print('6')

    # Decryption
    if (mg != '0') & (mg2 == '1'):
        if mg == '1':
            result_text.delete(0.0, END)
            Vc = Vigenere()
            Vc_string = text_text.get("1.0", "end")
            print(Vc_string)
            Vc_string = Vc_string.replace("\n", "")
            bytestring = bytearray(Vc_string, 'utf-8')
            print(bytestring)

            Vc.key = key_text.get("1.0", "end")
            Vc.key = Vc.key.replace("\n", "")
            CipherText = Vc.original_text(Vc_string, Vc.key)
            print("CipherText:", CipherText)
            result_text.insert('insert', CipherText)
        elif mg == '2':
            result_text.delete(0.0, END)
            des = DES()
            des_text = text_text.get("1.0", "end")
            des_text = ''.join(des_text.replace("\n", ""))
            print(des_text)
            des_key = key_text.get("1.0", "end")
            des_key = ''.join(des_key.replace("\n", ""))
            desText = des.decryption(des_key, des_text)
            print(desText)
            result_text.insert('insert', desText)
        elif mg == '3':
            result_text.delete(0.0, END)
            key = text_text.get("1.0", "end")
            key = ''.join(key.replace("\n", ""))
            obj = MD5_State()
            buff = [''] * 16
            ciper = obj.md5_digest(key, len(key), buff)
            str1 = ''
            for i in range(16):
                str1 += "%x" % ((ord(buff[i]) & 0xF0) >> 4)
                str1 += "%x" % (ord(buff[i]) & 0x0F)
            result_text.insert('insert', str1)
        elif mg == '4':
            result_text.delete(0.0, END)
            print('3')
        elif mg == '5':
            result_text.delete(0.0, END)
            key = text_text.get("1.0", "end")
            key = key.replace("\n", "")
            paill = Paillier()
            p = Paillier()
            p.__key_gen__()
            # Key = p.pubKey
            byte = bytes(key, 'utf-8')
            plaintext = byte
            print("Plaintext:", plaintext)
            deciphertext = p.decrypt(plaintext)
            print("Deciphertext: ", deciphertext)
            result_text.insert('insert', deciphertext)
        else:
            result_text.delete(0.0, END)
            paill = Paillier()

    key_text['state'] = DISABLED
    text_text['state'] = DISABLED
    result_text['state'] = DISABLED


def show_key():
    # global file_path
    # global file_text
    file_path = filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser('E:/')))
    print('open file：', file_path)
    key_text['state'] = NORMAL
    key_text.delete(0.0, END)
    if file_path is not None:
        with open(file=file_path, mode='r+', encoding='utf-8') as file:
            file_text = file.read()
            print(file_text)
            key_text.insert('insert', file_text)
    key_text['state'] = DISABLED


def show_text():
    # global file_path
    # global file_text
    file_path = filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser('E:/')))
    print('open file：', file_path)
    text_text['state'] = NORMAL
    text_text.delete(0.0, END)
    if file_path is not None:
        with open(file=file_path, mode='r+', encoding='utf-8') as file:
            file_text = file.read()
            print(file_text)
            text_text.insert('insert', file_text)
    key_text['state'] = DISABLED


root = Tk()
root.geometry("800x600")
root.title("Computer security")
lb = Label(root, text='Please select algorithm：', fg='blue')
# lb.pack(anchor='nw')

first_x = 20
first_y = 40

lb.place(x=first_x, y=first_y)
algorithm_value = IntVar()
VC_select = Radiobutton(root, text='VC', value=1, variable=algorithm_value)
# VC_select.pack(side=TOP, fill=Y)
VC_select.place(x=first_x, y=first_y * 2)
DES_select = Radiobutton(root, text='DES', value=2, variable=algorithm_value)
# DES_select.pack(side=LEFT)
DES_select.place(x=first_x, y=first_y * 3)
MD5_select = Radiobutton(root, text='MD5', value=3, variable=algorithm_value)
# MD5_select.pack(side=LEFT)
MD5_select.place(x=first_x, y=first_y * 4)
RSA_select = Radiobutton(root, text='RSA', value=4, variable=algorithm_value)
# RSA_select.pack(side=LEFT)
RSA_select.place(x=first_x, y=first_y * 5)
pailliar_select = Radiobutton(root, text='Pailliar', value=5, variable=algorithm_value)
# pailliar_select.pack(anchor=SW)
pailliar_select.place(x=first_x, y=first_y * 6)
Elgamal_select = Radiobutton(root, text='Elgamal', value=6, variable=algorithm_value)
# pailliar_select.pack(anchor=SW)
Elgamal_select.place(x=first_x, y=first_y * 7)

# algorithm_text = Text(root, state=DISABLED, width=30, height=10)
# # algorithm_text.pack()
# algorithm_text.place(x=first_x,y=first_y*8)
lb2 = Label(root, text='Decryption or Encryption：', fg='blue')
# lb2.pack()
lb2.place(x=first_x, y=first_y * 9)
work = IntVar()
Decryption_select = Radiobutton(root, text='Decryption', value=1, variable=work, command=work_fuc)
# Decryption_select.pack(anchor='n')
Decryption_select.place(x=first_x, y=first_y * 10)
Encryption_select = Radiobutton(root, text='Encryption', value=2, variable=work, command=work_fuc)
# Encryption_select.pack(anchor='n')
Encryption_select.place(x=first_x, y=first_y * 11)

key_button = Button(root, text='Select key file', command=show_key)
key_button.place(x=200, y=first_y)
text_button = Button(root, text='Select Plaintext/Ciphertext file', command=show_text)
text_button.place(x=500, y=first_y)
key_text = Text(root, state=DISABLED, width=35, height=15)
key_text.place(x=200, y=first_y * 2)
text_text = Text(root, state=DISABLED, width=35, height=15)
text_text.place(x=500, y=first_y * 2)

lb4 = Label(root, text='Result：', fg='black')
lb4.place(x=420, y=first_y * 7.5)
result_text = Text(root, state=DISABLED, width=60, height=15)
result_text.place(x=260, y=first_y * 8)

root.mainloop()
