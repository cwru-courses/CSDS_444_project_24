import gmpy2 
import math
from random import randint
from math import gcd
import libnum
rs = gmpy2.random_state()


class Paillier(object):
    
 
    def __init__(self):
        
        self.publicKey = None
        self.privateKey = None
        
    def lcm(self, x, y):
        
        return x * y // gcd(x, y) 
    
    def sTn(self,m):
        arr = bytes(m, 'utf-8')
        m = int.from_bytes(arr, 'big')
        return m
          
     
    def getP(self):
        
        p = gmpy2.mpz_urandomb(rs, 2024)
        while not gmpy2.is_prime(p):
            p = p + 1
        return p
    
    def getKeys(self):
     
        p = self.getP()
        q = self.getP()
        
        n = p * q
        lamda = self.lcm(p-1, q-1)
        g = n + 1
        mu = (pow(g,lamda,n*n)-1) // n
        mu = libnum.invmod(mu, n)
        
        self.publicKey = [n, g]
        self.privateKey = [lamda, mu]
    
    def encrypt(self, m):
        
        m = self.sTn(m)
        # print(m)
        
        n,g = self.publicKey
        r = randint(0,n)
        c = (pow(g, m, n*n) * pow(r, n, n*n)) % (n*n)
        
        # print(c)
        return c
    
    def decrypt(self,c):
        
        n, g = self.publicKey
        lamda, mu = self.privateKey
        
        c = (pow(c,lamda, n*n) - 1) // n * mu
        c = c % n
        c = int (c)
        # print(c)
        
        m = libnum.n2s(c)
        m = m.decode("utf-8") 
        return m


    
if __name__ == "__main__":    
    string = 'CWRo get ae.'
    byte = ''
    text = string #byte
    
    p = Paillier()
    p.getKeys()
    
    
    c = p.encrypt(text) 
    m = p.decrypt(c)
    
    print("Plaintext:", text)
    print("Ciphertext:", c)
    print("Deciphertext: ", m)
