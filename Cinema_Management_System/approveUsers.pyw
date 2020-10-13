import subprocess
from tkinter import *
import sqlite3

approveUser = Tk()
approveUser.title('Approve Users')
approveUser.configure(background='white')

def main_menu():
    approveUser.destroy()

def approve(userId):
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    c.execute("UPDATE Audience SET approved=? WHERE oid=?",('yes',userId))
    
    conn.commit()
    conn.close()
    print(userId)
    approveUser.destroy()
    subprocess.Popen('python approveUsers.pyw', shell=True)
    
conn = sqlite3.connect('cms.db')
c= conn.cursor()
c.execute("SELECT oid,* FROM Audience WHERE approved=? ORDER BY oid ASC",('no',))
records = c.fetchall()

username_label = Label(approveUser, text="Username", bg="#034036", fg='white', font =('Cambria 10 bold'))
username_label.grid(row=0,column=0, ipadx=50)
name_label = Label(approveUser, text="Name", bg="#034036", fg='white', font =('Cambria 10 bold'))
name_label.grid(row=0,column=1, ipadx=50)
email_label = Label(approveUser, text="Email", bg="#034036", fg='white', font =('Cambria 10 bold'))
email_label.grid(row=0,column=2, ipadx=50)
pNumber_label = Label(approveUser, text="Phone Number", bg="#034036", fg='white', font =('Cambria 10 bold'))
pNumber_label.grid(row=0,column=3, ipadx=50)
approve_label = Label(approveUser, text="Action", bg="#034036", fg='white', font =('Cambria 10 bold'))
approve_label.grid(row=0,column=4, ipadx=50)

count = 1
approve_btn = []
for record in records:
    username = Label(approveUser, text=record[1])
    username['bg']=username.master['bg']
    username.grid(row=count,column=0)
    name = Label(approveUser, text=record[2])
    name['bg']=name.master['bg']
    name.grid(row=count,column=1)
    email = Label(approveUser, text=record[3])
    email['bg']=email.master['bg']
    email.grid(row=count,column=2)
    pNumber = Label(approveUser, text=record[4])
    pNumber['bg']=pNumber.master['bg']
    pNumber.grid(row=count,column=3)
    approve_btn.append(Button(approveUser, text="Approve", command=lambda record=record: approve(record[0]), bg = '#a1aba9', fg='white', font=('bold',8)))
    approve_btn[count-1].grid(row=count, column=4)
    count += 1

back_btn = Button(approveUser, text="Back", command=main_menu, bg = 'red', fg='white', font = ("Cambria 10 bold"))
back_btn.grid(row=10, column=count, pady=10, padx=10, ipadx=20)

conn.commit()
conn.close()
approveUser.mainloop()
