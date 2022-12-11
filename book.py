 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:13:43 2022

@author: AnantSrivastava
"""
from tkinter import*
import smtplib
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.attributes('-fullscreen', True)
root.configure(bg="#45b1e8")



label_heading=Label(root, text="Reserve a Parent!", font=("times",40,"bold"),fg="Orange")
label_heading.place(relx=0.5,rely=0.16,anchor=CENTER)


label_select_dish=Label(root,text="Select Human ",font=("times",15))
label_select_dish.place(relx=0.42,rely=0.26,anchor=CENTER)


dish=["Mummy","Papa"]
dish_dropdown=ttk.Combobox(root, state="readonly",value=dish)
dish_dropdown.place(relx=0.42,rely=0.3,anchor=CENTER)


label_select_addons=Label(root,text="Select Duration", font=("times",15))
label_select_addons.place(relx=0.42,rely=0.36,anchor=CENTER)


toppings=["10 Mins", "15 Mins","20 Mins","25 Mins","30 Mins"]
toppings_dropdown=ttk.Combobox(root,state="readonly",values=toppings)
toppings_dropdown.place(relx=0.42, rely=0.4,anchor=CENTER)


label_select_day=Label(root,text="Select Day", font=("times",15))
label_select_day.place(relx=0.42,rely=0.46,anchor=CENTER)


day=["Today", "Tomorrow"]
day_dropdown=ttk.Combobox(root,state="readonly",values=day)
day_dropdown.place(relx=0.42, rely=0.5,anchor=CENTER)


label_select_loc=Label(root,text="Select Location", font=("times",15))
label_select_loc.place(relx=0.58,rely=0.26,anchor=CENTER)


loc=["Anant's Room", "Aradhana's Room","Zimbawbe"]
loc_dropdown=ttk.Combobox(root,state="readonly",values=loc)
loc_dropdown.place(relx=0.58, rely=0.3,anchor=CENTER)


label_select_name=Label(root,text="Select Your Name", font=("times",15))
label_select_name.place(relx=0.58,rely=0.36,anchor=CENTER)


name=["Anant", "Aradhana"]
name_dropdown=ttk.Combobox(root,state="readonly",values=name)
name_dropdown.place(relx=0.58, rely=0.4,anchor=CENTER)


label_select_name=Label(root,text="Slurp or NO Slurp", font=("times",15))
label_select_name.place(relx=0.58,rely=0.46,anchor=CENTER)


slurp=["YEAAHHHHH SLURPPPPP", "NO SLURP(Im a loser)"]
slurp_dropdown=ttk.Combobox(root,state="readonly",values=slurp)
slurp_dropdown.place(relx=0.58, rely=0.5,anchor=CENTER)











dish_amount=Label(root,font=("times",25,"bold"))
dish_amount.place(relx=0.5,rely=0.75,anchor=CENTER)



lol_amount=Label(root,font=("times",25,"bold"))
lol_amount.place(relx=0.5,rely=0.9,anchor=CENTER)
lol_amount.config(fg="#FF0000")
lol_amount.config(bg="#45b1e8")






def book():
    person=dish_dropdown.get()
    time=toppings_dropdown.get()
    day=day_dropdown.get()
    loc=loc_dropdown.get()
    name=name_dropdown.get()
    slurp=slurp_dropdown.get()
    

    dish_amount ["text"]=(person) +" has been booked by "+(name)+ " for "+(time)+" at "+(loc)+ ". "+(person)+" has been booked for "+(day)
    lol_amount ["text"]=" "
    if dish_dropdown.index("end") == 0:
        noname()
        
    if slurp_dropdown.index("end") == 0:
        noslurp()
        
    if toppings_dropdown.index("end") == 0:
        notime()
        
    if day_dropdown.index("end") == 0:
        noday()
        
    if loc_dropdown.index("end") == 0:
         noloc()
         
    if name_dropdown.index("end") == 0:
         nouser()
counter=0       
def noname():
     lol_amount ["text"]=" PLEASE SELECT NAME!!! "
     counter+1
     
def noslurp():
     lol_amount ["text"]=" PLEASE SELECT SLURPING OPTION!!! "
     dish_amount ["text"]=" "
     counter+1
     
def notime():
    lol_amount ["text"]=" PLEASE SELECT A TIME!!! "
    dish_amount ["text"]=" "
    counter+1
    
def noday():
    lol_amount ["text"]=" PLEASE SELECT A DAY!!! "
    dish_amount ["text"]=" "
    counter+1
    
def noloc():
    lol_amount ["text"]="PLEASE SELECT A LOCATION!!! "
    dish_amount ["text"]=" "
    counter+1
    
def nouser():
    lol_amount ["text"]=" PLEASE SELECT YOUR NAME!!! "
    dish_amount ["text"]=" "
    counter+1
    
    if (counter<4):
        lol_amount ["text"]="PLEASE FILL IN ALL OPTIONS"
        dish_amount ["text"]=" "
        

from email.message import EmailMessage
def mail():
    
# set your email and password
# please use App Password
    email_address = "email.anantsrivastava@gmail.com"
    email_password = "Anant1234#"

# create email
    msg = EmailMessage()
    msg['Subject'] = "Email subject"
    msg['From'] = email_address
    msg['To'] = "to-address@gmail.com"
    msg.set_content("This is eamil message")

# send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        
    
    
send=Button(root, text="SEND EMAIL CONFERMATION",command=mail)
send.place(relx=0.5, rely=0.64,anchor=CENTER)

btn=Button(root, text="CONFIRM RESERVATION",command= book)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)





root.mainloop()
