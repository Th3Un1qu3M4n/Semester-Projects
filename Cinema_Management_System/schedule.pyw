import subprocess
from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk,Image
from io import BytesIO

root = Tk()
root.geometry('1200x800')
root.configure(bg='white')
root.title('Cinema Schedule')
container = ttk.Frame(root)
canvas = Canvas(container, width=1180, height=700)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
schedule = ttk.Frame(canvas, style="My.TFrame")

schedule.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window((0, 0), window=schedule, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

container.grid(row=1, column=0, columnspan=5)
canvas.grid(row=0, column=0)
scrollbar.grid(row=0, column=2, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

s = ttk.Style()
s.configure('My.TFrame', background='#2a3436')

def refresh():
    root.destroy()
    subprocess.Popen('python schedule.pyw',shell=True)

def main_menu():
    root.destroy()
    
def view_movie(movieId):
    sessionFile= open('session.txt')
    lines= sessionFile.readlines()
    sessionFile.close()
    if len(lines)!=1:
        sessionFile= open('session.txt','w')
        lines[1]=str(movieId)
        sessionFile.writelines(lines)
        sessionFile.close()
    else:
        sessionFile.close()
        sessionFile= open('session.txt','a')
        data="\n"+str(movieId)
        sessionFile.writelines(data)
        sessionFile.close()
    subprocess.Popen('python viewMovie.pyw',shell=True)

conn = sqlite3.connect('cms.db')
c= conn.cursor()

c.execute("""SELECT
                    oid,*
                FROM
                    movies
                ORDER BY
                    date ASC;
                    """)
records = c.fetchall()
cover = Label(schedule, text="Cover", width=10, bg="#36afbf", font=("Cambria 22 bold")).grid(row=1,column=0, columnspan=5, ipadx=80)
details_label = Label(schedule, text="Details", width=10, bg="#36afbf", font=("Cambria 22 bold")).grid(row=1,column=5, columnspan=2, ipadx=200)
view_label = Label(schedule, text="Actions", width=10, bg="#36afbf", font=("Cambria 22 bold")).grid(row=1,column=8, ipadx=50)
count = 1
imageCount=2
view_btn = []
photos=[]
for record in records:
    timeDict = {
            "1600":"4:00 PM",
            "1900":"7:00 PM",
            "2200":"10:00 PM",
            "100":"1:00 AM"
        }

    timeToDisplay = timeDict[record[6]]
        
    img=  Image.open(BytesIO(record[9]))
    img.thumbnail((600,350))
    photos.append((ImageTk.PhotoImage(img)))

    panel= Label(schedule, image = photos[count-1], relief="groove").grid(row=imageCount, column=0, columnspan=5, rowspan=10,padx=2, pady=2)
    language_label = Label(schedule, text="Language :", bg='#2a3436', fg='white', font=('Cambria 20 bold'))
    language_label.grid(row=imageCount+1, column=5, ipadx=20) 
    time_label = Label(schedule, text="Time :", bg='#2a3436', fg='white', font=('Cambria 20 bold'))
    time_label.grid(row=imageCount+2,column=5, ipadx=35)
    date_label = Label(schedule, text="Date :", bg='#2a3436', fg='white', font=('Cambria 20 bold'))
    date_label.grid(row=imageCount+3,column=5, ipadx=35)
    seats_label = Label(schedule, text="Available Seats :", bg='#2a3436', fg='white', font=('Cambria 20 bold'))
    seats_label.grid(row=imageCount+4,column=5, ipadx=8)       
    name = Label(schedule, text=record[1], fg='#a7d4ae', bg='#2a3436', font=('Cambria 25 bold'))
    name.grid(row=imageCount, column=5, columnspan=2, ipadx=2)
    language = Label(schedule, text=record[3], fg='#0ceb2d', bg='#2a3436', font=('Cambria 18 bold'))
    language.grid(row=imageCount+1,column=6)
    time = Label(schedule, text=timeToDisplay, fg='#0ceb2d', bg='#2a3436', font=('Cambria 18 bold'))
    time.grid(row=imageCount+2,column=6)
    date = Label(schedule, text=record[7], bg='#2a3436', fg='#0ceb2d', font=('Cambria 18 bold'))
    date.grid(row=imageCount+3,column=6)
    seats = Label(schedule, text=record[8], fg='#0ceb2d', bg='#2a3436', font=('Cambria 18 bold'))
    seats.grid(row=imageCount+4,column=6)
    view_btn.append(Button(schedule, text="View", bg = 'cyan', command=lambda record=record: view_movie(record[0])))
    view_btn[count-1].grid(row=imageCount+1, column=8, rowspan=2, ipadx=10)
    imageCount+=10
    count += 1

Heading_label = Label(root, text="SCHEDULE", font=('Cambria 48 bold'))
Heading_label['bg']=Heading_label.master['bg']
Heading_label.grid(row=0,column=0, columnspan=2, padx=200)

back_btn = Button(root, text="Back", bg='red', fg='white', font=('Cambria 18 bold'), command=main_menu)
back_btn.grid(row=0, column=2, columnspan=1,  pady=5, ipadx=50)

refresh_btn = Button(root, text="refresh", bg='grey', fg='white', font=('Cambria 18 bold'), command=refresh)
refresh_btn.grid(row=0, column=3, pady=5, ipadx=40)

                
conn.commit()
conn.close()

root.mainloop()
