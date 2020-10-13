import subprocess
from tkinter import *
from tkinter import ttk,filedialog
import sqlite3
from datetime import datetime, date

insert = Tk()
insert.title('Add New Movie')
insert.configure(bg='#fafcfc')
insert.geometry('455x250')

def main_menu():
    insert.destroy()

def fileDialog():
        filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpeg files","*.jpg"),("All","*.*")) )
        
        path.insert(0, filename)
        
                
def submit():
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()
    timeDict = {
            "4:00 PM":"1600",
            "7:00 PM":"1900",
            "10:00 PM":"2200",
            "1:00 AM":"100"
        }

    timeSubmitted = timeDict[time.get()]
    print(timeSubmitted)

    dateSubmitted=date(eval(year.get()),eval(month.get()),eval(date1.get()))
    print(dateSubmitted)

    file=open(path.get(), 'rb')
    image= file.read()
    file.close()
    
    c.execute("INSERT INTO movies VALUES(:name, :desc, :language, :subtitle, :price, :time, :date, :tickets, :cover)",
            {                 
                'name':name.get(),
                'desc':desc.get(),
                'language':language.get(),
                'subtitle':subtitle.get(),
                'price':price.get(),
                'time':timeSubmitted,
                'date':dateSubmitted,
                'tickets':tickets.get(),
                'cover':image
                        })
        
    name.delete(0, END)
    desc.delete(0, END)
    language.delete(0, END)
    subtitle.delete(0, END)
    price.delete(0, END)
    time.delete(0, END)
    date1.delete(0, END)
    month.delete(0, END)
    year.delete(0, END)
    name.focus()
    
    message_label.configure(text="Movie Added Successfully!")
    
    conn.commit()
    conn.close()

name = Entry(insert, width=60)
name.grid(row=1, column=1, columnspan=6, pady=5)
desc = Entry(insert, width=60)
desc.grid(row=2, column=1, columnspan=6, pady=5)
language = ttk.Combobox(insert,values=["urdu","english"], width=10, state="readonly")
language.grid(row=3, column=1)
language.current(0)
subtitle = ttk.Combobox(insert,values=["no","yes"], width=10, state="readonly")
subtitle.grid(row=3, column=3, pady=5)
subtitle.current(0)
price = Entry(insert, width=13)
price.grid(row=5, column=1, pady=5)
time = ttk.Combobox(insert,values=["4:00 PM","7:00 PM","10:00 PM","1:00 AM"], width=10, state="readonly")
time.grid(row=5, column=3, pady=5)
time.current(0)
date1 = ttk.Combobox(insert,values=[*range(1,32)], width=10, state="readonly")
date1.grid(row=7, column=1, pady=5)
date1.current(0)
month = ttk.Combobox(insert,values=[*range(1,13)], width=10, state="readonly")
month.grid(row=7, column=3, pady=5)
month.current(0)
year = ttk.Combobox(insert,values=[*range(2019,2026)], width=10, state="readonly")
year.grid(row=7, column=5, pady=5)
year.current(0)
tickets = Entry(insert, width=10)
tickets.grid(row=3, column=5, pady=5)
name.focus()

name_label = Label(insert, text="Name")
name_label['bg']=name_label.master['bg']
name_label.grid(row=1, column=0)
desc_label = Label(insert, text="Description")
desc_label['bg']=desc_label.master['bg']
desc_label.grid(row=2, column=0)
language_label = Label(insert, text="language")
language_label['bg']=language_label.master['bg']
language_label.grid(row=3, column=0)
subtitle_label = Label(insert, text="Subtitle")
subtitle_label['bg']=subtitle_label.master['bg']
subtitle_label.grid(row=3, column=2)
price_label = Label(insert, text="Price")
price_label['bg']=price_label.master['bg']
price_label.grid(row=5, column=0)
time_label = Label(insert, text="Time")
time_label['bg']=time_label.master['bg']
time_label.grid(row=5, column=2)
date_label = Label(insert, text="Date")
date_label['bg']=date_label.master['bg']
date_label.grid(row=7, column=0)
month_label = Label(insert, text="Month")
month_label['bg']=month_label.master['bg']
month_label.grid(row=7, column=2)
year_label = Label(insert, text="Year")
year_label['bg']=year_label.master['bg']
year_label.grid(row=7, column=4)
tickets_label = Label(insert, text="Total Tickets")
tickets_label['bg']=tickets_label.master['bg']
tickets_label.grid(row=3, column=4)
file_label = Label(insert, text = "Thumbnail")
file_label.grid(row = 4, column = 0)

path = Entry(insert, width=45)
path.grid(row = 4, column = 1, columnspan=4)

cover = Button(insert, text = "Select Cover", bg='grey', fg='white',command=fileDialog)
cover.grid(row = 4, column = 5)

submit_btn = Button(insert, text="Add Movie", bg='grey', fg='white', command=lambda path=path: submit())
submit_btn.grid(row=10, column=2, columnspan=2, pady=10, padx=10)
back_btn = Button(insert, text="Back", bg='red', fg='white', command=main_menu)
back_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10)

message_label = Label(insert, text="")
message_label['bg']=message_label.master['bg']
message_label.grid(row=11, column=0, columnspan=2)

insert.mainloop()
