import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

bookings = Tk()
bookings.title('Cinema Management System')
bookings.configure(bg='#fafcfc')
bookings.geometry('450x400')


def main_menu():
    bookings.destroy()

def callBack(self, mode, callback):
    global totalPrice
    totalPrice=price*int(seats.get())
    totalPrice_label.configure(text=("Total Price: "+str(totalPrice)))


def submit(userId, movieId, userName, movieName, totalPrice, time, date, bookBy, totalSeats):
    print(userId, movieId, userName, movieName, totalPrice, time, date, bookBy, seats.get())

    remainingSeats = totalSeats-int(seats.get())
    if remainingSeats<0:
        msg=str(seats.get())+" seats not available!"
        messagebox.showerror("Sorry", msg)
        return

    conn = sqlite3.connect('cms.db')
    c= conn.cursor()


    c.execute("INSERT INTO bookings VALUES(:userId, :movieId, :userName, :movieName, :bookBy, :price, :time, :date, :seats)",
                {
                
                'userId':userId,
                'movieId':movieId,
                'userName':userName,
                'movieName':movieName,
                'bookBy':bookBy,
                'price':totalPrice,
                'time':time,
                'date':date,
                'seats':seats.get()
                    })
    bookingId=(c.lastrowid)
    c.execute("""UPDATE movies SET
                tickets = :leftSeats
                
                WHERE oid=:oid""",
                  {
                    'leftSeats':remainingSeats,
                    'oid':movieId
                      })
      
    conn.commit()
    conn.close()
    filename="ticket_"+str(bookingId)+".txt"
    ticketFile = open(filename, 'w')
    data="Booking No."+str(bookingId)+"\n Name: "+userName+"\t Movie: "+movieName+"\n Time: "+time+"\t Date: "+date+"\n Booked seats: "+str(seats.get())+"\t Price: "+str(totalPrice)
    ticketFile.write(data)
    ticketFile.close()

    messagebox.showinfo("Booking Successful", "Your refernce no. is "+str(bookingId)+"\n \n "+filename+" generated!")
    bookings.destroy()
    subprocess.Popen("python bookMovie.pyw", shell=True)
    

    
try:    
    sessionFile= open('sessionA.txt', 'r')
    bookBy='management'
except:
    sessionFile= open('session.txt', 'r')
    bookBy='Audience'

lines=sessionFile.read().splitlines()
userId=lines[0]
movieId=lines[1]
sessionFile.close()
print(userId)
print(movieId)
print(bookBy)
timeDict = {
            "1600":"4:00 PM",
            "1900":"7:00 PM",
            "2200":"10:00 PM",
            "100":"1:00 AM"
        }

conn = sqlite3.connect('cms.db')
c= conn.cursor()
c.execute("SELECT name FROM "+bookBy+" WHERE oid="+str(userId))
userrecord=c.fetchone()
userName=userrecord[0]
print(userName)
c.execute("SELECT * FROM movies WHERE oid="+str(movieId))
records = c.fetchone()
print(records)

movieName=records[0]
price=records[4]
time=timeDict[records[5]]
date=records[6]
totalSeats=records[7]

print(movieName, price, time, date, totalSeats)

user_label=Label(bookings, text=("Available Seats are: "+str(totalSeats)))
user_label.configure(bg='#fafcfc')
user_label.grid(row=0, column=0, pady=(5,0))
user_label=Label(bookings, text=("Selected Movie: "+movieName))
user_label.configure(bg='#fafcfc')
user_label.grid(row=1, column=0)


seats_label= Label(bookings, text="Select No. of Seats:", bg='#fafcfc')
seats_label.grid(row=4, column=0, pady=5)

totalPrice_label=Label(bookings, text="", bg='#fafcfc')
totalPrice_label.grid(row=5, column=0)
var= StringVar()
var.trace("w", callBack)
seats= ttk.Combobox(bookings,values=[*range(1,11)], width=10, state="readonly", textvariable=var)
seats.grid(row=4, column=1, pady=5)
seats.current(0)


message_label = Label(bookings, text="")
message_label['bg']=message_label.master['bg']
message_label.grid(row=11, column=1)

back_btn = Button(bookings, text="Back", bg = 'red', fg='white', command=main_menu, font=('Cambria 10 bold'))
back_btn.grid(row=10, column=0, pady=10, padx=10, ipadx=20)

submit_btn = Button(bookings, text="Book Movie", bg='grey', fg='white', command=lambda userId=userId: submit(userId, movieId, userName, movieName, totalPrice, time, date, bookBy, totalSeats))
submit_btn.grid(row=10, column=1, pady=10, padx=10, ipadx=20)

message_label = Label(bookings, text="")
message_label['bg']=message_label.master['bg']
message_label.grid(row=11, column=0, columnspan=2)


bookings.mainloop()
