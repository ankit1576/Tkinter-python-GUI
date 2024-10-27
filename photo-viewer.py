from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_image():
    global counter
    image_label.config(image=img_array[counter%len(img_array)])
    counter=counter+1


counter=1
root=Tk()
root.title('Photo viewer')
root.geometry('500x500')

files=os.listdir('images')
img_array=[]
for i in files:
    img=Image.open(os.path.join('images',i))
    resized_img=img.resize((400,400))
    img_array.append(ImageTk.PhotoImage(resized_img))

image_label=Label(root,image=img_array[0])
image_label.pack()

next_btn=Button(root,text='Next',bg='white',fg='black',width=15,height=2,command=rotate_image)
next_btn.pack(pady=(15,10))

root.mainloop();