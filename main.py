import pygame
import os
from encoder import generate_key,encoding
from decoder import decoding
from tkinter import Tk,Button,Entry,filedialog

def open_file():
    filename=filedialog.askopenfilename()
    return filename

class Encryption:
    def __init__(self):
        self.root=Tk()
        self.root.title('Encryption')

        self.Button1=Button(self.root,text='Generate Key',command=self.key)
        self.Button2=Button(self.root,text='Choose Rule',command=self.process_file)
        entry=Entry(self.root)
        self.Button3=Button(self.root,text="Encode",command=self.encode)

        self.Button1.pack()
        self.Button2.pack()
        entry.pack()
        self.message = entry.get()
        self.Button3.pack()
        #self.root.mainloop()



    def key(self):
        generate_key(10)

    def process_file(self):
        path=open_file()
        rule=open(path,'r');
        self.m=rule.readline()
        self.k=rule.readline()

    def encode(self):
        code=encoding(self.message,self.k,self.m)
        if os.path.exists('Message') == False:
            os.mkdir('Message')
        path_code = os.path.join('Message', 'code.txt');
        code_file=open(path_code,'w')
        print(code)
        for i in code:
            code_file.write(i+',')
        code_file.close()

class Decryption:
    def __init__(self):
        self.root=Tk()
        self.root.title('Decryption')

class Tester:
    def __init__(self):
        self.root=Tk()
        self.root.title('Test')
        self.message="This is an implementation of the RSA public key cryptosystem"
        self.Button1=Button(self.root,text='Generate Key',command=self.key)
        self.Button2=Button(self.root,text="Encode",command=self.encode)
        self.Button3=Button(self.root,text="Decode",command=self.decode)
        self.Button4=Button(self.root,text="Update",command=self.update)

        self.Button1.pack()
        self.Button2.pack()
        self.Button3.pack()
        self.Button4.pack()
        self.root.mainloop()

    def key(self):
        generate_key(10)

    def encode(self):
        self.code=encoding(self.message,self.m,self.k)

    def decode(self):
        message=decoding(self.k,self.p,self.q,self.code)
        print(message)

    def update(self):
        rule = open('Table/rule.txt', 'r')
        key = open('Table/key.txt', 'r')

        self.m = int(rule.readline())
        self.k = int(rule.readline())

        self.p = int(key.readline())
        self.q = int(key.readline())



class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title('RSA Public Key Cryptosystem')

        self.Button1 = Button(self.root, text='Test',command=self.Test)
        self.Button2 = Button(self.root, text='Encryption')
        self.Button3 = Button(self.root, text='Decryption')
        self.Button4 = Button(self.root, text='Attack')

        self.Button1.pack()
        self.Button2.pack()
        self.Button3.pack()
        self.Button4.pack()
        self.root.mainloop()

    def Test(self):
        t=Tester()

if __name__=="__main__":
    m=Menu()
