# LANG tkinger gjennomgang: https://www.youtube.com/watch?v=YXPyB4XeYLA

import tkinter as tk
import sys
from tkinter import font
from tkinter import simpledialog
import requests
import os

HEIGHT = 500
WIDTH = 600

def test_function(entry):

	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = '5173d001661c989e15282ccef411a5ec'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()

# def register_user():
#	username_info = username.get()
#	password_info = password.get()
#	appendusername = str(username_info)
#	print("The username is " + str(username_info) + " and the password is " + str(password_info) + " " + appendusername)

# f = open('users.txt', 'a')
# f.write("dummytext")
# f.close()

#	file=open(username_info+".txt", "w")
#	file.write(username_info+"\n")
#	file.write(password_info)
#	file.close()
#	entryusername.delete(0, END)
#	entrypassword.delete(0, END)

# registerlabel = tk.Label(top, text = "Registration was succesfull", fg = "green").pack()

def open():
	top = tk.Toplevel()
	top.title("My second window")
	top.geometry("500x600")

	global username
	global password
	global entryusername
	global entrypassword
	username = tk.StringVar()
	password = tk.StringVar()

	label = tk.Label(top, text="Here you can register as a new user").pack()
	label1 = tk.Label(top, text="Please enter details below").pack()
	label2 = tk.Label(top, text="").pack()
	label3 = tk.Label(top, text = "Username * ").pack()
	entryusername = tk.Entry(top, textvariable = username)
	entryusername.pack()
	label4 = tk.Label(top, text="").pack()
	label3 = tk.Label(top, text = "Password * ").pack()
	entrypassword = tk.Entry(top, textvariable = password)
	entrypassword.pack()
	Registerbutton = tk.Button(top, text = "Register", command=register_user).pack()

	btn2 = tk.Button(top, text="Close window", command=top.destroy).pack()

def openfile():
	os.system('python skrivtilfil.py')

def getflights():
	os.system('python getflights.py')

#lbl = Label(top, text="Hello World").pack

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


#background_image = tk.PhotoImage(file='landscape.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

actionframe = tk.Frame(root, bg='#0059b3', bd=5)
actionframe.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.07, anchor='n')

orderbutton = tk.Button(actionframe, text="Find flight", command=getflights)
orderbutton.place(relx=0.7, relheight=1, relwidth=0.3)

registerbutton = tk.Button(actionframe, text="Register", command=openfile)
registerbutton.place(relx=0.3, relheight=1, relwidth=0.3)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.27, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)




root.mainloop()