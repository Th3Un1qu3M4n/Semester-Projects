import subprocess
from tkinter import *
import sqlite3

viewBookings = Tk()
viewBookings.title('All Bookings')
viewBookings.configure(bg='white')


def main_menu():
    viewBookings.destroy()
'''
def delete(userId):
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    c.execute("DELETE FROM Bookings WHERE oid="+str(bookingId))
    
    conn.commit()
    conn.close()
    print(userId)
    viewUsers.destroy()
    subprocess.Popen('python viewUsers.pyw', shell=True)
    
'''

conn = sqlite3.connect('cms.db')
c= conn.cursor()

c.execute("SELECT oid,* FROM bookings ORDER BY oid DESC")
records = c.fetchall()
print(records)

caption_label= Label(viewBookings, text='Booking Details', bg = 'grey', fg='white', width= 20, font=('Roman 20 bold')).grid(row=0, column=4, columnspan=2, pady=5)
bookingId = Label(viewBookings, text="Booking Id ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=0)
userId = Label(viewBookings, text="User Id ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=1)
userName = Label(viewBookings, text="Name ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=2)
movieId = Label(viewBookings, text="Movie Id ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=3)
movieName = Label(viewBookings, text="Movie Name ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=15).grid(row=1,column=4)
bookBy = Label(viewBookings, text="Booked By ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=15).grid(row=1,column=5)
paid = Label(viewBookings, text="Paid ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=6)
time = Label(viewBookings, text="Time ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=7)
date = Label(viewBookings, text="Date ", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=8)
seats = Label(viewBookings, text="Seats", bg="#034036", fg='white', font=("Cambria 12 bold"), width=10).grid(row=1,column=9)

count = 2
approve_btn = []
for record in records:

    bookingId = Label(viewBookings, text=record[0])
    bookingId['bg']=bookingId.master['bg']
    bookingId.grid(row=count,column=0)
    userId = Label(viewBookings, text=record[1])
    userId['bg']=userId.master['bg']
    userId.grid(row=count,column=1)
    userName = Label(viewBookings, text=record[3])
    userName['bg']=userName.master['bg']
    userName.grid(row=count,column=2)
    movieId = Label(viewBookings, text=record[2])
    movieId['bg']=movieId.master['bg']
    movieId.grid(row=count,column=3)
    movieName = Label(viewBookings, text=record[4])
    movieName['bg']=movieName.master['bg']
    movieName.grid(row=count,column=4)
    bookBy = Label(viewBookings, text=record[5])
    bookBy['bg']=bookBy.master['bg']
    bookBy.grid(row=count,column=5)
    paid = Label(viewBookings, text=record[6])
    paid['bg']=paid.master['bg']
    paid.grid(row=count,column=6)
    time = Label(viewBookings, text=record[7])
    time['bg']=time.master['bg']
    time.grid(row=count,column=7)
    date = Label(viewBookings, text=record[8])
    date['bg']=date.master['bg']
    date.grid(row=count,column=8)
    seats = Label(viewBookings, text=record[9])
    seats['bg']=seats.master['bg']
    seats.grid(row=count,column=9)
    count += 1
    '''
    approve_btn.append(Button(viewUsers, text="delete", command=lambda record=record: delete(record[0])))
    approve_btn[count-1].grid(row=count, column=4)
    count += 1
    '''

back_btn = Button(viewBookings, text="Back", command=main_menu, bg = 'red', fg='white', font = ("Cambria 10 bold"))
back_btn.grid(row=10, column=count, pady=10, padx=10, ipadx=20)
conn.commit()
conn.close()
    
viewBookings.mainloop()
