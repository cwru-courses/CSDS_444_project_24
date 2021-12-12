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

    def cipherText(self, string, key):
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


        
    def original_text(self,cipher_text, key):
        output = ""
        for i in range(len(cipher_text)):
            if cipher_text[i] not in self.asciilist:
                output += cipher_text[i]
            output += self.asciilist[(self.asciilist.index(cipher_text[i]) - self.asciilist.index(key[i % len(key)])) % len(self.asciilist)]
        return output


 

    

if __name__ == "__main__":
    Vc = Vigenere()
    #long text encryption
    with open("plaintext3.txt", "r") as f:
        data = f.read()
    #    print(data)
    # the file input
    with open("key3.txt", "r") as k :
        key = k.read()
    # the key 
    start_cipher = time.time()
    CipherText = Vc.cipherText(data, key)
    end_cipher = time.time()
    print("time to encrypt long text ", end_cipher - start_cipher)
    
    with open("Ciphertext.txt","w") as c:
        c.write(CipherText)
    start_decrypt = time.time()
    PlainText = Vc.original_text(CipherText,key)
    end_decrypt = time.time()
    print("time to decrypt long text", end_decrypt - start_cipher)
    with open("Plaintext.txt", "w") as p:
        p.write(PlainText)

    # Image to bytes
    img_path = 'figure3_1920_970.png'
    fname = 'imagebytes.txt'
    with open(img_path,'rb') as f:
        img_byte2string = base64.b64encode(f.read())
        img_string = img_byte2string.decode('ascii')
        # print(img_string)
    start_cipherimg = time.time()
    if not os.path.getsize(fname):
        with open(fname,'w') as f:
            f.write(img_string)
    else:
        with open(fname,'w') as f:
            f.truncate(0)
            f.write(img_string)
    #bytes to image

    #Encrypt the Image
    Cipher_Image = Vc.cipherText(img_string, key)
    end_encryptimg = time.time()
    print("time to encrypt the image:" , end_encryptimg - start_cipherimg)



    start_decryptimg = time.time()
    with open('cipher_image.txt', 'w') as f:
        f.write(Cipher_Image)
    Plain_Image = Vc.original_text(Cipher_Image, key)
    with open("PlainImage.txt", "w") as p:
        p.write(Plain_Image)
    
    String2Bytes = Plain_Image.encode('ascii')
    #print(type(String2Bytes))

    with open('originalImage.jpg','wb') as str2image:
       str2image.write(base64.b64decode(String2Bytes))
       str2image.close()
    end_decryptimg = time.time()
    print("time to decrypt img:", end_decryptimg - start_decryptimg)

  
    
    



        


    



    
    

         
        
