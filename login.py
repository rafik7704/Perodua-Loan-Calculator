from tkinter import *
#import library
from time import strftime
import mysql.connector
from config import *
#open databse
#defining login function
def login():
    #getting form data
    connection = mysql.connector.connect(
      host=hosted,
      user=user1,
      password=datapass,
      port=dataport,
      database=databased)
    c = connection.cursor()
    uname=username.get()
    pwd=password.get()
    actv=activation.get()
   
        #print(c.fetchall())
    
    #applying empty validation
    if uname=='' or pwd=='' or actv=='':
        message.set("fill the empty field!!!") 
    else:
      #open database
      select_query = 'SELECT * FROM `ADMIN` WHERE `USERNAME` = %s and PASSWORD = %s and ACTIVATION = %s' 
      vals = (uname,pwd,actv)
      c.execute(select_query, vals)
      user = c.fetchone()
      if user is not None:
       message.set("Login success")
       login_screen.destroy()
       import database
      else:
       message.set("Wrong username or password!!!")
#defining loginform function

def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("LOG MASUK PERODUA CALCULATOR")
    login_screen.iconbitmap("images\perodua.ico")
    #setting height and width of screen
    login_screen.geometry("350x300")
    login_screen["bg"]="#1C2833"
    #declaring variable
    
    lbl = Label(login_screen,bg="#1C2833",fg="white",font=("Arial",11,"bold"))
    
    global  message 
    global username
    global password
    global activation
    username = StringVar()
    password = StringVar()
    message=StringVar()
    activation=StringVar()
    #Creating layout of login form
    Label(login_screen,width="450", text="LOG MASUK ", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Username:",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=50)
    #Username textbox
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=52)
    #Password Label
    Label(login_screen, text="Password: ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
     #Password Label
    Label(login_screen, text="Pin:",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=120)
    #Password textbox
    Entry(login_screen, textvariable=activation,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=122)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=70,y=150)
    #Login button
    Button(login_screen, text="Login", width=11, height=2, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=100,y=200)
   
    def time():
     string = strftime('%H:%M:%S %p')
     lbl.config(text = string)
     lbl.after(10,time)
    lbl.pack(anchor = 'sw')
    
    time()
    login_screen.mainloop()
#calling function Loginform
Loginform()



