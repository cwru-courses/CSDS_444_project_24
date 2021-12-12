import random
import math

class RSA_text():

    def __init__(self):
        self.n = None
        self.e = None
        self.d = None
    
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

    def generate_keys(self):
        p = self.gen_prime(self.k / 2)
        q = self.gen_prime(self.k / 2)
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

    def miller_rabin(n, k):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def fast_exp(b, e, m): # b**e mod m
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
    
    


class APP:
    def __init__(self):
        self.n = ""
        self.e = ""
        self.d = ""
        self.msg = ""
        self.secret = ""

        self.root = tk.Tk()
        self.text = tk.StringVar(value="Private Key")
        self.text_pub = tk.StringVar(value="Public Key")

        self.root.title("RSA")
        self.root.rowconfigure(0, minsize=800, weight=1)
        self.root.columnconfigure(1, minsize=800, weight=1)

        self.txt_edit = tk.Text(self.root)
        self.fr_buttons = tk.Frame(self.root, relief=tk.RAISED, bd=2)
        self.btn_pri_key = tk.Button(self.fr_buttons, text="Generate Keys", command=self.gen_keys,
                                     highlightbackground='#3E4149')
        self.btn_open = tk.Button(self.fr_buttons, text="Open File", command=self.open_file,
                                  highlightbackground='#3E4149')
        self.btn_enc = tk.Button(self.fr_buttons, text="Encrypt", command=self.encrypt_msg,
                                 highlightbackground='#3E4149')
        self.dec_input = tk.Entry(self.fr_buttons)
        self.dec_input.insert(0, "Private Key: 000 000")
        self.btn_dec = tk.Button(self.fr_buttons, text="Decrypt", command=self.decrypt_msg,
                                 highlightbackground='#3E4149')
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=self.clear, highlightbackground='#3E4149')
        self.btn_save = tk.Button(self.fr_buttons, text="Save File", command=self.save_file,
                                  highlightbackground='#3E4149')
        self.statusbar_pri = tk.Label(self.fr_buttons, textvariable=self.text, bd=1, relief=tk.SUNKEN, anchor='center')
        self.statusbar_pub = tk.Label(self.fr_buttons, textvariable=self.text_pub, bd=1, relief=tk.SUNKEN, anchor='center')

        self.statusbar_pri.grid(row=0, column=0, sticky="nsew")
        self.statusbar_pub.grid(row=1, column=0, sticky="nsew")
        self.btn_pri_key.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.btn_open.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.btn_enc.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.dec_input.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.btn_dec.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
        self.btn_clear.grid(row=8, column=0, sticky="ew", padx=5)

        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")

        self.root.mainloop()

    def decrypt_msg(self):
        input = self.dec_input.get()
        if input:
            if "Private Key:" in input:
                input = input.split("Private Key:")[1]

        (n, d) = input.split()
        print(n, d)
        self.decrypt_txt = ''
        for unit in self.secret:
            self.decrypt_txt += chr(KeyGenerator.fast_exp(ord(unit), int(d), int(n)))
        self.decrypt_txt = str(self.decrypt_txt)

        self.txt_edit.insert(tk.END, str(self.decrypt_txt)[2:-1]+'\n\n')

    def encrypt_msg(self):

        print("encrypting...")

        self.secret = ''
        for unit in self.msg:
            self.secret += chr(KeyGenerator.fast_exp(ord(unit), self.e, self.n))

        self.txt_edit.insert(tk.END, bytes(self.secret.encode('utf-8')).__str__()[2:-1]+'\n\n')
        print("finish")

 

    def save_file(self):

        file_path = askdirectory(title=u'save path')
        print('save file: ', file_path)
        file_text = self.secret
        if file_path is not None:
            with open(file='/'.join([file_path, "encrypted"]), mode='w') as file:
                file.write(bytes(file_text.encode("utf-8")).__str__())
        file_text = self.decrypt_txt
        if file_path is not None:
            with open(file='/'.join([file_path, "decrypted"]), mode='w') as file:
                file.write(file_text)
        print('finish')

    def gen_keys(self):
        Keys = KeyGenerator(1024)
        Keys.generate_keys()
        self.n = Keys.n
        self.e = Keys.e
        self.d = Keys.d
        text = f"Private Key：{self.n} {self.d}"
        self.text.set(text)
        text_pub = f"Public Key: {self.n} {self.e}"
        self.text_pub.set(text_pub)


