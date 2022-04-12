from tkinter import *
from tkinter.font import BOLD
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math
from PIL import _imaging
global path_image

image_display_size = 300, 300

def on_click1():
    
    global path_image
    
    path_image = filedialog.askopenfilename()
    
    load_image = Image.open(path_image)
    
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(app, image=render)
    img.image = render
    img.place(x=150, y=40)
    
def encrypt_data_into_image():
    global path_image
    data = txt.get(1.0, "end-1c")
    img = cv2.imread(path_image)
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    
    PixReq = len(data) * 3
    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0
    
    for i in range(RowReq + 1):
        
        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            
            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    
    cv2.imwrite("encrypted_image.png", img)
    
    success_label = Label(app, text="Encryption Successful!!",bg='white',fg='#09a100', font=("Times New Roman", 20,BOLD))
    success_label.pack(anchor='n',fill='x',pady=300)

def decrypt():

    
    global path_image
    on_click_button.destroy()
    encrypt_button.destroy()
    path_image = filedialog.askopenfilename()
    load = Image.open(path_image)
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(app, image=render)
    img.image = render
    img.place(x=150, y=43)

    
    img = cv2.imread(path_image)
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                
                data.append(bin(j[0])[-1])
                
                data.append(bin(j[1])[-1])
                
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                
                data.append(bin(j[0])[-1])
                
                data.append(bin(j[1])[-1])
                
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    message_label = Label(app, text="The decrypted Meassage:\n"+message, bg='white', font=("Times New Roman", 10))
    message_label.place(x=601, y=56)

def about():
    txt.destroy()
    Button_f1.destroy()
    on_click_button.destroy()
    encrypt_button.destroy()
    l1=Label(text="This Project is made by Following Students From VIIT,Pune",font=("Times New Roman",12))
    l1.pack()
    Str="1.Pramod Daware   8056\n2.Eeshan Bhanap   8057\n3.Rutik Jadhav    8058\n4.Akshay Kothule  8059\n5.Akash Rathod    "
    l2=Label(text=Str,anchor='w',font=('Times New Roman',11))
    l2.pack()
    
app = Tk()
app.configure(background='lavender')
app.title("Steganography Project")
app.geometry('900x700')
mainframe=Frame(app,bg="white",borderwidth=4)
mainframe.pack(side=TOP,fill="x")
startlabel=Label(mainframe,text="Steganography Project",bg="white",font=("Times New Roman",20))
startlabel.pack(side=TOP,fill="x")
Button_f1=Frame(app,bg="grey",borderwidth=6)
Button_f1.pack(side=LEFT,fill="y")
txt = Text(app, wrap=WORD, width=30)
txt.place(x=600, y=55, height=165)
Decrypt_button = Button(Button_f1, text="Start decrypting", bg='white', fg='black',relief="groov",command=decrypt)
Decrypt_button.pack(padx=10)
on_click_button = Button(app, text="Choose Image", bg='white', fg='black',borderwidth=1, command=on_click1)
on_click_button.place(x=250, y=235)
encrypt_button = Button(app, text="Encode", bg='white', fg='black', command=encrypt_data_into_image)
encrypt_button.place(x=600, y=235)
credits_Button=Button(Button_f1,text='Credits',command=about)
credits_Button.pack(side=BOTTOM,pady=10)
app.mainloop()




