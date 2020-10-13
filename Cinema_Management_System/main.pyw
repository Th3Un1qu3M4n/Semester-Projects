import subprocess
from tkinter import *
from tkinter import messagebox
import sqlite3
import os

main = Tk()
main.title('Cinema Management System')
main.configure(background = '#415fba')
main.geometry('620x400')

def my_booking():
    subprocess.Popen('python myBookings.pyw',shell=True)

def view_movie():
    subprocess.Popen('python schedule.pyw',shell=True)

def search_movies():
    subprocess.Popen('python search.pyw',shell=True)

def view_profile():
    subprocess.Popen('python profile.pyw',shell=True)

def logout():
    os.remove('session.txt')
    main.destroy()
    subprocess.Popen('python login.pyw',shell=True)
    
def retrieveUser():
    try:
        sessionFile= open('session.txt', 'r')
        lines=sessionFile.read().splitlines()
        userId=lines[0]
        sessionFile.close()
        print(userId)
        
        conn=sqlite3.connect("cms.db")
        c=conn.cursor()
        c.execute("SELECT name FROM Audience WHERE oid=?",userId)
        record=c.fetchone()
        conn.close()
        name="Welcome "+str(record[0])
        welcome_label = Label(main, text=name , bg = 'white', width=8, font=("Cambria 14 bold italic"))
        welcome_label.grid(row=2, column=0, columnspan=4, pady=10, padx=10, ipadx=100)
    except:
        messagebox.showerror("Error", "Not Authorized")
        main.destroy()
        subprocess.Popen('python login.pyw',shell=True)


  
main_label = Label(main, text="MAIN MENU", bg='#c9abb3', width=13, font=("Roman 48 bold"))
main_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10, ipadx=100)


view_btn = Button(main, text="Book a Movie", command=view_movie, bg = 'white', width=20, font=('Cambria 10'))
view_btn.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

search_btn = Button(main, text="Search Movies", command=search_movies, bg = 'white', width=20, font=('Cambria 10'))
search_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

verify_btn = Button(main, text="My Bookings", command=my_booking, bg = 'white', width=20, font=('Cambria 10'))
verify_btn.grid(row=7, column=0, columnspan=3, pady=10, padx=10)

profile_btn = Button(main, text="Edit Profile", command=view_profile, bg = '#78112e', fg='white', width=10, font=('Cambria 10 bold'))
profile_btn.grid(row=4, column=2, pady=10, padx=10)

logout_btn = Button(main, text="Log Out", command=logout, width=10, bg = '#78112e', fg='white', font=('Cambria 10 bold'))
logout_btn.grid(row=4, column=0, pady=10)

retrieveUser()

main.mainloop()
