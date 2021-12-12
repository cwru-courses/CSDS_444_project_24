#python code to implement Vigenere Cipher


# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from io import BytesIO
import numpy as np
import string
import os
import base64
import time

from numpy.core.fromnumeric import shape


class Vigenere():

    def __init__(self):
        self.asciilist=[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', 
                        '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
                        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', 
                        '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~','\n']
        
    def encryptstring(self, string, key):
        cipher_text = ""
        for i in range(len(string)):
            if string[i] not in self.asciilist:
                cipher_text += string[i]
            cipher_text += self.asciilist[(self.asciilist.index(string[i])+self.asciilist.index(key[i%len(key)]))%len(self.asciilist)]
        return cipher_text


        
    def decryptstring(self,cipher_text, key):
        output = ""
        for i in range(len(cipher_text)):
            if cipher_text[i] not in self.asciilist:
                output += cipher_text[i]
            output += self.asciilist[(self.asciilist.index(cipher_text[i]) - self.asciilist.index(key[i % len(key)])) % len(self.asciilist)]
        return output


    def cipher_Text(self, data_file, key):
        cipher_text = ""
        cipher_text_path = "Ciphertext.txt"
        with open(data_file, 'r') as f:
            string = f.read()
        for i in range(len(string)):
            if string[i] not in self.asciilist:
                cipher_text += string[i]
            cipher_text += self.asciilist[(self.asciilist.index(string[i])+self.asciilist.index(key[i%len(key)]))%len(self.asciilist)]

        with open(cipher_text_path,'w') as f:
            f.write(cipher_text)
        return cipher_text


        
    def decrypt_text(self, key):
        output = ""
        cipher_text_path = "Ciphertext.txt"
        PlainText_path = "Plaintext.txt"
        with open(cipher_text_path, 'r') as f:
            cipher_text = f.read()
        for i in range(len(cipher_text)):
            if cipher_text[i] not in self.asciilist:
                output += cipher_text[i]
            output += self.asciilist[(self.asciilist.index(cipher_text[i]) - self.asciilist.index(key[i % len(key)])) % len(self.asciilist)]
        with open(PlainText_path, 'w') as f:
            f.write(output)
        return output



    def encrypt_img(self, img_path, key):
        byte_path = 'image_bytes.txt'
        cipher_path = 'cipher_img.txt'
        with open(img_path, 'rb') as f :
            img_byte2string = base64.b64encode(f.read())
            img_string = img_byte2string.decode('ascii')
        with open(byte_path, 'w') as f:
            f.write(img_string)
        Cipher_Image = self.encryptstring(img_string,key )
        with open(cipher_path, 'w') as f:
            f.write(Cipher_Image)
        
    def decrypt_img(self, key):
        cipher_path = 'cipher_img.txt'
        plainimg_path = 'PlainImage.txt'
        originalimg_path = 'originalImage.jpg'
        with open(cipher_path, 'r') as f:
            Cipher_Image = f.read()
            Plain_Image = self.decryptstring(Cipher_Image,key)
        with open(plainimg_path, "w") as p:
            p.write(Plain_Image)
        String2Bytes = Plain_Image.encode('ascii')

        with open(originalimg_path,'wb') as str2image:
            str2image.write(base64.b64decode(String2Bytes))
            str2image.close()

def main():
    Vc = Vigenere()
    with open('key3.txt','r') as f:
        key = f.read()
    file_path = 'plaintext3.txt'
    img_path = "figure3_1920_970.png"
    Vc.cipher_Text(file_path,key)
    Vc.decrypt_text(key)
    Vc.encrypt_img(img_path,key)
    Vc.decrypt_img(key)
    print("success!")
    
if __name__ == '__main__':
    main()
        

        

 

    


  
    
    



        


    



    
    

         
        
