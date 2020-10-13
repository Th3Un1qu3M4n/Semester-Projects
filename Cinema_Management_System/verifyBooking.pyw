import subprocess
from tkinter import *
from tkinter import messagebox
import sqlite3

verify = Tk()
verify.title('Cinema Management System')
verify.configure(bg='#fafafc')
verify.geometry('620x300')

def back():
    verify.destroy()


def view():

    for widget in viewBookings.winfo_children():
        widget.destroy()
        
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()
    booking_id=str(bookId.get())
    c.execute("Select oid,* FROM bookings WHERE oid ="+booking_id)

    record = c.fetchone()
    if not record:
    	messagebox.showerror("Sorry!", "Booking not Found!")
    	
    	return
    print(record)
    
    bookingId = Label(viewBookings, text="Booking Id :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    bookingId['bg']=bookingId.master['bg']
    bookingId.grid(row=0,column=0, padx=10, pady=(30,0))
    bookBy = Label(viewBookings, text="Booked By :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    bookBy['bg']=bookBy.master['bg']
    bookBy.grid(row=0,column=4, padx=10, pady=(30,0))
    userId = Label(viewBookings, text="User Id :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    userId['bg']=userId.master['bg']
    userId.grid(row=1,column=0, padx=10)
    userName = Label(viewBookings, text="Name :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    userName['bg']=userName.master['bg']
    userName.grid(row=1,column=4, padx=20)
    movieId = Label(viewBookings, text="Movie Id :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    movieId['bg']=movieId.master['bg']
    movieId.grid(row=2,column=0, padx=20)
    movieName = Label(viewBookings, text="Movie Name :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    movieName['bg']=movieName.master['bg']
    movieName.grid(row=2,column=4, padx=20) 
    time = Label(viewBookings, text="Time :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    time['bg']=time.master['bg']
    time.grid(row=3,column=0, padx=20)
    date = Label(viewBookings, text="Date :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    date['bg']=date.master['bg']
    date.grid(row=3,column=4, padx=2)
    seats = Label(viewBookings, text="Seats :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    seats['bg']=seats.master['bg']
    seats.grid(row=4,column=0, padx=2, pady=(0,30))
    paid = Label(viewBookings, text="Paid :", fg='#0ceb2d', font=("Cambria 13 bold"), width=10)
    paid['bg']=paid.master['bg']
    paid.grid(row=4,column=4, padx=2, pady=(0,30))

    bookingId = Label(viewBookings, text=record[0], fg='white', font=("Cambria 12 bold"))
    bookingId['bg']=bookingId.master['bg']
    bookingId.grid(row=0,column=1, pady=(30,0))
    bookBy = Label(viewBookings, text=record[5], fg='white', font=("Cambria 12 bold"))
    bookBy['bg']=bookBy.master['bg']
    bookBy.grid(row=0,column=5, pady=(30,0), padx=35)
    userId = Label(viewBookings, text=record[1], fg='white', font=("Cambria 12 bold"))
    userId['bg']=userId.master['bg']
    userId.grid(row=1,column=1)
    userName = Label(viewBookings, text=record[3], fg='white', font=("Cambria 12 bold"))
    userName['bg']=userName.master['bg']
    userName.grid(row=1,column=5, padx=35)
    movieId = Label(viewBookings, text=record[2], fg='white', font=("Cambria 12 bold"))
    movieId['bg']=movieId.master['bg']
    movieId.grid(row=2,column=1)
    movieName = Label(viewBookings, text=record[4], fg='white', font=("Cambria 12 bold"))
    movieName['bg']=movieName.master['bg']
    movieName.grid(row=2,column=5, padx=35)
    time = Label(viewBookings, text=record[7], fg='white', font=("Cambria 12 bold"))
    time['bg']=time.master['bg']
    time.grid(row=3,column=1)
    date = Label(viewBookings, text=record[8], fg='white', font=("Cambria 12 bold"))
    date['bg']=date.master['bg']
    date.grid(row=3,column=5, padx=35)
    seats = Label(viewBookings, text=record[9], fg='white', font=("Cambria 12 bold"))
    seats['bg']=seats.master['bg']
    seats.grid(row=4,column=1, pady=(0,30))
    paid = Label(viewBookings, text=record[6], fg='white', font=("Cambria 12 bold"))
    paid['bg']=paid.master['bg']
    paid.grid(row=4,column=5, pady=(0,30), padx=35)

viewBookings = Frame(verify)
viewBookings.configure(bg='#2a3436')
viewBookings.grid(row=2,column=0, columnspan=5)

caption_label=Label(verify, text="Booking Verification", bg="grey", fg='white', width= 30, font=('Roman 20 bold')).grid(row=0, column=0, columnspan=5, padx=100)

name_label = Label(verify, text="Booking Id:")
name_label['bg']=name_label.master['bg']
name_label.grid(row=1, column=0, padx=10)

bookId = Entry(verify)
bookId.grid(row=1, column=1,pady=(10,0))
bookId.focus()


search_btn = Button(verify, text="search", bg='cyan', command=view, width=20)
search_btn.grid(row=1, column=2, columnspan=2, pady=10)

back_btn = Button(verify, text="Back", bg='red', fg='white', command=back, width=10)
back_btn.grid(row=1, column=4, pady=10, padx=20)

    
verify.mainloop()