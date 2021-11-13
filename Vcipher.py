#python code to implement Vigenere Cipher


# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text

class Vigenere():

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
        cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i % len(key)])) % 26
            #ord():It takes a character (a string of length 1) 
            #as a parameter 
            #and returns the corresponding ASCII value or Unicode value
            x += ord('A')
            cipher_text.append(chr(x))
            #chr() takes an integer in the range (256) (that is, 0～255) as a parameter
            #and returns a corresponding character
            #The return value is the ASCII character
            #corresponding to the current integer
        return ("".join(cipher_text))

    def original_text(self,cipher_text, key):
        original = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(key[i % len(key)]) + 26) % 26
            x += ord('A')
            original.append(chr(x))

        return ("".join(original))


if __name__ == "__main__":
    Vc = Vigenere()
    Vc.string = input("string:")
    stringup = Vc.string.upper()
    Vc.key = input("key:")
    keyup = Vc.key.upper()
    KeyWord = Vc.generate_key(stringup, keyup)
    print(KeyWord)
    CipherText = Vc.cipherText(stringup, keyup)
    print("CipherText:", CipherText)
    PlainText = Vc.original_text(CipherText, keyup)
    print("Originaltext:", PlainText)



    
    

         
        