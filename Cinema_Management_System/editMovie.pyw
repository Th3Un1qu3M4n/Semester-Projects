import subprocess
from tkinter import *
from tkinter import messagebox,ttk
import sqlite3

editMovie = Tk()
editMovie.title('Edit Movie')
editMovie.configure(bg='#fafcfc')
editMovie.geometry('500x400')


def main_menu():
    editMovie.destroy()

def edit(movieId):
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    timeDict = {
            "4:00 PM":"1600",
            "7:00 PM":"1900",
            "10:00 PM":"2200",
            "1:00 AM":"100"
        }
    timeSubmitted = timeDict[time.get()]

    c.execute("""UPDATE movies SET
                name = :name,
                desc = :desc,
                language = :language,
                subtitle = :subtitle,
                price = :price,
                time = :time,
                date = :date,
                tickets=:tickets
                
                WHERE oid=:oid""",
                  {
                    'name':name.get(),
                    'desc':desc.get(),
                    'language':language.get(),
                    'subtitle':subtitle.get(),
                    'price':price.get(),
                    'time':timeSubmitted,
                    'date':date.get(),
                    'tickets':seats.get(),
                    'oid':movieId
                      })
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Movie Updated!")
    editMovie.destroy()
    subprocess.Popen('python editMovie.pyw', shell=True)
    

sessionFile= open('sessionA.txt', 'r')
lines=sessionFile.read().splitlines()
movieId=lines[1]
sessionFile.close()
print(movieId)

conn = sqlite3.connect('cms.db')
c= conn.cursor()

c.execute("SELECT * FROM movies WHERE oid="+str(movieId))
records = c.fetchall()

name = Entry(editMovie, width=60)
name.grid(row=2, column=1, columnspan=6, pady=5)
desc = Entry(editMovie, width=60)
desc.grid(row=3, column=1, columnspan=6, pady=5)
language = ttk.Combobox(editMovie,values=["urdu","english"], width=10, state="readonly")
language.grid(row=4, column=1)
subtitle = ttk.Combobox(editMovie,values=["no","yes"], width=10, state="readonly")
subtitle.grid(row=4, column=3, pady=5)
price = Entry(editMovie, width=13)
price.grid(row=6, column=1, pady=5)
time = ttk.Combobox(editMovie,values=["4:00 PM","7:00 PM","10:00 PM","1:00 AM"], width=10, state="readonly")
time.grid(row=6, column=3, pady=5)
date = Entry(editMovie, width=15)
date.grid(row=8, column=1, pady=5)
seats = Entry(editMovie, width=15)
seats.grid(row=8, column=3, pady=5)
name.focus()

caption_label= Label(editMovie, text='Edit Movie', bg='grey', fg='white', font=('Cambria 25 bold'))
caption_label.grid(row=0, column=1, columnspan=3, pady=10)
name_label = Label(editMovie, text="Name", bg='#fafcfc')
name_label.grid(row=2, column=0)
desc_label = Label(editMovie, text="Description", bg='#fafcfc')
desc_label.grid(row=3, column=0)
language_label = Label(editMovie, text="Language", bg='#fafcfc')
language_label.grid(row=4, column=0)
subtitle_label = Label(editMovie, text="Subtitle", bg='#fafcfc')
subtitle_label.grid(row=4, column=2)
price_label = Label(editMovie, text="Price", bg='#fafcfc')
price_label.grid(row=6, column=0)
time_label = Label(editMovie, text="Time", bg='#fafcfc')
time_label.grid(row=6, column=2)
date_label = Label(editMovie, text="Date", bg='#fafcfc')
date_label.grid(row=8, column=0)
seats_label = Label(editMovie, text="Seats", bg='#fafcfc')
seats_label.grid(row=8, column=2)

for record in records:
    timeDict = {
            "1600":"4:00 PM",
            "1900":"7:00 PM",
            "2200":"10:00 PM",
            "100":"1:00 AM"
        }

    timeSubmitted = timeDict[record[5]]

    name.insert(0, record[0])
    desc.insert(0, record[1])
    language.set(record[2])
    subtitle.set(record[3])
    price.insert(0, record[4])
    time.set(timeSubmitted)
    date.insert(0, record[6])
    seats.insert(0, record[7])
 
    
edit_btn = Button(editMovie, text="Save Changes", bg='grey', fg='white', command=lambda movieId=movieId: edit(movieId))
edit_btn.grid(row=9, column=1)

back_btn = Button(editMovie, text="Back", bg='red', fg='white', command=main_menu)
back_btn.grid(row=9, column=0, pady=10, padx=10, ipadx=20)

conn.commit()
conn.close()
    
editMovie.mainloop()
