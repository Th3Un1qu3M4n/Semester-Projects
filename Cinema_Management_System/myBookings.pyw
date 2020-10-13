import subprocess
from tkinter import *
import sqlite3

myBookings = Tk()
myBookings.title('All Bookings')
myBookings.configure(bg ='white')

def main_menu():
    myBookings.destroy()

sessionFile= open('session.txt', 'r')
lines=sessionFile.read().splitlines()
userId=lines[0]
sessionFile.close()
print(userId)

conn = sqlite3.connect('cms.db')
c= conn.cursor()

c.execute("SELECT oid,* FROM bookings WHERE userId="+str(userId)+" AND bookBy='Audience' ORDER BY oid DESC")
records = c.fetchall()

bookingId = Label(myBookings, text="Booking Id ", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=0)
movieId = Label(myBookings, text="Movie Id ", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=1)
movieName = Label(myBookings, text="Movie Name ", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=2)
paid = Label(myBookings, text="Paid ", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=3)
time = Label(myBookings, text="Time ", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=4)
date = Label(myBookings, text="Date ", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=5)
seats = Label(myBookings, text="Seats", bg="#36afbf", font=("Century 11 bold"), width=10).grid(row=0,column=6)

count = 1
approve_btn = []
for record in records:

    bookingId = Label(myBookings, text=record[0])
    bookingId['bg']=bookingId.master['bg']
    bookingId.grid(row=count,column=0)
    movieId = Label(myBookings, text=record[2])
    movieId['bg']=movieId.master['bg']
    movieId.grid(row=count,column=1)
    movieName = Label(myBookings, text=record[4])
    movieName['bg']=movieName.master['bg']
    movieName.grid(row=count,column=2)
    paid = Label(myBookings, text=record[6])
    paid['bg']=paid.master['bg']
    paid.grid(row=count,column=3)
    time = Label(myBookings, text=record[7])
    time['bg']=time.master['bg']
    time.grid(row=count,column=4)
    date = Label(myBookings, text=record[8])
    date['bg']=date.master['bg']
    date.grid(row=count,column=5)
    seats = Label(myBookings, text=record[9])
    seats['bg']=seats.master['bg']
    seats.grid(row=count,column=6)
    count += 1
    
back_btn = Button(myBookings, text="Back", bg='#ff1c1c', fg='white', font=('Cambria 10 bold'), command=main_menu)
back_btn.grid(row=count, column=6, pady=10, padx=10, ipadx=20)

conn.commit()
conn.close()
    
myBookings.mainloop()
