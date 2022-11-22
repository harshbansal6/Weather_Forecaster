from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

#ADDING THE FUNCTIONS AND API
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file="config.ini"
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']

def get_weather(city):
    result=requests.get(url.format(city,api_key))
    if result:
        json=result.json()
        #(City,Country,temp_celsius, temp_fahrenheit,icon,weather)
        city=json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_celsius=temp_kelvin-273.15
        temp_fahr=(temp_kelvin-273.15)*9/5+32
        weather=json['weather'][0]['main']
        final=(city,country,temp_celsius,temp_fahr,weather)
        return final
    else:
        return None

def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location_lbl['text']='{}, {}'.format(weather[0], weather[1])
        temp_lbl['text']='{:.2f}*C, {:.2f}*F'.format(weather[2], weather[3])
        weather_lbl['text']=weather[4]

    else:
            messagebox.showerror('Error','Cannot find city {}'.format(city))

#STARTING THE WINDOW
app=Tk()
app.title("WEATHER APP")
app.geometry("500x500")

#ENTRY BOX
city_text=StringVar()
city_entry=Entry(app,textvariable=city_text)
city_entry.pack()

#SEARCH BUTTON
search_btn=Button(app,text="search weather", width=12, command=search)
search_btn.pack()

#ADDING THE INFORMATION SCREEN
location_lbl=Label(app,text="location",font=("bold",20))
location_lbl.pack()

#LABEL/ELEMENT FOR TEMPERATURE
temp_lbl=Label(app,text="temperature")
temp_lbl.pack()

#WEATHER LABEL/ELEMENT
weather_lbl=Label(app,text="weather")
weather_lbl.pack()

#FOR CLOSING THE WINDOW
app.mainloop()