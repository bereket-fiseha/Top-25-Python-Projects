import requests
import tkinter as tk
from tkinter import messagebox
import json
def show_weather_ui():
  def fetch_weather():
    city = city_entry.get()
    print(city)
    # Add your API key here
    api_key = "7f1386dd7ca4f926c04fb6bf5a43bf53"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {round(temperature-273.15,2)}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")
  
  root = tk.Tk()
  root.title("Weather App")
  root.geometry("400x400")
 # Create and configure labels and entry fields
  city_label = tk.Label(root, text="City:")
  city_label.pack()
  city_entry = tk.Entry(root)
  city_entry.pack()

# Create a button to fetch weather data
  fetch_button = tk.Button(root, text="Fetch Weather",command=fetch_weather)
  fetch_button.pack()
  

# Create a label to display weather information
  weather_label = tk.Label(root, text="")
  weather_label.pack()
  root.mainloop()


  

if __name__=="__main__":
    show_weather_ui()