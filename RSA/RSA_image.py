import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import random
import math


class RSAimage(object):

    def __int__(self):
        self.n = None
        self.e = None
        self.d = None
        self.PublicKey = None
        self.PrivateKey = None
        self.encrypt = None

def miller_rabin(self,nn, k):
    a = random.randrange(2, nn - 1)
    x = self.fast_mod(a, k,nn)
    if x == 1 or x == nn-1:
        return True
    else:
        while(k != nn-1):
            x = ((x % nn)*(x % nn)) % nn
            if x == 1:
                return False
            if x == nn-1:
                return True
            d <<= 1
    return False

def fast_mod(self,b, e, m):
    ans = 1
    while e != 0:
        if e % 2 == 1:
            ans = ((ans % m)*(b % m)) % m
        b = ((b % m)*(b % m)) % m
        e >>= 1
    return ans



def isPrime(self,m,k):
    if m == 3 or m == 2:
        return True
    if m <= 1 or m % 2 == 0:
        return False
    d = m-1
    while d % 2 != 0:
        d /= 2
    for _ in range(k):
        if not self.miller_rabin(m, d):
            return False
    return True

def genprimeseed(self,length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def gen_prime(self,length):
    A = 4
    while not self.isPrime(A, 128):
        A = self.genprimeseed(length)
    return A



# In[5]:

def genkeys(self,length):
    p = self.gen_prime(length)
    q = self.gen_prime(length)
    self.n = p*q
    fn = (p-1)*(q-1)
    self.e = self.gen_prime(4)
    while math.gcd(self.e, fn) != 1:
        self.e = self.gen_prime(4)
    a1, a2, b1, b2, d1, d2 = 1, 0, 0, 1, fn, self.e
    while d2 != 1:
        k = (d1//d2)
        temp = a2
        a2 = a1-(a2*k)
        a1 = temp
        temp = b2
        b2 = b1-(b2*k)
        b1 = temp
        temp = d2
        d2 = d1-(d2*k)
        d1 = temp
        self.d = b2
    if self.d > fn:
        self.d = self.d % fn
    elif self.d < 0:
        self.d = self.d+fn

def getkeys(self):
    self.genkeys(5)
    self.PrivateKey = [self.n, self.d]
    self.PublicKey = [self.n, self.e]

def encrypt_img(self,path):
    my_img = io.imread(path)
    plt.imshow(my_img, cmap="gray")
    plt.show()
    height, width = my_img.shape[0], my_img.shape[1]
    row, col = my_img.shape[0], my_img.shape[1]
    self.encrypt= [[0 for x in range(10000)] for y in range(10000)]
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = my_img[i, j]
            C1 = self.fast_mod(r, self.e, self.n)
            C2 = self.fast_mod(g, self.e, self.n)
            C3 = self.fast_mod(b, self.e, self.n)
            self.encrypt[i][j] = [C1, C2, C3]
            C1 = C1 % 256
            C2 = C2 % 256
            C3 = C3 % 256
            my_img[i, j] = [C1, C2, C3]

    fig=plt.figure()
    plt.xlabel('encrypted image ')
    plt.imshow(my_img, cmap="gray")
    plt.show()
    return my_img

# In[15]:

def decrypt_img(self):
    height, width = my_img.shape[0], my_img.shape[1]
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = self.encrypt[i][j]
            M1 = self.fast_mod(r, self.d, self.n)
            M2 = self.fast_mod(g, self.d, self.n)
            M3 = self.fast_mod(b, self.d, self.n)
            my_img[i, j] = [M1, M2, M3]
    plt.imshow(my_img, cmap="gray")
    plt.xlabel('Image decryption')
    plt.show()
    plt.show(block='True')
    return my_image
