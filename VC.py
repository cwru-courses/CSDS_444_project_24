


class Vigenere():

    def __init__(self):
        self.asciilist = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
                     '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
                     '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
        bytelist = []
        for index, i in enumerate(self.asciilist):
            index_out = bytes(self.asciilist[index], 'utf-8')
            bytelist.append(index_out)
        #
        # print(bytelist)

    def generate_key(self, string, key):
        key = list(key)
        if len(string) == len(key):
            return key
        else:
            # key cannot be longer that the plain text
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

        # The join() method takes all items in an iterable and joins them into one string.

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
            cipher_text += self.asciilist[(self.asciilist.index(string[i]) + self.asciilist.index(key[i % len(key)])) % len(self.asciilist)]
        return cipher_text

    def original_text(self, cipher_text, key):
        '''msg = []
        output = ''
        for char in cipher_text:
            if ord(char) in range(65,91):
                msg.append((ord(char)-65,0))
            elif ord(char) in range(97,123):
                msg.append((ord(char)-97,1))
            else:
                msg.append(char)
        key = [ord(char) - 65 for char in key.lower()]
        for i in range(len(msg)):
            if type(msg[i]) == type('') : output += msg[i]
            else:
                    value = (msg[i][0] - key[i % len(key)]) % 26
                    output += chr(value + 65 + msg[i][1]*32)
        return output'''
        output = ""
        for i in range(len(cipher_text)):
            if cipher_text[i] not in self.asciilist:
                output += cipher_text[i]
            output += self.asciilist[(self.asciilist.index(cipher_text[i]) - self.asciilist.index(key[i % len(key)])) % len(self.asciilist)]
        return output

#
# # if __name__ == "__main__":
# Vc = Vigenere()
# Vc_string = input("string:")
# bytestring = bytearray(Vc_string, 'utf-8')
# print(bytestring)
#
# Vc.key = input("key:")
# # KeyWord = Vc.generate_key(Vc.string, Vc.key)
# # print(KeyWord)
# CipherText = Vc.cipherText(Vc_string, Vc.key)
# print("CipherText:", CipherText)
# PlainText = Vc.original_text(CipherText, Vc.key)
# print("Originaltext:", PlainText)
