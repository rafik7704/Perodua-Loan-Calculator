from tkinter import Tk
from tkinter import *
import os
from xmlrpc.client import boolean
from PIL import Image, ImageTk
import mysql.connector

root = Tk()
root.iconbitmap("perodua.ico")
root.title('Perodua Loan Calculator')
root.geometry("1020x800")
root.state("zoomed")

canvas = Canvas(root, width = 415, height = 283)  
canvas.pack(padx=0, pady=0, side=RIGHT)  
img = PhotoImage(file="bank.jpg")  
canvas.create_image(0, 0, anchor=NW, image=img)  

connection = mysql.connector.connect(
      host='sql12.freemysqlhosting.net',
      user='sql12541617',
      password='I8fgmNLepp',
      port='3306',
      database='sql12541617')
c = connection.cursor()




def payment():
    if  commitment_entry.get() and year_entry.get() and kwsp_entry.get() and salary_entry.get() or nama_entry.get() and rate_entry.get():
        
        
        kwsp= int(kwsp_entry.get())
        salary=int(salary_entry.get()) 
        years = int(year_entry.get())
        bank=(rate_entry.get())
        
        commitment = int(commitment_entry.get()) 
        nama=(nama_entry.get())
        
        car_model=(car_entry.get())
        
        select_query = 'SELECT * FROM FAEDAH WHERE BANK="{}"'.format(bank)
        c.execute(select_query)
        user = c.fetchone()
        rate=float(user[1])
        full_bank =(user[2])
        
        
        select_query = 'SELECT * FROM HARGA WHERE CARMODEL="{}"'.format(car_model)
        c.execute(select_query)
        user = c.fetchone()
        full_model=(user[2])
        car_price =float(user[1])
        otr_price=float(user[3])
        
        
        
        month=(years*12)
        deposit=int((10/100)*otr_price)
        carchange=int((90/100)*otr_price)
        net_salary=(salary-kwsp-commitment)
        car_monthly=((carchange)+(((carchange)*(rate/100)*years))) / (month)
        car_monthly = int(car_monthly)
        insurance=otr_price-car_price
        salarym = int((car_monthly))*3
        
        
        
        nama_label.config(text=f"Nama: {nama}")
        model_label.config(text=f"Model Kereta:{full_model}"+os.linesep+f"Gaji Bersih:RM {net_salary}")
        payment_label.config(text=F"Harga OTR(*Selepas Deposit 10%*):RM {carchange}"+os.linesep+F"Harga Insurans termasuk cukai:RM {insurance}"+os.linesep+F"Deposit:RM {deposit}"+os.linesep+F"Bayaran Bulanan:RM {car_monthly}"+os.linesep+F"Bank Pilihan:{full_bank} {rate}%")
       
        if  salarym<net_salary:
          result_label.config(text="TAHNIAH!!! ANDA LAYAK UNTUK MEMBUAT PINJAMAN")
        elif salarym>net_salary:
          result_label.config(text=f'''MAAF ANDA TIDAK LAYAK UNTUK MEMBUAT PINJAMAN
     Gaji Bersih Minimum Untuk Layak:RM {salarym}''')
          
         
    else:
        payment_label.config(text="Anda Lupa Untuk Memasukkan Amaun...") 





my_label_frame = LabelFrame(root, text="Loan Calculator")
my_label_frame.pack(pady=0)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=30)



nama_label = Label(my_frame, text="Nama:")
nama_entry = Entry(my_frame, font=("Helvetica", 18))

commitment_label = Label(my_frame, text="Komitmen Bank:")
commitment_entry = Entry(my_frame, font=("Helvetica", 18))

kwsp_label = Label(my_frame, text="Potongan KSWP:")
kwsp_entry = Entry(my_frame, font=("Helvetica", 18))

salary_label = Label(my_frame, text="Gaji: ")
salary_entry = Entry(my_frame,font=("Helvetica", 18))

year_label = Label(my_frame, text="Tempoh Pinjaman:")
year_entry = Entry(my_frame, font=("Helvetica", 18))

car_label = Label(my_frame, text="Model Kereta:")
car_entry = Entry(my_frame, font=("Helvetica", 18))

rate_label = Label(my_frame, text="Bank Pilihan:")
rate_entry = Entry(my_frame, font=("Helvetica", 18))




nama_label.grid(row=0, column=0)
nama_entry.grid(row=0, column=1,pady=10)

commitment_label.grid(row=3, column=0)
commitment_entry.grid(row=3, column=1)

kwsp_label.grid(row=2, column=0)
kwsp_entry.grid(row=2, column=1,pady=5)

salary_label.grid(row=1, column=0)
salary_entry.grid(row=1, column=1,pady=10)

year_label.grid(row=5, column=0)
year_entry.grid(row=5, column=1, pady=10)

car_label.grid(row=4, column=0,)
car_entry.grid(row=4, column=1,pady=10)

rate_label.grid(row=6, column=0, pady=10)
rate_entry.grid(row=6, column=1,pady=10)


 
my_button = Button(my_label_frame,text="Kira Bayaran", command=payment,bg='black',fg='white')
my_button.pack(pady=0)



 
nama_label = Label(root, text="", font=("Helvetica", 12))
nama_label.pack(pady=0) 
model_label = Label(root, text="", font=("Helvetica", 12))
model_label.pack(pady=0) 
payment_label = Label(root, text="", font=("Helvetica", 12))
payment_label.pack(pady=0)
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=0,side=RIGHT)

root.mainloop()



