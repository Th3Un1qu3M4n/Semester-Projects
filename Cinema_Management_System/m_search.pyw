import subprocess
from tkinter import *
from tkinter import messagebox,ttk
import sqlite3
from PIL import ImageTk,Image
from io import BytesIO

searchBy = Tk()
searchBy.title('Search Movies')
searchBy.configure(background='white')

def refresh():
    searchBy.destroy()
    subprocess.Popen('python m_search.pyw',shell=True)


def callBack(self, mode, callback):
     global searchValue
     if searchType.get()=="name":
          searchValue = Entry(searchBy, width=23)
          searchValue.grid(row=0, column=2, pady=(10,0))
     if searchType.get()=="language":
          entryValue=["english","urdu"]
          searchValue = ttk.Combobox(searchBy, values=entryValue, state="readonly", width=20)
          searchValue.grid(row=0, column=2,pady=(10,0))
          searchValue.current(0)
     if searchType.get()=="time":
          entryValue=["4:00 PM","7:00 PM","10:00 PM", "1:00 AM"]
          searchValue = ttk.Combobox(searchBy, values=entryValue, state="readonly", width=20)
          searchValue.grid(row=0, column=2,pady=(10,0))
          searchValue.current(0)
    

def main_menu():
    searchBy.destroy()

def view_movie(movieId):
    sessionFile= open('sessionA.txt')
    lines= sessionFile.readlines()
    sessionFile.close()
    if len(lines)!=1:
        sessionFile= open('sessionA.txt','w')
        lines[1]=str(movieId)
        sessionFile.writelines(lines)
        sessionFile.close()
    else:
        sessionFile.close()
        sessionFile= open('sessionA.txt','a')
        data="\n"+str(movieId)
        sessionFile.writelines(data)
        sessionFile.close()
    subprocess.Popen('python m_viewMovie.pyw',shell=True)
    
def edit_movie(movieId):
    sessionFile= open('sessionA.txt')
    lines= sessionFile.readlines()
    sessionFile.close()
    if len(lines)!=1:
        sessionFile= open('sessionA.txt','w')
        lines[1]=str(movieId)
        sessionFile.writelines(lines)
        sessionFile.close()
    else:
        sessionFile.close()
        sessionFile= open('sessionA.txt','a')
        data="\n"+str(movieId)
        sessionFile.writelines(data)
        sessionFile.close()
    subprocess.Popen('python editMovie.pyw',shell=True)

def delete_movie(movieId):
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()

    c.execute("DELETE FROM movies where oid="+str(movieId))

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Movie Deleted!")
    searchBy.destroy()
    subprocess.Popen('python m_search.pyw',shell=True)
    
