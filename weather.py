from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x700+300+100")
root.resizable(False, False)

def getWeather():

    try:
        city = textfield.get()
        geolocator = Nominatim (user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at (lng=location. longitude, lat=location.latitude)

        home = pytz.timezone (result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text="Current Weather & Time")

        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b65505f3239c513dda27a6d8f10bdc29"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data[ 'main']['pressure']
        humidity = json_data['main']['humidity']
        wind= json_data[ 'wind' ]['speed']
    
        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "Feels", "Like", temp, "°"))
        w.config(text=wind)
        h.config(text=humidity)
        d. config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry")



#search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image = Search_image)
myimage.place(x=320,y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 20, "bold"), bg = "#404040", border=0, fg="white")
textfield.place(x=320, y=20)
textfield.focus()

Search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=535, y=19.4)

#logo
Logo_image = PhotoImage(file = "logo.png")
logo = Label(image=Logo_image)
logo.place(x=55, y=125)

#Bottom Box
Frame_image = PhotoImage(file = "box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=3, pady=5, side=BOTTOM)

#time
name = Label(root, font=("arial", 30, "bold"))
name.place(x=400, y=170)
clock = Label(root, font=("arial", 20, "bold"))
clock.place(x=450, y=270)

#label
label1=Label (root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=580)

label2=Label (root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=580)

label3=Label (root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=580)

label4=Label (root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=580)

t=Label(font=("arial", 40, "bold"), fg="#ee666d")
t.place(x=655, y=250)
c=Label(font=("arial", 15, 'bold'))
c.place(x=655, y=310)

w=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=610)
h=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=610)
d=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=440, y=610)
p=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=610)


root.mainloop()