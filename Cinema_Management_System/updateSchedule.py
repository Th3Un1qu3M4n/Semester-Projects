from datetime import date as dt
import sqlite3
from tkinter import *

root= Tk()
root.title("Update Schedule")

def oK():
    root.destroy()

conn = sqlite3.connect('cms.db')

c= conn.cursor()

fullDate = dt.today()

c_date=fullDate.strftime("%d")
month=fullDate.strftime("%m")
year=fullDate.strftime("%y")


c.execute("DELETE FROM movies WHERE date <'"+str(fullDate)+"';")
records=c.fetchall()

conn.commit()
conn.close()


msg=Label(root, text="Successfully updated Schedule!").pack(pady=10,padx=10)
btn = Button(root, text="OK", command=oK).pack()


root.mainloop()
