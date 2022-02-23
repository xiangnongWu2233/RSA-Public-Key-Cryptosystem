from encoder import generate_key,fast_power,encoding,primality_test,toCode
from decoder import decoding,solve
from tkinter import Tk,Button,filedialog

def open_file():
    filename=filedialog.askopenfilename()
    return filename

class Encryption:
    def __init__(self):
        self.root=Tk()
        self.root.title('Encryption')

        self.Button1=Button(self.root,text='Generate Key',command=self.key)
        self.Button2=Button(self.root,text='Choose Rule')
        self.Button3=Button(self.root,text="Put message")

        self.Button1.pack()
        self.Button2.pack()
        self.Button3.pack()
        self.root.mainloop()

    def key(self):
        generate_key(10)


class Decryption:
    def __init__(self):
        self.root=Tk()
        self.root.title('Decryption')

class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title('RSA Public Key Cryptosystem')

        self.Button1 = Button(self.root, text='Practice')
        self.Button2 = Button(self.root, text='Encryption',command=self.encrypt)
        self.Button3 = Button(self.root, text='Decryption',command=self.decrypt)
        self.Button4 = Button(self.root, text='Attack')

        self.Button1.pack()
        self.Button2.pack()
        self.Button3.pack()
        self.Button4.pack()
        self.root.mainloop()

    def encrypt(self):
        e=Encryption()

    def decrypt(self):
        d=Decryption()

if __name__=="__main__":
    m=Menu()
