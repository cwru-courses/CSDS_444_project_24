import random
import math

class RSAtext(object):

    def __init__(self):
        self.n = None
        self.e = None
        self.d = None
        self.PublicKey = None
        self.PrivateKey = None
        self.msg = ""
        self.secret = ""
    
    def gen_prime(self, l):
        while True:
            p = random.randint(0, l/2)
            if p % 2 != 0:
                target = 1
                for _ in range(0, 10):
                    if self.miller_rabin(p, 7):
                        pass
                    else:
                        target = 0
                        break
                if target:
                    return p

    def genkeys(self,length):
        p = self.gen_prime(length / 2)
        q = self.gen_prime(length / 2)
        self.n = p * q
        fn = (p - 1) * (q - 1)
        while True:
            self.e = random.randint(0, fn)
            if math.gcd(self.e, fn) == 1:
                break
        self.d = 0
        while True:
            if (self.e * self.d) % fn == 1:
                break
            self.d += 1
            
    def getkey(self):
        self.genkeys(1024)
        self.PrivateKey = [self.n, self.d]
        self.PublicKey = [self.n,self.e]

    def miller_rabin(self,nn, k):
        if nn == 2:
            return True
        if nn % 2 == 0:
            return False
        r, s = 0, nn - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, nn - 1)
            x = pow(a, s, nn)
            if x == 1 or x == nn - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, nn)
                if x == nn - 1:
                    break
                else:
                    return False
        return True
   # b**e mod m
    def fast_mod(self,b, e, m):
        e=int(e)
        track = 2
        aim = [b]
        while track <= e:
            aim.append((aim[-1]**2) % m)
            track *= 2
        bin_str = bin(e)[2:][::-1]
        multiply = 1

        for i in range(len(bin_str)):
            if bin_str[i] == '1':
                multiply *= aim[i]
                multiply %= m
        return multiply
    

    def decrypt(self):
        self.decrypt_txt = ''
        for unit in self.secret:
            self.decrypt_txt += chr(self.fast_mod(ord(unit), int(self.d), int(self.n)))
        self.decrypt_txt = str(self.decrypt_txt)
        return self.decrypt_txt


    def encrypt(self):
        self.secret = ''
        for unit in self.msg:
            self.secret += chr(self.fast_mod(ord(unit), self.e, self.n))
        self.secret = bytes(self.secret.encode('utf-8')).__str__()
        return self.secret
 


