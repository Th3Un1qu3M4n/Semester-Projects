import subprocess
from tkinter import *
import sqlite3

viewManagement = Tk()
viewManagement.title('All Users')
viewManagement.configure(background='white')


def main_menu():
    viewManagement.destroy()

def delete(userId):
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    c.execute("DELETE FROM management WHERE oid="+str(userId))
    
    conn.commit()
    conn.close()
    print(userId)
    viewManagement.destroy()
    subprocess.Popen('python viewManagement.pyw', shell=True)
    
conn = sqlite3.connect('cms.db')
c= conn.cursor()

c.execute("SELECT oid,* FROM management WHERE role=? ORDER BY oid ASC",('manage',))
records = c.fetchall()

caption_label= Label(viewManagement, text='Management', bg = 'grey', fg='white', width= 25, font=('Roman 20 bold')).grid(row=0, column=2, pady=5)
username_label = Label(viewManagement, text="Username", bg="#034036", fg='white', font =('Cambria 10 bold'))
username_label.grid(row=1,column=0, ipadx=50)
name_label = Label(viewManagement, text="Name", bg="#034036", fg='white', font =('Cambria 10 bold'))
name_label.grid(row=1,column=1, ipadx=50)
email_label = Label(viewManagement, text="Email", bg="#034036", fg='white', width=29, font =('Cambria 10 bold'))
email_label.grid(row=1,column=2, ipadx=50)
pNumber_label = Label(viewManagement, text="Phone Number", bg="#034036", fg='white', font =('Cambria 10 bold'))
pNumber_label.grid(row=1,column=3, ipadx=50)
approve_label = Label(viewManagement, text="Action", bg="#034036", fg='white', font =('Cambria 10 bold'))
approve_label.grid(row=1,column=4, ipadx=50)

count = 2
approve_btn = []
for record in records:

    username = Label(viewManagement, text=record[1])
    username['bg']=username.master['bg']
    username.grid(row=count,column=0)
    name = Label(viewManagement, text=record[2])
    name['bg']=name.master['bg']
    name.grid(row=count,column=1)
    email = Label(viewManagement, text=record[3])
    email['bg']=email.master['bg']
    email.grid(row=count,column=2)
    pNumber = Label(viewManagement, text=record[4])
    pNumber['bg']=pNumber.master['bg']
    pNumber.grid(row=count,column=3)
    approve_btn.append(Button(viewManagement, text="delete", command=lambda record=record: delete(record[0]), bg = '#a1aba9', fg='white', font=('Cambria 9 bold')))
    approve_btn[count-2].grid(row=count, column=4)
    count += 1

back_btn = Button(viewManagement, text="Back", command=main_menu, bg = 'red', fg='white', font = ("Cambria 10 bold"))
back_btn.grid(row=10, column=count, pady=10, padx=10, ipadx=20)
conn.commit()
conn.close()
    
viewManagement.mainloop()
