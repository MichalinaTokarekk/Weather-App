from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textField.get()

        geolocator = Nominatim(user_agent="geoapiExcercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        home = pytz.timezone(result)
        localTime = datetime.now(home)
        currentTime = localTime.strftime("%I:%M %p")
        clock.config(text=currentTime)
        name.config(text="CURRENT WEATHER")

        #weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d7c52bd3659e5a54c5351aa89acf7cd7"
        #api_key = 'd7c52bd3659e5a54c5351aa89acf7cd7'
        #api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}"


        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")

#serach box
searchImage=PhotoImage(file="search.png")
myImage = Label(image = searchImage)
myImage.place(x=20, y=20)

textField = tk.Entry(root, justify="center", width=17, font=("poopins", 25, "bold"), bg="#404040", border=0, fg="white")
textField.place(x=50, y=40)
textField.focus()

searchIcon = PhotoImage(file="searchIcon.png")
myImageIcon = Button(image=searchIcon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myImageIcon.place(x=400, y=34)

#logo
logoImage = PhotoImage(file="logo.png")
logo = Label(image=logoImage)
logo.place(x=150, y=100)

#bottom box
frameImage = PhotoImage(file="box.png")
frame = Label(image=frameImage)
frame.pack(padx=5, pady=5, side=BOTTOM)

#time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

#label
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=420, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=420, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
