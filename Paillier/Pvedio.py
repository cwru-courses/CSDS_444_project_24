import cv2
import numpy as np
import gmpy2
import math
from random import randint
from math import gcd
import libnum
from PIL import Image
import timeit


### paillier method
class Paillier(object):

    def __init__(self):
        rs = gmpy2.random_state()
        self.publicKey = None
        self.privateKey = None

    def lcm(self, x, y):

        return x * y // gcd(x, y)

    def sTn(self, m):
        arr = bytes(m, 'utf-8')
        m = int.from_bytes(arr, 'big')
        return m

    def getP(self):

        p = gmpy2.mpz_urandomb(rs, 1024)
        while not gmpy2.is_prime(p):
            p = p + 1
        return p

    def getKeys(self):

        # p = self.getP()
        # q = self.getP()

        p = 23
        q = 19

        n = p * q
        lamda = self.lcm(p - 1, q - 1)

        g = n + 1
        mu = (pow(g, lamda, n * n) - 1) // n
        mu = libnum.invmod(mu, n)

        # mu = gmpy2.invert(lamda, n)

        n = int(n)
        g = int(g)
        lamda = int(lamda)
        mu = int(mu)

        self.publicKey = [n, g]
        self.privateKey = [lamda, mu]

    def encrypt(self, m):

        if isinstance(m, str):
            m = self.sTn(m)

        # print(m)

        n, g = self.publicKey
        r = randint(0, n)
        while gcd(n, r) != 1:
            r = r + 1

        c = (pow(g, m, n * n) * pow(r, n, n * n)) % (n * n)

        # print(c)
        return c

    def decrypt(self, c):

        n, g = self.publicKey
        lamda, mu = self.privateKey

        c = (pow(c, lamda, n * n) - 1) // n * mu
        c = c % n
        c = int(c)
        # print(c)
        m = c
        # m = libnum.n2s(c)
        # m = m.decode("utf-8")
        return m