from tkinter import *
import base64

root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Message encoding and decoding')

Text=StringVar()
private_key=StringVar()
mode=StringVar()
Result = StringVar()

Label(root, text= 'Encode Decode', font='arial 20 bold').pack(side=TOP)
Label(root, text= 'Secure your information', font='arial 20 bold').pack(side=BOTTOM)

def Encode(key,message):
    enc = []
    for i in range(len(message)):
        key_c = key[i%len(key)]
        enc.append(chr((ord(message[i])+ord(key_c))%256))
    return base64.urlsafe_b64encode(''.join(enc).encode())

x=Encode('1234','hello')
print(x)

y=Encode('xyz','Secure your info')
print(y)

def Decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i%len(key)]
        dec.append(chr((256+ord(message[i])-ord(key_c))%256))
    return ''.join(dec)

#Example-
x1=Decode('1234','wpnCl8KfwqDCoA==')
print(x1)

y1=Decode('xyz', 'w4vDnsOdw63Dq8OfwpjDssOpw63Dq8Kaw6HDp8Ogw6c=')
print(y1)

#GUI for the Message encoder and decoder
def Mode():
    if(mode.get()=='e'):
        Result.set(Encode(private_key.get(),Text.get()))
    elif(mode.get()=='d'):
        Result.set(Decode(private_key.get(),Text.get()))
    else:
        Result.set('Invalid mode')
def Exit():
    root.destroy()
def Reset():
    Text.set('')
    private_key.set('')
    mode.set('')
    Result.set('')

Label(root,font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root,font='arial 10',textvariable=Text, bg='ghost white').place(x=290,y=60)

Label(root,font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(root,font='arial 10',textvariable=private_key, bg='ghost white').place(x=290,y=90)

Label(root,font='arial 12 bold', text='MODE').place(x=60, y=120)
Entry(root,font='arial 10',textvariable=mode, bg='ghost white').place(x=290,y=120)


Entry(root,font='arial 10',textvariable=Result, bg='ghost white').place(x=290,y=150)

Button(root,font='arial 10 bold', text='RESULT', bg='LightGrey', command=Mode).place(x=60, y=150)

Button(root,font='arial 10 bold', text='RESET', bg='LimeGreen', command=Reset).place(x=60, y=180)

Button(root,font='arial 10 bold', text='EXIT', bg='LightGrey', command=Exit).place(x=60, y=220)

root.mainloop()
