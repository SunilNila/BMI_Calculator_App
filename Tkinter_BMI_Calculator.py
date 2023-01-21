from tkinter import *
import tkinter as tk
#import  PIL as pillow
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title('BMI Calculator')
#root.geometry('470x580')
root.geometry('580x640')
root.resizable(False, False)
root.configure(bg='#f0f1f5')


def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    #convert height to meter
    m = h/100
    bmi = round(float(w / m**2),1)
    label1.config(text=bmi)
    
    # if bmi < 18.5:
    #     label2.config(text='Classification: Under')
    #     label3.config(text='Health Risk: Minimal')
    # elif bmi > 18.5 and bmi <= 25:
    #     label2.config(text='Classification: Normal Weight')
    #     label3.config(text='Health Risk: Minimal')
    # elif bmi > 25 and bmi <= 30:
    #     label2.config(text='Classification: Overweight')
    #     label3.config(text='Health Risk: Increased')

    if bmi >= 40:
        label2.config(text='Classification: Morbidly Obese')
        label3.config(text='Health Risk: Extremely High')
    elif bmi >= 35:
        label2.config(text='Classification: Severely Obese')
        label3.config(text='Health Risk: Very High')
    elif bmi >= 30:
        label2.config(text='Classification: Obese')
        label3.config(text='Health Risk: High')
    elif bmi >= 25:
        label2.config(text='Classification: Overweight')
        label3.config(text='Health Risk: Increased')
    elif bmi >= 18.5:
        label2.config(text='Classification: Normal weight')
        label3.config(text='Health Risk: Minimal')
    elif bmi < 18.5:
        label2.config(text='Classification: Under weight')
        label3.config(text='Health Risk: Minimal')
    
#icon
image_icon = PhotoImage(file="./images/icon.png")
root.iconphoto(False, image_icon)

#top
top = PhotoImage(file='./images/top.png')
top_image = Label(root, image=top, background='#f0f1f5')
top_image.place(x=42, y=-10)

#bottom box
Label(root, width=82, height=18, bg='lightblue').pack(side=BOTTOM)

#two boxes
box = PhotoImage(file='./images/square-ios-app-256.png')
Label(root, image=box).place(x=20, y=87)
Label(root, image=box).place(x=300, y=87)

#scales img
scale = PhotoImage(file='./images/scale.png')
Label(root, image=scale, bg='lightblue').place(x=20, y=375)

#######Slider1#########
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open('./images/man.png'))
    resized_image = img.resize(50, 10 + size)
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image = photo2

#styling the slider
style = ttk.Style()
style.configure('TScale', background='white')
#current_value = tk.DoubleVar()
slider = ttk.Scale(root, from_= 0, to=220, orient='horizontal', style='TScale', command=slider_changed, variable=current_value)
slider.place(x=95, y=310)
########Slider1##########

#######Slider2#########
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed(event):
    Weight.set(get_current_value2())

#styling the slider
style2 = ttk.Style()
style2.configure('TScale', background='white')
#current_value = tk.DoubleVar()
slider2 = ttk.Scale(root, from_= 0, to=200, orient='horizontal', style='TScale', command=slider_changed, variable=current_value2)
slider2.place(x=380, y=310)
#######Slider2#########


#entry box 
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=CENTER)
height.place(x=55, y=170)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=CENTER)
weight.place(x=335, y=170)
Weight.set(get_current_value2())

#man image
secondimage = Label(root, bg='lightblue')
secondimage.place(x=70, y=530)


Button(root, text='View Report', width=15, height=2, font='arial 10 bold', bg='#1f6e68', fg='white', command=BMI).place(x=400, y=400)
label1  = Label(root, font='arial 60 bold', bg='lightblue', fg='#fff')
label1.place(x=110, y=380)

label2  = Label(root, font='arial 20 bold', bg='lightblue', fg='#3b3a3a')
label2.place(x=110, y=480)

label3  = Label(root, font='arial 10 bold', bg='lightblue')
label3.place(x=225, y=540)


#box weight/height indicator
#Height
label4 = Label(root, font='arial 10 bold', bg='#fff', fg='grey' )
label4.config(text='Height(cm)')
label4.place(x=115, y=100)

#Weight
label5 = Label(root, font='arial 10 bold', bg='#fff', fg='grey' )
label5.config(text='Weight(kg)')
label5.place(x=390, y=100)


root.mainloop()