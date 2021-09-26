"""
Created on Sun Sep 26 21:17:06 2021

@author: Reza_Behzadfard
"""
from tkinter import *
import time

def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    if int(hr) > 12 and int(mn) > 0: # convert AM to PM
        w_dn.config(text="PM")
    if int(hr) > 12:
        hr = str(int(hr)-12)

    w_hour.config(text=hr)
    w_minute.config(text=mn)
    w_second.config(text=sc)
    
    w_hour.after(200, clock)  # to make clock update every second
           
clock_gui = Tk()
clock_gui.title("Digital Clock")
clock_gui.geometry("1350x700+0+0") # width, height, x-axis, y-axis. we have kept 0 because we will start from left
clock_gui.config(bg = "#0C1E28") # you can give any color you want


# Hour
w_hour = Label(clock_gui, text="12", font=("Times 20 bold", 75, "bold"), bg="#0875B7", fg="white")
w_hour.place(x=350, y=200, width=150, height=150)

w_hour_text = Label(clock_gui, text="HOUR", font=("Times 20 bold", 20, "bold"), bg="#0875B7", fg="white")
w_hour_text.place(x=350, y=360, width=150, height=50)

# Minute
w_minute = Label(clock_gui, text="12", font=("Times 20 bold", 75, "bold"), bg="#008EA4", fg="white")
w_minute.place(x=520, y=200, width=150, height=150)

w_minute_text = Label(clock_gui, text="Minute", font=("Times 20 bold", 20, "bold"), bg="#008EA4", fg="white")
w_minute_text.place(x=520, y=360, width=150, height=50)

# Second
w_second = Label(clock_gui, text="12", font=("Times 20 bold", 75, "bold"), bg="#06B4B8", fg="white")
w_second.place(x=690, y=200, width=150, height=150)

w_second_text = Label(clock_gui, text="Second", font=("Times 20 bold", 20, "bold"), bg="#06B4B8", fg="white")
w_second_text.place(x=690, y=360, width=150, height=50)

# dn
w_dn = Label(clock_gui, text="AM", font=("Times 20 bold", 70, "bold"), bg="#9F0646", fg="white")
w_dn.place(x=860, y=200, width=150, height=150)

w_dn_text = Label(clock_gui, text="NOON", font=("Times 20 bold", 20, "bold"), bg="#9F0646", fg="white")
w_dn_text.place(x=860, y=360, width=150, height=50)

clock()
clock_gui.mainloop()
