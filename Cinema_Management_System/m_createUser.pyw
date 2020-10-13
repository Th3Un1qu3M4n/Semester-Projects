import subprocess
from tkinter import *
from tkinter import ttk
import sqlite3

createUser = Tk()
createUser.title('Create Management User')
createUser.configure(background = '#15204d')
createUser.geometry('500x400')


def main_menu():
    createUser.destroy()

def submit():
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    approveUser='no'
    c.execute("INSERT INTO management VALUES(:username, :name, :email, :pNumber, :password, :role)",
                {
                
                'username':username.get(),
                'name':name.get(),
                'email':email.get(),
                'pNumber':eval(pNumber.get()),
                'password':password.get(),
                'role':'manage'
                    })

    message_label.configure(text="User created  successfully!")
    
    username.delete(0, END)
    name.delete(0, END)
    email.delete(0, END)
    pNumber.delete(0, END)
    password.delete(0, END)
    
    username.focus()
    
    
    conn.commit()
    conn.close()

def viewUsers():
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()


    c.execute("SELECT oid,* FROM management")
    records = c.fetchall()
    print(records)

    
    username.delete(0, END)
    name.delete(0, END)
    email.delete(0, END)
    pNumber.delete(0, END)
    password.delete(0, END)
    
    username.focus()
    
    conn.commit()
    conn.close()
    
    




username = Entry(createUser, width=50)
username.grid(row=2, column=1)
name = Entry(createUser, width=50)
name.grid(row=3, column=1, pady=5)
email = Entry(createUser, width=50)
email.grid(row=4, column=1, pady=5)
pNumber = Entry(createUser, width=50)
pNumber.grid(row=5, column=1, pady=5)
password = Entry(createUser, width=50)
password.grid(row=6, column=1, pady=5)

username.focus()

caption_label= Label(createUser, text="New Management Account", width=30, fg='white', font=('Roman 20 bold'))
caption_label['bg']=caption_label.master['bg']
caption_label.grid(row=1, column =0, columnspan=2, ipadx=50, pady= 8)
username_label = Label(createUser, text="username", fg='white', width=10, font=("Cambria 12 bold"))
username_label['bg']=username_label.master['bg']
username_label.grid(row=2, column=0, pady =5)
name_label = Label(createUser, text="name", fg='white', width=10, font=("Cambria 12 bold"))
name_label['bg']=name_label.master['bg']
name_label.grid(row=3, column=0, pady =5)
email_label = Label(createUser, text="email", fg='white', width=10, font=("Cambria 12 bold"))
email_label['bg']=email_label.master['bg']
email_label.grid(row=4, column=0, pady=5)
pNumber_label = Label(createUser, text="Phone Number \n 10 Digit \n (e.g 3001234567)", fg='white', font=("Cambria 12 bold"))
pNumber_label['bg']=pNumber_label.master['bg']
pNumber_label.grid(row=5, column=0)
password_label = Label(createUser, text="password", fg='white', width=10, font=("Cambria 12 bold"))
password_label['bg']=password_label.master['bg']
password_label.grid(row=6, column=0, pady=5)



back_btn = Button(createUser, text="Back", command=main_menu, bg = '#a81818', fg='white', width=4, font=('Century 10 bold'))
back_btn.grid(row=10, column=0, pady=15, padx=10, ipadx=20)

submit_btn = Button(createUser, text="Create Account", command=submit, bg = 'white', width=10, font=('Century 10 bold'))
submit_btn.grid(row=10, column=1, pady=15, padx=10, ipadx=20)


submit1_btn = Button(createUser, text="View Accounts", command=viewUsers, bg = 'white', width=10, font=('Century 10 bold'))
submit1_btn.grid(row=12, column=1, pady=15, padx=10, ipadx=20)

message_label = Label(createUser, text="")
message_label['bg']=message_label.master['bg']
message_label.configure(foreground = 'white')
message_label.grid(row=11, column=0, columnspan=2)


createUser.mainloop()
