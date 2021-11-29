import random
from math import pow
import gmpy2 as gy
import time
import libnum



class Paillier(object):

    def __init__(self, pubKey=None, priKey=None):
        self.pubKey = pubKey
        self.priKey = priKey

    def __gen_prime__(self, rs):
        p = gy.mpz_urandomb(rs, 1024)
        while not gy.is_prime(p):
            p += 1
        return p

    def __div__(self, x, n):
        res = gy.div((x - 1), n)
        return res

    def __key_gen__(self):
        # generate random state
        while True:

            rs = gy.random_state(int(time.time()))
            p = self.__gen_prime__(rs)
            q = self.__gen_prime__(rs)
            n = p * q
            lmd = (p - 1) * (q - 1)

            if gy.gcd(n, lmd) == 1:
                break

        g = n + 1
        mu = gy.invert(lmd, n)

        self.pubKey = [n, g]
        self.priKey = [lmd, mu]
        return

    def decrypt(self, ciphertext):
        n, g = self.pubKey
        lmd, mu = self.priKey
        m = self.__div__(gy.powmod(ciphertext, lmd, n ** 2), n) * mu % n
        print("raw message:", m)
        plaintext = libnum.n2s(int(m))
        return plaintext

    def encrypt(self, plaintext):
        m = libnum.s2n(plaintext)
        n, g = self.pubKey
        r = gy.mpz_random(gy.random_state(int(time.time())), n)
        while gy.gcd(n, r) != 1:
            r += 1
        ciphertext = gy.powmod(g, m, n ** 2) * gy.powmod(r, n, n ** 2) % (n ** 2)
        return ciphertext


if __name__ == "__main__":
    x = 2
    y = 3

    string = "make american great again"

    byte = bytes(string, 'utf-8')

    p = Paillier()
    p.__key_gen__()
    # Key = p.pubKey

    plaintext = byte
    print("Plaintext:", plaintext)

    ciphertext = p.encrypt(plaintext)
    print("Ciphertext:", ciphertext)

    deciphertext = p.decrypt(ciphertext)
    print("Deciphertext: ", deciphertext)