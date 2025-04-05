import tkinter as tk
import requests
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Import Pillow for resizing images

# Your API weather key
api_key = "015eebea1de289f6d9be246c1772917d"

from PIL import Image, ImageTk  # Import Pillow for resizing images


# Function to resize the icon
def resize_icon(icon_file, size=(100, 100)):
    # Open the image file
    image = Image.open(icon_file)

    # Resize the image using LANCZOS resampling method
    image = image.resize(size, Image.Resampling.LANCZOS)

    # Convert to a PhotoImage object for Tkinter
    icon_image = ImageTk.PhotoImage(image)

    return icon_image


def get_city():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        result_label.config(text=f"{temp}°C, {description}")

        # Determine which icon to show
        if "clear" in description:
            icon_file = "weather_icons/sunny.png"
        elif "cloud" in description:
            icon_file = "weather_icons/cloudy(1).png"
        elif "rain" in description:
            icon_file = "weather_icons/rainy.png"
        else:
            icon_file = "weather_icons/sunny.png"  # Default icon

        # Resize the image
        icon_image = resize_icon(icon_file, size=(100, 100))  # Resize to 100x100 (you can change this)

        # Display the resized icon
        icon_label.config(image=icon_image)
        icon_label.image = icon_image  # Keep a reference to prevent garbage collection

    else:
        result_label.config(text="City Not Found.")
        icon_label.config(image="")


# This code creates the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")  # Width x Height
root.config(bg="#f0f0f0")  # Sets the background color

# Labels
label = tk.Label(root, text="Enter a city:", bg="#f0f0f0", font=("Arial", 12))
label.pack(pady=10)

# Entry (text input box)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack()

# BUTTON CREATINNGGGG :DDDD
get_weather_button = tk.Button(root, text="Get Weather", command=get_city, bg="#4CAF50", fg="white", font=("Arial", 12))
get_weather_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14))
result_label.pack(pady=10)

# Label for the weather icon
icon_label = tk.Label(root, bg="#f0f0f0")
icon_label.pack(pady=10)

# To keep the window open
root.mainloop()

