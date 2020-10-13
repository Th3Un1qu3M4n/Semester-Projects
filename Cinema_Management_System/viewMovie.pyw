import subprocess
from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from io import BytesIO

view = Tk()
view.title('Cinema Management System')
view.configure(bg='#2a3436')
view.geometry('620x400')

def back():
    view.destroy()

def bookMovie():
	view.destroy()
	subprocess.Popen("python bookMovie.pyw", shell=True)

sessionFile= open('session.txt', 'r')
lines=sessionFile.read().splitlines()
movieId=lines[1]
sessionFile.close()
print(movieId)

conn = sqlite3.connect('cms.db')
c= conn.cursor()
movie_id =str(movieId)
print(movie_id)
c.execute("Select * FROM movies WHERE oid =?",(movie_id))

records = c.fetchall()
record=list(sum(records, ()))

view.title(record[0])

name_label = Label(view, text="Name :", width=13, bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=1, column=0, pady=(10,0))
desc_label = Label(view, text="Description :", width=13, bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=2, column=0)
language_label = Label(view, text="language :", width=13, bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=3, column=0)
subtitle_label = Label(view, text="Subtitle :", width=13,  bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=4, column=0)
price_label = Label(view, text="Price :", width=13, bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=5, column=0)
time_label = Label(view, text="Time :", width=13, bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=6, column=0)
date_label = Label(view, text="Date :", width=13, bg="#2a3436",fg='white', font=("Century 15 bold")).grid(row=7, column=0)
seats_label = Label(view, text="Available Seats :", width=13, bg="#2a3436",fg='white', font=("century 15 bold")).grid(row=8, column=0)


timeDict = {
            "1600":"4:00 PM",
            "1900":"7:00 PM",
            "2200":"10:00 PM",
            "100":"1:00 AM"
        }
timeToDisplay = timeDict[record[5]]

name = Label(view, text=record[0], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=1, column=1, padx=10, pady=(10,0))
desc = Label(view, text=record[1], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=2, column=1, padx=10)
language = Label(view, text=record[2], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=3, column=1, padx=10)
subtitle = Label(view, text=record[3], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=4, column=1, padx=10)
price = Label(view, text=record[4], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=5, column=1, padx=10)
time = Label(view, text=timeToDisplay, bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=6, column=1, padx=10)
date = Label(view, text=record[6], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=7, column=1, padx=10)
seats = Label(view, text=record[7], bg="#2a3436",fg='#48cf5d', font=('Cambria 14 bold')).grid(row=8, column=1, padx=10)

img=  Image.open(BytesIO(record[8]))
img.thumbnail((200,200))
photo = (ImageTk.PhotoImage(img))
panel= Label(view, image = photo).grid(row=1, column=2,rowspan=8,padx=10)

back_btn = Button(view, text="Back", bg = 'red', fg='white', command=bookMovie, font=('Cambria 10 bold'))
back_btn.grid(row=9, column=0, pady=10, padx=10, ipadx=10)
book_btn = Button(view, text="Book", bg='grey', fg='white', command=bookMovie, font=('Cambria 10 bold') )
book_btn.grid(row=9, column=1, pady=10, padx=10, ipadx=100)
    
conn.commit()
conn.close()
view.mainloop()
