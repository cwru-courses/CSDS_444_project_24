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


    def generate_key(self, string, key):
        key = list(key)
        if len(string) == len(key):
            return key
        else:
            #key cannot be longer that the plain text
            for i in range(len(string)-len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))
        
        #The join() method takes all items in an iterable and joins them into one string. 

    def cipher_Text(self, string, key):
        cipher_text = ""
        '''for char in string:
            if ord(char) in range(65,91):
                msg.append((ord(char)-65,0))
            elif ord(char) in range(97,123):
                msg.append((ord(char)-97,1))
            elif ord(char) in range(33, 48):
                msg.append((ord(char)-33,2))
            else:
                msg.append(char)
        key = [ord(char) - 65 for char in key.lower()]
        for i in range(len(msg)):
            if type(msg[i]) == type('') : cipher_text += msg[i]
            else:
                value = (msg[i][0] + key[i % len(key)]) % 26
                #v1 = (msg[i][2] + key[i % len(key)]) % 15
                cipher_text += chr(value + 65 + msg[i][1]*32)
        return cipher_text'''
        for i in range(len(string)):
            if string[i] not in self.asciilist:
                cipher_text += string[i]
            cipher_text += self.asciilist[(self.asciilist.index(string[i])+self.asciilist.index(key[i%len(key)]))%len(self.asciilist)]
        return cipher_text


        
    def decrypt_text(self,cipher_text, key):
        output = ""
        for i in range(len(cipher_text)):
            if cipher_text[i] not in self.asciilist:
                output += cipher_text[i]
            output += self.asciilist[(self.asciilist.index(cipher_text[i]) - self.asciilist.index(key[i % len(key)])) % len(self.asciilist)]
        return output


    def encrypt_img(self, img_path, key ):
        byte_path = 'image_bytes.txt'
        cipher_path = 'cipher_img.txt'
        with open(img_path, 'rb') as f :
            img_byte2string = base64.b64encode(f.read())
            img_string = img_byte2string.decode('ascii')
            with open(byte_path, 'w') as f:
                f.write(img_string)
            Cipher_Image = self.cipher_Text(img_string, key )
            with open(cipher_path, 'w') as f:
                f.write(Cipher_Image)
        
    def decrypt_img(self, key):
        cipher_path = 'cipher_img.txt'
        plainimg_path = 'PlainImage.txt'
        originalimg_path = 'originalImage.jpg'
        with open(cipher_path, 'r') as f:
            Cipher_Image = f.read()
            Plain_Image = self.decrypt_text(Cipher_Image, key)
            with open(plainimg_path, "w") as p:
                p.write(Plain_Image)
            String2Bytes = Plain_Image.encode('ascii')

        with open(originalimg_path,'wb') as str2image:
            str2image.write(base64.b64decode(String2Bytes))
            str2image.close()

def main():
        Vc = Vigenere()
        with open("key3.txt", "r") as k :
            key = k.read()
        img_path = 'figure2_700_525.png'
        Vc.encrypt_img(img_path,key)
        Vc.decrypt_img(key)
        print("success!")
    
if __name__ == '__main__':
    main()
        

        

 

    


  
    
    



        


    



    
    

         
        
