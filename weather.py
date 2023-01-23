from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from api_key import api_key

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+300")
root.resizable(False, False)


base_url='http://api.openweathermap.org/data/2.5/weather?'

def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    complete_url = f"{base_url}appid={api_key}&q={city}"
    json_data = requests.get(complete_url).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp, "°C"))
    c.config(text=(f"{condition} | FEELS LIKE {temp} °C"))

    w.config(text=f"{wind} km/h")
    h.config(text=f"{humidity} %")
    d.config(text=f"{description}")
    p.config(text=f"{pressure} hPa")

    

# Search box
Search_image = PhotoImage(file="bar6.png")
myimage = Label(root, image=Search_image)
myimage.place(x=20, y=20)

# Text field
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#007db9", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search3.png")
my_image_icon = Button(image=Search_icon, borderwidth=0, border=0, cursor="hand2", bg="#007db9", activebackground="#007db9", command=getWeather)
my_image_icon.place(x=460, y=34)

# Logo image
Logo_image = PhotoImage(file="weather2.png")
logo = Label(root, image=Logo_image)
logo.place(x=170, y=110)


# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(root, image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Label1
Label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), bg="#007db9", fg="white")
Label1.place(x=120, y=400)

Label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), bg="#007db9", fg="white")
Label2.place(x=250, y=400)

Label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), bg="#007db9", fg="white")
Label3.place(x=430, y=400)

Label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), bg="#007db9", fg="white")
Label4.place(x=650, y=400)

t=Label(font=("arial", 70, "bold"), fg="white")
t.place(x=450, y=150)
c=Label(font=("arial", 15, "bold"), fg="white")
c.place(x=450, y=250)

w=Label(text='...', font=("arial", 20, "bold"), bg="#007db9", fg="black")
w.place(x=120, y=450)
h=Label(text='...', font=("arial", 20, "bold"), bg="#007db9", fg="black")
h.place(x=250, y=450)
d=Label(text='...', font=("arial", 20, "bold"), bg="#007db9", fg="black")
d.place(x=430, y=450)
p=Label(text='...', font=("arial", 20, "bold"), bg="#007db9", fg="black")
p.place(x=650, y=450)



root.mainloop()