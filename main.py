from encoder import generate_key,fast_power,encoding,primality_test,toCode
from decoder import decoding,solve
from tkinter import Tk,Button

def main():
    root=Tk()
    root.title('RSA Public Key Cryptosystem')

    Button1=Button(root,text='Practice')
    Button2=Button(root,text='Encryption')
    Button3=Button(root,text='Attack')


    Button1.pack()
    Button2.pack()
    Button3.pack()
    root.mainloop()

if __name__=="__main__":
    main()
