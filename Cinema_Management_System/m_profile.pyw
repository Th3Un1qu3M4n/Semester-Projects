import subprocess
from tkinter import *
from tkinter import messagebox
import sqlite3

profile = Tk()
profile.title('Profile')
profile.configure(bg='#fafcfc')
profile.geometry('500x300')


def main_menu():
    profile.destroy()

def edit(userId):
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    c.execute("""UPDATE management SET
                username = :username,
                email = :email,
                pNumber = :pNumber,
                password = :password
                
                WHERE oid=:oid""",
                  {
                    'username':username.get(),
                    'email':email.get(),
                    'pNumber':pNumber.get(),
                    'password':password.get(),
                    'oid':userId
                      })
    
    conn.commit()
    conn.close()
    print(userId)
    messagebox.showinfo("Success", "Profile Updated!")
    profile.destroy()
    subprocess.Popen('python m_profile.pyw', shell=True)
    

sessionFile= open('sessionA.txt', 'r')
lines=sessionFile.read().splitlines()
userId=lines[0]
sessionFile.close()

conn = sqlite3.connect('cms.db')
c= conn.cursor()

c.execute("SELECT * FROM management WHERE oid="+str(userId))
records = c.fetchall()
print(records)

caption_label=Label(profile, text="Profile", fg= '#415fba',font=('Roman 20 bold'))
caption_label['bg']=caption_label.master['bg']
caption_label.grid(row=1, column =0, columnspan=2, pady= 8)
username_label = Label(profile, text="Username", width=10)
username_label['bg']=username_label.master['bg']
username_label.grid(row=2,column=0, ipadx=50)
name_label = Label(profile, text="Name", width=10)
name_label['bg']=name_label.master['bg']
name_label.grid(row=3,column=0, ipadx=50)
email_label = Label(profile, text="Email", width=10)
email_label['bg']=email_label.master['bg']
email_label.grid(row=4,column=0, ipadx=50)
pNumber_label = Label(profile, text="Phone Number", width=10)
pNumber_label['bg']=pNumber_label.master['bg']
pNumber_label.grid(row=5,column=0, ipadx=50)
password_label = Label(profile, text="Password", width=10)
password_label['bg']=password_label.master['bg']
password_label.grid(row=6,column=0, ipadx=50)

username = Entry(profile, width=50)
username.grid(row=2,column=1)
name = Entry(profile, width=50)
name.grid(row=3,column=1)
email = Entry(profile, width=50)
email.grid(row=4,column=1)
pNumber = Entry(profile, width=50)
pNumber.grid(row=5,column=1)
password = Entry(profile, width=50)
password.grid(row=6,column=1)

for record in records:
    username.insert(0, record[0])
    name.insert(0, record[1])
    name.config(state="disabled")
    email.insert(0, record[2])
    pNumber.insert(0, record[3])
    password.insert(0, record[4])
 
    
edit_btn = Button(profile, text="Save Changes", bg='#0a8291', fg='white', command=lambda userId=userId: edit(userId), font=('Cambria 10 bold'))
edit_btn.grid(row=7, column=1)

back_btn = Button(profile, text="Back", bg='red', fg='white', command=main_menu, font=('Cambria 10 bold'))
back_btn.grid(row=7, column=0, pady=10, padx=10, ipadx=20)

conn.commit()
conn.close()
    
profile.mainloop()
