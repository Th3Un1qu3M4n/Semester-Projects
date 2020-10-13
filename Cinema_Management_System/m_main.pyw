import subprocess
from tkinter import *
from tkinter import messagebox
import sqlite3
import os


main = Tk()
main.title('Cinema Management System')
main.configure(background = '#15204d')
main.geometry('620x400')

def view_bookings():
    subprocess.Popen('python viewBookings.pyw',shell=True)

def verify_booking():
    subprocess.Popen('python verifyBooking.pyw',shell=True)

def profile():
    subprocess.Popen('python m_profile.pyw',shell=True)

def add_movie():
    subprocess.Popen('python createMovie.pyw',shell=True)

def add_manage():
    subprocess.Popen('python m_createUser.pyw',shell=True)

def view_movie():
    subprocess.Popen('python m_schedule.pyw',shell=True)

def search_movies():
    subprocess.Popen('python m_search.pyw',shell=True)

def approve_Users():
    subprocess.Popen('python approveUsers.pyw',shell=True)

def view_management():
    subprocess.Popen('python viewManagement.pyw',shell=True)

def view_users():
    subprocess.Popen('python viewUsers.pyw',shell=True)

def updateSchedule():
    subprocess.Popen('python updateSchedule.py',shell=True)

def logout():
    os.remove('sessionA.txt')
    main.destroy()
    subprocess.Popen('python m_login.pyw',shell=True)
    
def retrieveUser():
    try:
        sessionFile= open('sessionA.txt', 'r')
        lines=sessionFile.read().splitlines()
        userId=lines[0]
        sessionFile.close()
        print(userId)
        
        conn=sqlite3.connect("cms.db")
        c=conn.cursor()
        c.execute("SELECT name,role FROM management WHERE oid=?",userId)
        record=c.fetchone()
        conn.close()
        name="Welcome "+str(record[0])
        role=record[1]
        welcome_label = Label(main, text=name , bg = 'white', width=8, font=("Cambria 14 bold italic"))
        welcome_label.grid(row=2, column=0, columnspan=4, pady=10, padx=10, ipadx=100)
        return role
    except:
        global isAuthorized
        isAuthorized=False

def notAuthorized():
        messagebox.showerror("Error", "Not Authorized")
        main.destroy()
        subprocess.Popen('python m_login.pyw',shell=True)

isAuthorized=True
role=retrieveUser()


main_label = Label(main, text="CONTROL PANEL", bg='cyan', width=13, font=("Roman 48 bold"))
main_label.grid(row=1, column=0, columnspan=4, pady=10, padx=10, ipadx=100)

profile_btn = Button(main, text="Edit Profile", command=profile, bg='#84cbe3', width=10, font=("Cambria 10 bold"))
profile_btn.grid(row=2, column=3, pady=10, padx=10)

logout_btn = Button(main, text="Log Out", command=logout, bg='#84cbe3', width=10, font=("Cambria 10 bold"))
logout_btn.grid(row=2, column=0, pady=10)

addMovie_btn = Button(main, text="Add Movie", command=add_movie, bg='white', width=30, font=("Cambria 10"))
addMovie_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

update_btn = Button(main, text="Update Schedule", command=updateSchedule, bg='white', width=30, font=("Cambria 10"))
update_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

approve_btn = Button(main, text="Approve Users", command=approve_Users, bg='white', width=30, font=("Cambria 10"))
approve_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

view_btn = Button(main, text="View Schedule", command=view_movie, bg='white', width=30, font=("Cambria 10"))
view_btn.grid(row=3, column=2, columnspan=2, pady=10, padx=10)

search_btn = Button(main, text="Search Movies", command=search_movies, bg='white', width=30, font=("Cambria 10"))
search_btn.grid(row=4, column=2, columnspan=2, pady=10, padx=10)

users_btn = Button(main, text="View Users", command=view_users, bg='white', width=30, font=("Cambria 10"))
users_btn.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

bookings_btn = Button(main, text="View Bookings", command=view_bookings, bg='white', width=30, font=("Cambria 10"))
bookings_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

verify_btn = Button(main, text="Verify Booking", command=verify_booking, bg='white', width=30, font=("Cambria 10"))
verify_btn.grid(row=6, column=2, columnspan=2, pady=10, padx=10)

if role=='admin':
    addUser_btn = Button(main, text="Add Management", command=add_manage, bg='white', width=30, font=("Cambria 10"))
    addUser_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    users_btn = Button(main, text="View Management", command=view_management, bg='white', width=30, font=("Cambria 10"))
    users_btn.grid(row=7, column=2, columnspan=2, pady=10, padx=10)


if not isAuthorized:
    notAuthorized()




main.mainloop()
