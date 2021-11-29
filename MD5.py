from pip._vendor.distlib.compat import raw_input


class MD5_State:
    def __init__(self):
        # 初始化
        self.state = [0, 0, 0, 0]
        self.count = [0, 0]
        self.PADDING = ['\000'] * 64
        self.buffer = ['\000'] * 64

        self.count[0] = self.count[1] = 0
        self.state[0] = 0x67452301
        self.state[1] = 0xefcdab89
        self.state[2] = 0x98badcfe
        self.state[3] = 0x10325476

        self.PADDING[0] = chr(0x80)

    def __unsigned_int(self, x):
        # python中的数是可以无限大的
        # C中unsigned int的取值范围为0~4294967296一共4294967296个数字
        # 取余相当于c中unsigned int的越界截断
        return x % 4294967296

    # Python没有宏定义的概念，写成函数

    def __F(self, x, y, z):
        return ((x & y) | ((~x) & z)) & 0xffffffff

    def __G(self, x, y, z):
        return ((x & z) | (y & (~z))) & 0xffffffff

    def __H(self, x, y, z):
        return (x ^ y ^ z) & 0xffffffff

    def __I(self, x, y, z):
        return (y ^ (x | (~z))) & 0xffffffff

    def __ROTATE_LEFT(self, x, n):
        return (x << n) | (x >> (32 - n)) & 0xffffffff

    # Python中没有指针这一概念无法按地址传递，
    # 因此这里使用返回值

    def __FF(self, a, b, c, d, x, s, ac):
        ac = self.__unsigned_int(ac)
        a = self.__unsigned_int(a + self.__F(b, c, d) + x + ac)
        a = self.__unsigned_int(self.__ROTATE_LEFT(a, s))
        a = self.__unsigned_int(a + b)
        return a

    def __GG(self, a, b, c, d, x, s, ac):
        ac = self.__unsigned_int(ac)
        a = self.__unsigned_int(a + self.__G(b, c, d) + x + ac)
        a = self.__unsigned_int(self.__ROTATE_LEFT(a, s))
        a = self.__unsigned_int(a + b)
        return a

    def __HH(self, a, b, c, d, x, s, ac):
        ac = self.__unsigned_int(ac)
        a = self.__unsigned_int(a + self.__H(b, c, d) + x + ac)
        a = self.__unsigned_int(self.__ROTATE_LEFT(a, s))
        a = self.__unsigned_int(a + b)
        return a

    def __II(self, a, b, c, d, x, s, ac):
        ac = self.__unsigned_int(ac)
        a = self.__unsigned_int(a + self.__I(b, c, d) + x + ac)
        a = self.__unsigned_int(self.__ROTATE_LEFT(a, s))
        a = self.__unsigned_int(a + b)
        return a

    # Python允许返回多个返回值

    def Encode(self, output, input, len):
        i, j = 0, 0
        while j < len:
            # chr() ASCII码转为字符
            output[j] = chr(input[i] & 0xff)
            output[j + 1] = chr((input[i] >> 8) & 0xff)
            output[j + 2] = chr((input[i] >> 16) & 0xff)
            output[j + 3] = chr((input[i] >> 24) & 0xff)
            j += 4
            i += 1
        return output, input

    def Decode(self, output, input, len):
        i, j = 0, 0
        while j < len:
            # ord()就是输出字符的ASCII码
            output[i] = ord(input[j]) | (ord(input[j + 1]) << 8) | \
                (ord(input[j + 2]) << 16) | (ord(input[j + 3]) << 24)
            j += 4
            i += 1
        return output, input

    def MD5_Transform(self, state, block):
        a, b, c, d, x = state[0], state[1], state[2], state[3], [0] * 16

        x, block = self.Decode(x, block, 64)

        a = self.__FF(a, b, c, d, x[0], 7, 0xd76aa478)
        d = self.__FF(d, a, b, c, x[1], 12, 0xe8c7b756)
        c = self.__FF(c, d, a, b, x[2], 17, 0x242070db)
        b = self.__FF(b, c, d, a, x[3], 22, 0xc1bdceee)
        a = self.__FF(a, b, c, d, x[4], 7, 0xf57c0faf)
        d = self.__FF(d, a, b, c, x[5], 12, 0x4787c62a)
        c = self.__FF(c, d, a, b, x[6], 17, 0xa8304613)
        b = self.__FF(b, c, d, a, x[7], 22, 0xfd469501)
        a = self.__FF(a, b, c, d, x[8], 7, 0x698098d8)
        d = self.__FF(d, a, b, c, x[9], 12, 0x8b44f7af)
        c = self.__FF(c, d, a, b, x[10], 17, 0xffff5bb1)
        b = self.__FF(b, c, d, a, x[11], 22, 0x895cd7be)
        a = self.__FF(a, b, c, d, x[12], 7, 0x6b901122)
        d = self.__FF(d, a, b, c, x[13], 12, 0xfd987193)
        c = self.__FF(c, d, a, b, x[14], 17, 0xa679438e)
        b = self.__FF(b, c, d, a, x[15], 22, 0x49b40821)

        a = self.__GG(a, b, c, d, x[1], 5, 0xf61e2562)
        d = self.__GG(d, a, b, c, x[6], 9, 0xc040b340)
        c = self.__GG(c, d, a, b, x[11], 14, 0x265e5a51)
        b = self.__GG(b, c, d, a, x[0], 20, 0xe9b6c7aa)
        a = self.__GG(a, b, c, d, x[5], 5, 0xd62f105d)
        d = self.__GG(d, a, b, c, x[10], 9, 0x2441453)
        c = self.__GG(c, d, a, b, x[15], 14, 0xd8a1e681)
        b = self.__GG(b, c, d, a, x[4], 20, 0xe7d3fbc8)
        a = self.__GG(a, b, c, d, x[9], 5, 0x21e1cde6)
        d = self.__GG(d, a, b, c, x[14], 9, 0xc33707d6)
        c = self.__GG(c, d, a, b, x[3], 14, 0xf4d50d87)
        b = self.__GG(b, c, d, a, x[8], 20, 0x455a14ed)
        a = self.__GG(a, b, c, d, x[13], 5, 0xa9e3e905)
        d = self.__GG(d, a, b, c, x[2], 9, 0xfcefa3f8)
        c = self.__GG(c, d, a, b, x[7], 14, 0x676f02d9)
        b = self.__GG(b, c, d, a, x[12], 20, 0x8d2a4c8a)

        a = self.__HH(a, b, c, d, x[5], 4, 0xfffa3942)
        d = self.__HH(d, a, b, c, x[8], 11, 0x8771f681)
        c = self.__HH(c, d, a, b, x[11], 16, 0x6d9d6122)
        b = self.__HH(b, c, d, a, x[14], 23, 0xfde5380c)
        a = self.__HH(a, b, c, d, x[1], 4, 0xa4beea44)
        d = self.__HH(d, a, b, c, x[4], 11, 0x4bdecfa9)
        c = self.__HH(c, d, a, b, x[7], 16, 0xf6bb4b60)
        b = self.__HH(b, c, d, a, x[10], 23, 0xbebfbc70)
        a = self.__HH(a, b, c, d, x[13], 4, 0x289b7ec6)
        d = self.__HH(d, a, b, c, x[0], 11, 0xeaa127fa)
        c = self.__HH(c, d, a, b, x[3], 16, 0xd4ef3085)
        b = self.__HH(b, c, d, a, x[6], 23, 0x4881d05)
        a = self.__HH(a, b, c, d, x[9], 4, 0xd9d4d039)
        d = self.__HH(d, a, b, c, x[12], 11, 0xe6db99e5)
        c = self.__HH(c, d, a, b, x[15], 16, 0x1fa27cf8)
        b = self.__HH(b, c, d, a, x[2], 23, 0xc4ac5665)

        a = self.__II(a, b, c, d, x[0], 6, 0xf4292244)
        d = self.__II(d, a, b, c, x[7], 10, 0x432aff97)
        c = self.__II(c, d, a, b, x[14], 15, 0xab9423a7)
        b = self.__II(b, c, d, a, x[5], 21, 0xfc93a039)
        a = self.__II(a, b, c, d, x[12], 6, 0x655b59c3)
        d = self.__II(d, a, b, c, x[3], 10, 0x8f0ccc92)
        c = self.__II(c, d, a, b, x[10], 15, 0xffeff47d)
        b = self.__II(b, c, d, a, x[1], 21, 0x85845dd1)
        a = self.__II(a, b, c, d, x[8], 6, 0x6fa87e4f)
        d = self.__II(d, a, b, c, x[15], 10, 0xfe2ce6e0)
        c = self.__II(c, d, a, b, x[6], 15, 0xa3014314)
        b = self.__II(b, c, d, a, x[13], 21, 0x4e0811a1)
        a = self.__II(a, b, c, d, x[4], 6, 0xf7537e82)
        d = self.__II(d, a, b, c, x[11], 10, 0xbd3af235)
        c = self.__II(c, d, a, b, x[2], 15, 0x2ad7d2bb)
        b = self.__II(b, c, d, a, x[9], 21, 0xeb86d391)

        self.state[0] = self.__unsigned_int(self.state[0] + a)
        self.state[1] = self.__unsigned_int(self.state[1] + b)
        self.state[2] = self.__unsigned_int(self.state[2] + c)
        self.state[3] = self.__unsigned_int(self.state[3] + d)

        x = [0] * 16

    def MD5_Update(self, input, inputLen):
        index = (self.count[0] >> 3) & 0x3F
        self.count[0] += (inputLen << 3)

        if self.count[0] < (inputLen << 3):
            self.count[1] += 1
        self.count[1] += inputLen >> 29
        partLen = 64 - index

        if inputLen >= partLen:
            self.buffer[index:index + partLen] = input[:partLen]
            self.MD5_Transform(self.state, self.buffer)
            i = partLen
            while (i + 63) < inputLen:
                self.MD5_Transform(self.state, input[i])
                i += 64
            index = 0
        else:
            i = 0

        self.buffer[index:index + inputLen - i] = input[i:i + partLen]
        return input

    def MD5_Final(self, digest):
        bits = ['\000'] * 8
        bits, self.count = self.Encode(bits, self.count, 8)

        index = (self.count[0] >> 3) & 0x3f
        padLen = 56 - index if index < 56 else 120 - index
        self.MD5_Update(self.PADDING, padLen)

        self.MD5_Update(bits, 8)
        digest, self.state = self.Encode(digest, self.state, 16)
        self.__init__()
        return

    def md5_digest(self, strContent, iLength, output):
        strContent = self.MD5_Update(strContent, iLength)
        self.MD5_Final(output)
        return strContent


if __name__ == "__main__":
    key = input("Please input:")
    obj = MD5_State()
    buff = [''] * 16
    ciper = obj.md5_digest(key, len(key), buff)
    print("deciper_text =")
    str = ''
    for i in range(16):
        str+="%x" % ((ord(buff[i]) & 0xF0) >> 4)
        str+="%x" % (ord(buff[i]) & 0x0F)
        print("%x" % ((ord(buff[i]) & 0xF0) >> 4), end='')
        print("%x" % (ord(buff[i]) & 0x0F), end='')
    print(str)




