from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title('Weather App')
root.geometry("900x500+300+200")
root.resizable(0,0)

def getwh():
    city = search_en.get()
    if city == '':
        messagebox.showerror("error!", "Fill Search")
    else:
            try:
                geolocator = Nominatim(user_agent="geoapiExercises")
                location = geolocator.geocode(city)
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

                home = pytz.timezone(result)
                local_time = datetime.now(home)
                current_time = local_time.strftime("%I:%M %p")
                clock.config(text=current_time)
                name.config(text="CURRENT WEATHER")

                api = "https://api.openweathermap.org/data/2.5/weather?q" + city + "&appid=3ddb0f6f6696dbedbd7f5aee054dbca8"

                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                description = json_data['weather'][0]['description']
                temp = int(json_data['main']['temp'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                clock.config(text=current_time)
                name.config(text="CURRENT WEATHER")
                t.config(text=(temp, "°"))
                c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

                w.config(text=wind)
                h.config(text=humidity)
                d.config(text=description)
                p.config(text=pressure)
            except:

                clock.config(text='')
                name.config(text='')
                messagebox.showerror("error!", "Invalid Search")
                return

search_lmg = PhotoImage(file='Copy of search.png')
seLabel = Label(root, image=search_lmg)
seLabel.place(x=20, y=20)

search_en = Entry(root, width=17,justify='center', font=('Microsoft Yeahei UI Light', 25, 'bold'), bd=0,bg='#404040', fg='white')
search_en.place(x=50,y=40)
search_en.focus()

searchq_lmg = PhotoImage(file='Copy of search_icon.png')
seqLabel = Button(root, image=searchq_lmg,bd=0,bg='#404040',command=getwh)
seqLabel.place(x=396, y=32)

name =Label(root,font=("arial",15,"bold"))
name.place(x=25,y=96)
clock =Label(root,font=("arial",15,"bold"))
clock.place(x=25,y=130)
logo_lmg = PhotoImage(file='Copy of logo.png')
lgLabel = Label(root, image=logo_lmg)
lgLabel.place(x=135, y=120)

box_lmg = PhotoImage(file='Copy of box.png')
bLabel = Label(root, image=box_lmg)
bLabel.place(x=70, y=380)

info_lbl = tk.Label(root, text="WIND",fg='white', font=("Helvetica", 15,'bold'), bg="#1ab5ef")
info_lbl.place(x=125,y=403)

info1_lbl = tk.Label(root, text="HUMIDITY",fg='white', font=("Helvetica", 15,'bold'), bg="#1ab5ef")
info1_lbl.place(x=250,y=403)

info2_lbl = tk.Label(root, text="DESCRIPTION",fg='white', font=("Helvetica", 15,'bold'), bg="#1ab5ef")
info2_lbl.place(x=430,y=403)

info3_lbl = tk.Label(root, text="PRESSURE",fg='white', font=("Helvetica", 15,'bold'), bg="#1ab5ef")
info3_lbl.place(x=650,y=403)

t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text='...',font=("arial",17,"bold"),bg='#1ab5ef')
w.place(x=125,y=435)
h = Label(text='...',font=("arial",17,"bold"),bg='#1ab5ef')
h.place(x=250,y=435)
d = Label(text='...',font=("arial",17,"bold"),bg='#1ab5ef')
d.place(x=430,y=435)
p = Label(text='...',font=("arial",17,"bold"),bg='#1ab5ef')
p.place(x=650,y=435)

root.mainloop()