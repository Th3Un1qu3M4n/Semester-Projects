import subprocess
from tkinter import *
import sqlite3
import os

login = Tk()
login.title('Management LOGIN')
login.configure(background = '#15204d')
login.geometry('400x400')

def retrieveUser():
    if os.path.isfile('sessionA.txt'):
        login.destroy()
        subprocess.Popen('pythonw m_main.pyw',shell=True)
        
        

def User():
    login.destroy()
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.Popen('python login.pyw', startupinfo=startupinfo)

def startSession(uId):
    sessionFile= open('sessionA.txt','w')
    lines=[str(uId)]
    sessionFile.writelines(lines)
    sessionFile.close()

def loginUser():
    
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()
    c.execute("SELECT oid,* FROM management WHERE username=? AND password=?",(username.get(), password.get()))
    records = c.fetchall()
    
    conn.commit()
    conn.close()

    if len(records) !=0:
        record = list(sum(records, ()))
        print(record)
        startSession(record[0])
        login.destroy()
        subprocess.Popen('python m_main.pyw', shell=True)
            
    else:
        print(records)
        message_label.configure(text="Wrong Username/Password")
        username.delete(0, END)
        password.delete(0 ,END)
    return
    

username = Entry(login, width=40)
username.grid(row=2, column=1, pady=(10,0))
password = Entry(login, show="*", width=40)
password.grid(row=3, column=1, pady=(10,0))

username.focus()

caption_label= Label(login, text="Management Login", fg='white', font=('Roman 20 bold'))
caption_label['bg']=caption_label.master['bg']
caption_label.grid(row=1, column =0, columnspan=2, pady= 8)
username_label = Label(login, text="username:", fg='white',width=10, font=("Cambria 12 bold"))
username_label['bg']=username_label.master['bg']
username_label.grid(row=2, column=0, pady=(10,0))
password_label = Label(login, text="password:", fg='white', width=10, font=("Cambria 12 bold"))
password_label['bg']=username_label.master['bg']
password_label.grid(row=3, column=0, pady=(10,0))
message_label = Label(login, text="")
message_label.configure(foreground = 'white')
message_label['bg'] = message_label.master['bg']
message_label.grid(row=6, column=0, columnspan=2, pady=(10,0))

login_btn = Button(login, text="Login", command=loginUser, bg='white', width=10, font=("Century 10 bold"))
login_btn.grid(row=5, column=0, columnspan=2, pady=(40,0), padx=10)

create_btn = Button(login, text="User Login", command=User, bg='white', width=40, font=("Century 10 bold"))
create_btn.grid(row=6, column=0, columnspan=2, pady=(140,10), padx=10)

retrieveUser()

login.mainloop()
