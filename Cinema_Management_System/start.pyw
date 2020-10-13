import subprocess
from tkinter import *

main = Tk()
main.title('Cinema Management System')
main.configure(background ='black')
main.geometry('650x520')

def userLogin():
    main.destroy()
    subprocess.Popen("python login.pyw", shell=True)
    
def manLogin():
    main.destroy()
    subprocess.Popen("python m_login.pyw", shell=True)

def closeProgram():
    main.destroy()
    
submit_label =Label(main, text="Submitted By :", bg='black', fg='#45e9ff',font=('Century 18 bold')).grid(row=6, column=0, columnspan=2, pady=5, ipadx=25)
std_label =Label(main, text="Muhammad Ahmed (FA19-BCS-041) ", bg='black', fg='#45e9ff',font=('Century 18 bold')).grid(row=7, column=0, columnspan=2, pady=5, ipadx=10)
std2_label =Label(main, text="Faiq Shahzad (FA19-BCS-021) ", bg='black', fg='#45e9ff',font=('Century 18 bold')).grid(row=8, column=0, columnspan=2, pady=5, ipadx=10)
main_label= Label(main, text="WELCOME TO CINEMA MANAGEMENT SYSTEM", font=("Algerian 22 bold italic"))
main_label['bg']=main_label.master['bg']
main_label.configure(foreground = 'white')
main_label.grid(row=1, column=0, columnspan=2, pady=10)

user_btn = Button(main, text="User Login", command=userLogin, width = 18, height = 4, bg='white',fg='#415fba', font=("Cambria 14 bold"))
user_btn.grid(row = 3, column=0, padx=10, pady =60)

admin_btn= Button(main, text="Management Login", command=manLogin, width = 18, height=4, bg='white',fg='#15204d', font=("Cambria 14 bold"))
admin_btn.grid(row =3, column=1, pady=60)

exit_btn= Button(main, text="EXIT", command=closeProgram, width = 14, bg= 'red', fg='white',font=("Cambria 10 bold"))
exit_btn.grid(row=5, column=0, columnspan=2, pady=20, padx=90)

main.mainloop()
