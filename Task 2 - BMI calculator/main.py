
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

app=Tk()
app.geometry("650x650+300+200")
app.resizable(False,False)
app.config(bg="#f5f0e1")
app.title("BMI Calculator")


def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    #convert height into meter
    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="Underweight!")
        label3.config(text="Your body weight is too low to be healthy.")



    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="You have a healthy body weight.")

    elif bmi>25 and bmi<=30:
        label2.config(text="Overweight!")
        label3.config(text="Your body weight is slightly above a weight considered healthy")

    else:
        label2.config(text="Obese!")
        label3.config(text="Your body weight is too high to be healthy. \nHealth may be at risk")
    
        

#icon
image_icon = PhotoImage(file = "bmi images/topicon.png")
app.iconphoto(False,image_icon)

#top
top = PhotoImage(file="bmi images/head.png")
top_image = Label(app,image=top,background="#f5f0e1")
top_image.place(x=-10,y=-10)

#bottom
Label(app,height=20,width=94,bg="lightblue").pack(side=BOTTOM)

#2boxes
box=PhotoImage(file="bmi images/box.png")
Label(app,image=box,bg="#f5f0e1").place(x=80,y=120)
Label(app,image=box,bg="#f5f0e1").place(x=350,y=120)


#scale
scale=PhotoImage(file="bmi images/scale.png")
Label(app,image=scale,bg="lightblue").place(x=50,y=370)


#############################Slider1###########################
current_value=tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    size = int(float(get_current_value()))
    img = (Image.open("bmi images/man.png"))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=120,y=610-size)
    secondimage.image=photo2

#command to change bgcolor of scale
style= ttk.Style()
style.configure("TScale",background="white")

slider=ttk.Scale(app,from_=0, to=220,orient="horizontal",style="TScale",
                 command=slider_changed,variable=current_value)
slider.place(x=140,y=260)







#############@@@@@@@@@@@@@@Slider 2@@@@@@@@@@@@@!#############

current_value2=tk.DoubleVar()

def get_current_value2():
    return "{: .2f}".format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

#command to change bgcolor of scale
style2= ttk.Style()
style2.configure("TScale",background="white")

slider2=ttk.Scale(app,from_=0, to=200,orient="horizontal",style="TScale",
                 command=slider_changed2,variable=current_value2)
slider2.place(x=410,y=260)

#entry box
Height=StringVar()
Weight=StringVar()

height = Entry(app,textvariable=Height,width=4,font='lato 40',bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=115,y=180)
Height.set(get_current_value())

weight = Entry(app,textvariable=Weight,width=4,font='lato 40',bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=395,y=180)
Weight.set(get_current_value2())

#label for weight and height
label_w =Label(app,font="lato 13 bold",bg="white")
label_w.place(x=400,y=130)
label_w.config(text="Weight(in kg)")

label_h= Label(app,font="lato 13 bold",bg="white")
label_h.place(x=130,y=130)
label_h.config(text="Height(in cm)")

#man image
secondimage=Label(app,bg="lightblue")
secondimage.place(x=150,y=500)


Button(app,text="SUBMIT",width=14,height=2,font="lato 12 bold",bg="#fbb13c",fg="white",command=BMI).place(x=380,y=560)

label1=Label(app,font="lato 60 bold",bg="lightblue",fg="#fff")
label1.place(x=250
             ,y=350)

label2=Label(app,font="lato 18 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=250,y=460)

label3=Label(app,font="lato 16",bg="lightblue")
label3.place(x=220,y=490)



app.mainloop()