def searchMovies(searchtype, searchValue):
     
    for widget in recordsframe.winfo_children():
        widget.destroy()

    if searchtype=='time':
         timeDict = {
            "4:00 PM":"1600",
            "7:00 PM":"1900",
            "10:00 PM":"2200",
            "1:00 AM":"100"
        }

         timeSubmitted = timeDict[searchValue]
         print(timeSubmitted)
        
    conn = sqlite3.connect('cms.db')
    c= conn.cursor()
        
    c.execute("DROP TABLE IF EXISTS Moviesearch")
    c.execute("CREATE VIRTUAL TABLE Moviesearch USING fts5(id, name, language, time, date, tickets, cover);")

    c.execute("INSERT INTO Moviesearch SELECT oid, name, language, time, date, tickets, cover FROM movies;")

    if searchtype=='name':
          c.execute("SELECT * FROM Moviesearch WHERE name MATCH '"+searchValue+"';")
    elif searchtype=='language':
       c.execute("SELECT * FROM Moviesearch WHERE language MATCH '"+searchValue+"';")
    elif searchtype=='time':
       c.execute("SELECT * FROM Moviesearch WHERE time MATCH '"+timeSubmitted+"';")

    records = c.fetchall()
    conn.commit()
    conn.close()
    
    
    cover = Label(recordsframe, text="Cover", bg="#36afbf", width=10, font=("Cambria 14 bold")).grid(row=1,column=0, ipadx=100)
    details_label = Label(recordsframe, text="Details", bg="#36afbf", width=10, font=("Cambria 14 bold")).grid(row=1,column=1, columnspan=2, ipadx=55)
    action_label = Label(recordsframe, text="Actions", bg="#36afbf", width=10, font=("Cambria 14 bold")).grid(row=1,column=6, ipadx=10)
    count = 1
    imageCount=2
    global photos
    photos=[]
    view_btn = []
    edit_btn = []
    delete_btn = []
    for record in records:
        timeDict = {
                "1600":"4:00 PM",
                "1900":"7:00 PM",
                "2200":"10:00 PM",
                "100":"1:00 AM"
            }

        timeToDisplay = timeDict[record[3]]
            
                
        img=  Image.open(BytesIO(record[6]))
        img.thumbnail((200,200))
        photos.append((ImageTk.PhotoImage(img)))

        panel= Label(recordsframe, image = photos[count-1], relief="groove").grid(row=imageCount, column=0,rowspan=5,padx=2, pady=2)
        language_label = Label(recordsframe, text="Language :", fg='white', font=('Cambria 13 bold'))
        language_label['bg']=language_label.master['bg']
        language_label.grid(row=imageCount+1, column=1, ipadx=20) 
        time_label = Label(recordsframe, text="Time :", fg='white', font=('Cambria 13 bold'))
        time_label['bg']=time_label.master['bg']
        time_label.grid(row=imageCount+2,column=1, ipadx=35)
        date_label = Label(recordsframe, text="Date :", fg='white', font=('Cambria 13 bold'))
        date_label['bg']=date_label.master['bg']
        date_label.grid(row=imageCount+3,column=1, ipadx=35)
        seats_label = Label(recordsframe, text="Available Seats :", fg='white', font=('Cambria 13 bold'))
        seats_label['bg']=seats_label.master['bg']
        seats_label.grid(row=imageCount+4,column=1, ipadx=8)       
        name = Label(recordsframe, text=record[1], fg='#a7d4ae', font=("Cambria 15 bold"))
        name.grid(row=imageCount, column=1, columnspan=2, ipadx=2)
        name['bg']=name.master['bg']
        language = Label(recordsframe, text=record[2], fg='#0ceb2d', font=('Cambria 10 bold'))
        language['bg']=language.master['bg']
        language.grid(row=imageCount+1,column=2)
        time = Label(recordsframe, text=timeToDisplay, fg='#0ceb2d', font=('Cambria 10 bold'))
        time['bg']=time.master['bg']
        time.grid(row=imageCount+2,column=2)
        date = Label(recordsframe, text=record[4], fg='#0ceb2d', font=('Cambria 10 bold'))
        date['bg']=date.master['bg']
        date.grid(row=imageCount+3,column=2)
        seats = Label(recordsframe, text=record[5], fg='#0ceb2d', font=('Cambria 10 bold'))
        seats['bg']=seats.master['bg']
        seats.grid(row=imageCount+4,column=2)
        view_btn.append(Button(recordsframe, text="View", bg='#1d8ebf', fg='white', font=('Cambria 9 bold'), command=lambda record=record: view_movie(record[0])))
        view_btn[count-1].grid(row=imageCount+1, column=6, rowspan=1)
        edit_btn.append(Button(recordsframe, text="Edit", bg='#1d8ebf', fg='white', font=('Cambria 9 bold'), command=lambda record=record: edit_movie(record[0])))
        edit_btn[count-1].grid(row=imageCount+2, column=6, rowspan=1)
        delete_btn.append(Button(recordsframe, text="Delete", bg='#1d8ebf', fg='white', font=('Cambria 9 bold'), command=lambda record=record: delete_movie(record[0])))
        delete_btn[count-1].grid(row=imageCount+3, column=6, rowspan=1)
        imageCount+=5
        count += 1

    

    
recordsframe = Frame(searchBy)
recordsframe.configure(bg='#2a3436')
recordsframe.grid(row=2,column=0, columnspan=6, pady=2)

name_label = Label(searchBy, text="Search By", font=('Century 9'))
name_label['bg']= name_label.master['bg']
name_label.grid(row=0, column=0, pady=(10,0))

var= StringVar()
var.trace("w", callBack)
searchType = ttk.Combobox(searchBy, values=["name","language","time",],textvariable=var, state="readonly", width=10)
searchType.grid(row=0, column=1,pady=(10,0))
searchType.current(0)



search_btn = Button(searchBy, text="search", bg = 'cyan', command=lambda searchType=searchType: searchMovies(searchType.get(), searchValue.get()))
search_btn.grid(row=0, column=4, pady=10, padx=10, ipadx=5)

back_btn = Button(searchBy, text="Back", bg = 'red', fg='white', command=main_menu, font=('Cambria 10 bold'))
back_btn.grid(row=1, column=0, pady=10, padx=20)

refresh_btn = Button(searchBy, text="refresh", bg = '#49909e', command=refresh)
refresh_btn.grid(row=1, column=1, columnspan=2, pady=10)

searchBy.mainloop()
