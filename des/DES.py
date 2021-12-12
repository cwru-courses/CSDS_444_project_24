import time

import cv2
import libnum
import numpy as np
import scipy.io as io


class DES():

    def __init__(self):
        self.IP_Table = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        ]

        self.left_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        self.key = []
        self.Sub_key_C = []
        self.Sub_key_D = []

        self.CD = []
        self.kk = []

        self.PC_1 = [
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

        self.PC_2 = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

        self.S1 = [
            14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
            0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
            4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
            15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
        ]

        self.S2 = [
            15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
            3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
            0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
            13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
        ]

        self.S3 = [
            10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
            13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 4, 12, 11, 15, 1,
            13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
            1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
        ]

        self.S4 = [
            7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
            13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
            10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
            3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
        ]

        self.S5 = [
            2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
            14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
            4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
            11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
        ]

        self.S6 = [
            12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
            10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
            9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
            4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
        ]

        self.S7 = [
            4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
            13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
            1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
            6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
        ]

        self.S8 = [
            13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
            1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
            7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
            2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
        ]
        self.S = [self.S1, self.S2, self.S3, self.S4, self.S5, self.S6, self.S7, self.S8]

        self.P = [16, 7, 20, 21,
                  29, 12, 28, 17,
                  1, 15, 23, 26,
                  5, 18, 31, 10,
                  2, 8, 24, 14,
                  32, 27, 3, 9,
                  19, 13, 30, 6,
                  22, 11, 4, 25]
        self.E_BIT_SELECTION_table = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]

        self.Inverse_IP_table = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        ]
        self.key_new = []

    def generate_subkey(self, key):
        C = []
        D = []
        new_key = self.IP_Replacement(key, 1)
        C0 = new_key[0:int(len(new_key) / 2)]
        D0 = new_key[int(len(new_key) / 2):int(len(new_key))]
        C.append(''.join(C0))
        D.append(''.join(D0))

        for i in range(0, 16, 1):
            sub_C = C[i][self.left_shift[i]:len(C[i])] + C[i][0:self.left_shift[i]]
            sub_D = D[i][self.left_shift[i]:len(D[i])] + D[i][0:self.left_shift[i]]
            C.append(''.join(sub_C))
            D.append(''.join(sub_D))
        for index in range(0, 17, 1):
            self.Sub_key_D.append(''.join(D[index]))
            self.Sub_key_C.append(''.join(C[index]))
        self.subkey_two()

    def subkey_two(self):
        c = [self.Sub_key_C[i] + self.Sub_key_D[i] for i in range(1, 17, 1)]
        # for i in range(1, 17, 1):
        #     c.append(self.Sub_key_C[i] + self.Sub_key_D[i])
        for data in c:
            mmmm = [data[index - 1] for index in self.PC_2]
            # for index in self.PC_2:
            #     mmmm.append(data[index - 1])
            self.key.append(''.join(mmmm))

    # 8 bits
    def binary2eight(self, single_char):
        temp = bin(ord(single_char))
        temp = temp[2:len(temp)]
        while len(temp) < 8:
            temp = "0" + temp
        return temp

    def IP_Replacement(self, text, categeory):
        new_text = []
        if categeory == 1:
            new_text = [text[replacement - 1] for replacement in self.PC_1]
            # for replacement in self.PC_1:
            #     new_text.append(text[replacement - 1])
        elif categeory == 2:
            new_text = [text[replacement - 1] for replacement in self.E_BIT_SELECTION_table]
            # for replacement in self.E_BIT_SELECTION_table:
            #     new_text.append(text[replacement - 1])
        elif categeory == 3:
            new_text = [text[replacement - 1] for replacement in self.Inverse_IP_table]
            # for replacement in self.Inverse_IP_table:
            #     new_text.append(text[replacement - 1])
        else:
            new_text = [text[replacement - 1] for replacement in self.IP_Table]
            # for replacement in self.IP_Table:
            #     new_text.append(text[replacement - 1])
        return ''.join(new_text)

    def E_function(self, R):
        return self.IP_Replacement(R, 2)

    def S_box(self, B, num):
        B_new = ''.join(B)
        first = B_new[0] + B_new[-1]
        first = '0b' + first
        second = B_new[1:-1]
        second = '0b' + second
        S_num = self.S[num]
        # a = int(first, 2)
        # b = int(second, 2)
        # c = a*16+b
        # d = S_num[c]
        return str(S_num[int(first, 2) * 16 + int(second, 2)])

    def ten2two(self, key):
        temp = bin(int(key, 10))
        temp = temp[2:len(temp)]
        while len(temp) < 8:
            temp = "0" + temp
        return temp

    def f_function(self, R, K):
        E_R = self.E_function(R)
        f_R = []
        element = []
        element = [str(int(E_R[i]) ^ int(K[i])) for i in range(len(E_R))]
        # for i in range(len(E_R)):
        #     element.append(str(int(E_R[i]) ^ int(K[i])))
        f_R = [self.ten2two(self.S_box(element[6 * j:6 * (j + 1)], j)) for j in range(8)]
        # for j in range(8):
        #     # print(self.S_box(element[6 * j:6 * (j + 1)], j))
        #     # new_element = element[6 * j:6 * (j + 1)]
        #     new_box = self.S_box(element[6 * j:6 * (j + 1)], j)
        #     f_R.append(self.ten2two(new_box))
        return ''.join(f_R)

    def transfor(self, R, num):
        new_R = []
        f_result = self.f_function(R, self.key[num])
        new_R = [f_result[self.P[i] - 1] for i in range(32)]
        # for i in range(32):
        #     new_R.append()
        return ''.join(new_R)

    def setKey(self, key):
        now_key = []
        num = 0
        for i in key:
            num = num + 1
            k = bin(ord(i))[2:]
            while len(k) < 8:
                k = "0" + k
            now_key.append(k)
            if num == 8:
                break
        # print(''.join(now_key))
        return ''.join(now_key)

    def LplusR(self, L, f):
        result = [str(int(L[i]) ^ int(f[i])) for i in range(32)]
        # for i in range(32):
        #     result.append(str(int(L[i]) ^ int(f[i])))
        return ''.join(result)

    def process(self, plaintext, type):
        if type == 0:
            L = plaintext[0:int(len(plaintext) / 2)]
            R = plaintext[int(len(plaintext) / 2):len(plaintext)]
            for i in range(16):
                new_L = L
                new_R = R
                L = new_R
                R = self.LplusR(self.transfor(new_R, i), new_L)
        else:
            L = plaintext[0:int(len(plaintext) / 2)]
            R = plaintext[int(len(plaintext) / 2):len(plaintext)]
            for i in range(16):
                new_L = L
                new_R = R
                L = new_R
                R = self.LplusR(self.transfor(new_R, 15 - i), new_L)
        return self.IP_Replacement(R + L, 3)

    def encryption(self, key, file, type):
        bin_key = self.setKey(key)
        self.generate_subkey(bin_key)
        if type == 1:
            text = ''

            for i in file:
                print(i, ord(i))
                m = bin(ord(i))
                k = m[2:]
                while len(k) < 8:
                    k = "0" + k
                text = text + k

            len_text = 0
            len_true = 0
            if len(text) % 64 == 0:
                len_text = int(len(text) / 64)
                len_true = 0
            else:
                len_text = int(len(text) / 64) + 1
                len_true = 1

            pt = ''
            for m in range(int(len_text)):
                if m != len_text - 1:
                    plaintext = self.IP_Replacement(text[m * 64:m * 64 + 64], 0)
                    pt += self.process(plaintext, 0)
                    # print(pt)
                elif len_true == 0:
                    plaintext = self.IP_Replacement(text[m * 64:], 0)
                    pt += self.process(plaintext, 0)
                    # print(pt)
                else:
                    n_text = text[m * 64:]
                    while len(n_text) < 64:
                        n_text = n_text + "0"
                    plaintext = self.IP_Replacement(n_text, 0)
                    pt += self.process(plaintext, 0)
                    # print(pt)
            pp = ''
            # print(len(pt))
            for i in range(int(len(pt) / 4)):
                # print(i)
                # print(pt[i * 4:i * 4 + 4])
                pp += hex(int('0b' + pt[i * 4:i * 4 + 4], 2))[2:]
            # print(len(pp))
            f = open('DES_cipher.txt', 'w')
            f.write(pp)
            f.close()
            return pp
        elif type == 0:
            length_one = file.shape[0]
            length_two = file.shape[1]
            length_three = file.shape[2]
            print(length_one,length_two,length_three)
            one = file.reshape(1, length_one * length_two * length_three)[0].tolist()
            multiple = 0
            if len(one) % 8 != 0:
                multiple = 1
            while len(one) % 8 != 0:
                one.append(0)
            len_data = int(len(one) / 8)
            cipher_result = []
            for data_i in range(len_data):
                data_str = ''
                for i in one[data_i * 8:data_i * 8 + 8]:
                    # print(i)
                    m = bin(i)
                    k = m[2:]
                    while len(k) < 8:
                        k = "0" + k
                    data_str = data_str + k
                plaintext = self.IP_Replacement(data_str, 0)
                pt = self.process(plaintext, 0)
                pp = [int('0b' + pt[i * 8:i * 8 + 8], 2) for i in range(int(len(pt) / 8))]
                # for i in range(int(len(pt) / 8)):
                #     pp.append(int('0b' + pt[i * 8:i * 8 + 8], 2))
                cipher_result += pp
            if multiple == 0:
                cv2.imwrite("cipher_galaxy.png", np.array(cipher_result).reshape(length_one, length_two, length_three))
            else:
                mat_path = 'cipher_galaxy.mat'
                io.savemat(mat_path, {'name': np.array(cipher_result)})
                dimension_path = 'dimension.mat'
                dimension_array = np.array([length_one, length_two, length_three])
                io.savemat(dimension_path, {'dimension': np.array(dimension_array)})
            return cipher_result
        else:
            length_one = int(file.get(cv2.CAP_PROP_FRAME_COUNT))
            length_two = int(file.get(cv2.CAP_PROP_FRAME_WIDTH))
            length_three = int(file.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = file.get(cv2.CAP_PROP_FPS)
            array_o = np.empty((length_one, length_three, length_two, 3), np.dtype('uint8'))

            num = 0
            ret = True

            while (num < length_one and ret):
                ret, array_o[num] = file.read()
                num += 1

            # length_one = file.shape[0]
            # length_two = file.shape[1]
            # length_three = file.shape[2]
            print(length_one, length_two, length_three)
            one = array_o.reshape(1, length_one * length_two * length_three*3)[0].tolist()
            multiple = 0
            if len(one) % 8 != 0:
                multiple = 1
            while len(one) % 8 != 0:
                one.append(0)
            len_data = int(len(one) / 8)
            cipher_result = []
            for data_i in range(len_data):
                data_str = ''
                for i in one[data_i * 8:data_i * 8 + 8]:
                    # print(i)
                    m = bin(i)
                    k = m[2:]
                    while len(k) < 8:
                        k = "0" + k
                    data_str = data_str + k
                plaintext = self.IP_Replacement(data_str, 0)
                pt = self.process(plaintext, 0)
                pp = [int('0b' + pt[i * 8:i * 8 + 8], 2) for i in range(int(len(pt) / 8))]
                cipher_result += pp
            if multiple == 0:
                fourcc = cv2.VideoWriter_fourcc(*'MP42')
                data_encrypted = np.array(cipher_result).reshape(length_one,length_three,length_two,3)

                array_code = np.array(data_encrypted, dtype=np.uint8)
                video = cv2.VideoWriter('encode.mp4', fourcc, float(fps), (length_two, length_three))

                for count in range(length_one):
                    img = array_code[count]
                    video.write(img)

                video.release()
                # cv2.imwrite("cipher_galaxy.png", np.array(cipher_result).reshape(length_one, length_two, length_three))
            else:
                mat_path = 'cipher_galaxy.mat'
                io.savemat(mat_path, {'name': np.array(cipher_result)})
                dimension_path = 'dimension.mat'
                dimension_array = np.array([length_one, length_two, length_three])
                io.savemat(dimension_path, {'dimension': np.array(dimension_array)})
            return cipher_result

    def decryption(self, key, file, type):
        bin_key = self.setKey(key)
        self.generate_subkey(bin_key)
        # print(len(file))
        if type == 1:
            text = ''

            for i in file:
                # print(i)
                k = bin(int('0x' + i, 16))[2:]
                while len(k) < 4:
                    k = "0" + k
                text = text + k
            len_cipher = int(len(text) / 64)

            pt = ''
            for m in range(len_cipher):
                if m == len_cipher - 1:
                    plaintext = self.IP_Replacement(text[m * 64:], 0)
                    ptt = self.process(plaintext, 1)
                    pttt = ''
                    for f in range(8):
                        if ptt[f * 8:f * 8 + 8] == '00000000':
                            break
                        else:
                            pttt += ptt[f * 8:f * 8 + 8]
                    pt += pttt
                else:
                    plaintext = self.IP_Replacement(text[m * 64:m * 64 + 64], 0)
                    pt += self.process(plaintext, 1)
            pp = ''
            for i in range(int(len(pt) / 8)):
                pp += chr(int('0b' + pt[i * 8:i * 8 + 8], 2))
            return pp
        else:
            num_dimension = 0
            if isinstance(file, dict):
                num_dimension = 2
                file = file['name'][0]
                dimension_path = 'dimension.mat'

                data = io.loadmat(dimension_path)
                data = data['dimension']
                data = data[0]
                length_one = data[0]
                length_two = data[1]
                length_three = data[2]
                len_data = int(len(file) / 8)
                data = file.tolist()
            else:
                num_dimension = 3
                length_one = file.shape[0]
                length_two = file.shape[1]
                length_three = file.shape[2]
                len_data = int(length_one * length_two * length_three / 8)
                data = file.reshape(1, length_one * length_two * length_three)[0].tolist()
            # dimension_path = 'dimension.mat'
            # num_dimension = file.ndim
            # if num_dimension == 2:
            #     data = io.loadmat(dimension_path)
            #     data = data['dimension']
            #     length_one = data[0]
            #     length_two = data[1]
            #     length_three = data[2]
            #     len_data = int(file.shape[0] * file.shape[1] / 8)
            #     data = file.reshape(1, file.shape[0] * file.shape[1])[0].tolist()
            # else:
            #     length_one = file.shape[0]
            #     length_two = file.shape[1]
            #     length_three = file.shape[2]
            #     len_data = int(length_one * length_two * length_three / 8)
            #     data = file.reshape(1, length_one * length_two * length_three)[0].tolist()
            cipher_result = []
            for data_i in range(len_data):
                data_str = ''
                for i in data[data_i * 8:data_i * 8 + 8]:
                    # print(i)
                    m = bin(i)
                    k = m[2:]
                    while len(k) < 8:
                        k = "0" + k
                    data_str = data_str + k
                plaintext = self.IP_Replacement(data_str, 0)
                pt = self.process(plaintext, 1)
                pp = [int('0b' + pt[i * 8:i * 8 + 8], 2) for i in range(int(len(pt) / 8))]
                # for i in range(int(len(pt) / 8)):
                #     pp.append(int('0b' + pt[i * 8:i * 8 + 8], 2))
                cipher_result += pp
            if num_dimension == 2:
                final_result = np.array(cipher_result[0:length_one*length_two*length_three]).reshape(length_one, length_two, length_three)
            else:
                final_result = np.array(cipher_result[0:]).reshape(length_one, length_two, length_three)
            cv2.imwrite("final_galaxy.png", final_result)
            return final_result


if __name__ == "__main__":
    start = time.time()
    key = 'jiede2323'
    # with open('pppp5.txt', 'r') as f:
    #     text1 = f.read()
    # f.close()
    # with open('DES_cipher.txt', 'r') as f1:
    #     mi = f1.read()
    # f1.close()
    #
    # des = DES()
    # print(des.encryption(key, text1,1))
    # des1 = DES()
    # cipher_text = des1.decryption(key, mi, 1)
    # end = time.time()
    # print(end - start)

    # print(cipher_text)
    # f = open('cipher.txt', 'w')
    # f.write(cipher_text)

    # des = DES()
    # mi = des.encryption(key, text1,0)
    # print(mi)
    # des1 = DES()
    # cipher_text = des1.decryption(key, mi,0)
    # print(cipher_text)
    # 9.567644119262695
    # encrypt picture
    # plain_image = cv2.imread('no60.jpg')
    # des = DES()
    # cipher = des.encryption(key, plain_image, 0)
    # decrypt picture
    # cipher_image = cv2.imread('cipher_galaxy.png')
    # cipher_image = io.loadmat('cipher_galaxy.mat')
    # des = DES()
    # cipher = des.decryption(key, cipher_image, 0)
    #encrypt video
    plain_video = cv2.VideoCapture('video1.mp4')
    des = DES()
    cipher = des.encryption(key, plain_video, 2)

    end = time.time()
    print(end - start)
