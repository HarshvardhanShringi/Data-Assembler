from cryptography.fernet import Fernet
import tkinter
from tkinter import IntVar
from tkinter import font
from tkinter import filedialog


def openfile():
    global filepath
    filepath=filedialog.askopenfilename()
    g=tkinter.Label(m,text=filepath)
    g.pack()

def encryption():
    kfile_path=b'C:\Program Files\Dell\Update\key.txt'
    g = open(kfile_path, 'rb')
    k=g.read()
    token=Fernet(k)
    orig_file_path=filepath
    file = open(orig_file_path,'rb')
    orig_data = file.read()
    enc_data = token.encrypt(orig_data)
    file1 = open(orig_file_path, 'wb')
    file1.write(enc_data)

def decryption():
    kfile_path=b'C:\Program Files\Dell\Update\key.txt'
    g = open(kfile_path, 'rb')
    k=g.read()
    token=Fernet(k)
    dec_file_path=filepath
    file2= open(dec_file_path, 'rb')
    enc_data = file2.read()
    dec_data = token.decrypt(enc_data)
    file3 = open(dec_file_path, 'wb')
    file3.write(dec_data)



def isbutton_checked():
    e_text = namvar.get()
    if CheckVar2==1 and e_text=='hukum':
        encryption()
        gg=tkinter.Label(m,text='encryption successfull')
        gg.pack(side='top')
    if CheckVar1==1 and e_text=='hukum':
        decryption()
        gg1 = tkinter.Label(m, text='decryption successfull')
        gg1.pack(side='top')

# main window
m=tkinter.Tk()
m.geometry('1600x1000')
m.title('practise')


# buttons
but=tkinter.Button(m,activebackground='cyan',text='Start',command=isbutton_checked,width=14,height=1,font=15,bd=6,bg='white')
but.pack(side='bottom',pady=150)
but2=tkinter.Button(m,activebackground='cyan',command=openfile,text='select file',width=14,height=1,font=10,bd=2,bg='white')
but2.pack(side='top',pady=60,padx=30)

# entry
namvar=tkinter.StringVar()

entry=tkinter.Entry(m,width=30,textvariable=namvar)
entry.pack(side='bottom',pady=0)



# checkbutton
CheckVar1 = IntVar()
CheckVar2 = IntVar()
myFont = font.Font(size=12)
C1 = tkinter.Checkbutton(m, text = "Decryption", variable = CheckVar1,offvalue=0,onvalue=1, height=0,width = 20,font=myFont)
C2 = tkinter.Checkbutton(m, text = "Encryption", variable = CheckVar2,offvalue=0,onvalue=1, height=0,width = 20,font=myFont)
C1.pack(side='bottom',pady=60)
C2.pack(side='bottom',pady=0)




m.mainloop()
