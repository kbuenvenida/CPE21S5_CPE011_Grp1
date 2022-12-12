# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:46:44 2022

@author: ATOM
"""

from tkinter import *
from tkinter import ttk, messagebox, NS,Canvas,Scrollbar
from PIL import ImageTk, Image
import tkinter as tk
import mysql.connector as mysql


def show_frame(frame):
    frame.tkraise()
root = tk.Tk()

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3=tk.Frame(root)

IVC=tk.Frame(root)
nangka=tk.Frame(root)
parang=tk.Frame(root)
concepcion1=tk.Frame(root)
concepcion2=tk.Frame(root)
mh=tk.Frame(root)
sanroque=tk.Frame(root)
staelena=tk.Frame(root)
stonino=tk.Frame(root)
tanong=tk.Frame(root)
barangka=tk.Frame(root)
malanday=tk.Frame(root)
JDP=tk.Frame(root)
kalumpang=tk.Frame(root)
fortune=tk.Frame(root)

global search
for frame in (frame1, frame2, frame3, IVC, nangka, parang, concepcion2, concepcion1,mh,sanroque,staelena,stonino,tanong,barangka,malanday,JDP,kalumpang,fortune):
    frame.grid(row=0,column=0,sticky='nsew')
    
#--------------------------------------------search location
def search_loc():
    location=search.get() 
    if (location == "IVC" or location == "ivc"):
        show_frame(IVC)
    elif (location == "nangka" or location == "Nangka" or location == "NANGKA"):
        show_frame(nangka)
    elif (location == "parang" or location == "Parang" or location == "PARANG"):
        show_frame(parang)
    elif (location == "conceptionI" or location == "concepcion I" or location == "CONCEPCION I"):
        show_frame(concepcion1)
    elif (location == "conceptionII" or location == "concepcion II" or location == "CONCEPCION II"):
        show_frame(concepcion2)
    elif (location == "marikina heights" or location == "MARIKINA HEIGHTS " or location == "Marikina Heights"):
         show_frame(mh)
    elif (location == "san roque" or location == "SAN ROQUE" or location == "San Roque"):
       show_frame(sanroque)
    elif (location == "sta elena" or location == "STA ELENA" or location == "Sta Elena"):
        show_frame(staelena)
    elif (location == "sto nino" or location == "Sto Nino" or location == "STO NINO"or location == "sto niño" or location == "Sto Niño"):
        show_frame(stonino)
    elif (location == "tanong" or location == "tañon" or location == "Tañong"):
        show_frame(tanong)
    elif (location == "barangka" or location == "Barangka" or location == "BARANGKA"):
        show_frame(barangka)
    elif (location == "Malanday" or location == "malanday" or location == "MALANDAY"):
        show_frame(malanday)
    elif (location == "jesus dela pena" or location == "Jesus Dela Peña" or location == "Jesus Dela Pena"):
        show_frame(JDP)
    elif (location == "kalumpang" or location == "Kalumpang" or location == "KALUMPANG"):
        show_frame(kalumpang)
    elif (location == "fortune" or location == "Fortune" or location == "FORTUNE"):
         show_frame(fortune)
    elif(location == ""):
        messagebox.showerror("","Blank is not allowed")
    else:
        messagebox.showinfo("","Incorect username or password")
def login():
    username=entry1.get()
    password=entry2.get()
    
    if (username=="" and password==""):
        messagebox.showerror("","Blank is not allowed")
    elif(username=="admin" and password=="admin" and var.get() == 1):
        show_frame(frame2)
    elif(username=="guest" and password=="guest" and var.get() == 2):
        show_frame(frame3)
    else:
        messagebox.showinfo("","Incorect username or password")
        
#-----------------------------------------------------------------------------------------------------------frame 1 code(LOGIN)
root.title("Hotline Express")
root.geometry("1160x820")
frame1.configure(bg="#071E22")
c=Canvas(frame1,bg="#071E22",height="1160",width="920")
filename=PhotoImage(file="C:\\Users\\ATOM\\Desktop\\Modules\\Data_Base\\login.png")
background_label1=Label(frame1,image=filename)
background_label1.place(x=0,y=0,relwidth=1, relheight=1)
c.pack()
icon = ImageTk.PhotoImage(Image.open("C:\\Users\\ATOM\\Desktop\\Modules\\Data_Base\\icon.png"))
root.iconphoto(False,icon)
#----------------------------text
Label(frame1,text = "USERNAME",font="arial 17 bold",bg="#071E22",fg="#4dccbd").place (x=750,y=260)
Label(frame1,text = "PASSWORD",font="arial 17 bold",bg="#071E22",fg="#4dccbd").place (x=750,y=360)
Label(frame1,text = "LOGIN ACCOUNT",font="arial 30 bold",bg="#071E22",fg="#4dccbd").place (x=735,y=130)

#------------------------------------textbox
entry1=Entry(frame1,bd=1)
entry1.place(x=753,y=295,height=30,width=300)

entry2=Entry(frame1,bd=1,show='*')
entry2.place(x=753,y=395,height=30,width=300)

#--------------------------------------button
mybutton = Button(frame1, text="LOGIN",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = login).place(x=860,y=560)

var=IntVar()
r1 = Radiobutton(frame1,text="ADMIN", value=1,font="arial 17 bold",bg="#071E22",fg="#4dccbd",variable = var).place(x=790,y=460)
r2 = Radiobutton(frame1,text="GUEST", value=2,font="arial 17 bold",bg="#071E22",fg="#4dccbd",variable = var).place(x=920,y=460)

#==============================================================================================================================frame 2 code (ADMIN)
frame2.configure(bg="#071E22")
Label(frame2,text = "ADMIN ACCOUNT",font="arial 30 bold",bg="#071E22",fg="#4dccbd").place (x=480,y=30)

#-----------------------------button
backbutton = Button(frame2, text="BACK",height=2,width=8,bd=1,font="arial 10 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame1)).place(x=20,y=20)
#----------------------------------------function 

def insert ():
    id = e_id.get()
    hotline_num = e_num1.get()
    mobile_num =e_num2.get()
    email = e_mail.get()
    dep_location = e_loc.get()
    dep_type = e_type.get()
    
    if (id==" " or  hotline_num=="" or mobile_num==""or dep_location==""or dep_type==""or email==""):
         messagebox.showinfo ("Insert Status", "All Fields are required")
    else:
         con = mysql.connect (host="localhost", user="root", password="", database="hex")
         cursor= con.cursor ()  
         cursor.execute ("insert into department values ('"+ id +"','"+ dep_type +"','"+ dep_location +"')")
         cursor.execute ("insert into contact values ('"+ id +"','"+ hotline_num +" ','" + mobile_num +" ','" + email +"')")
       
         cursor.execute("commit");
         
         e_id.delete(0, 'end')
         e_num1.delete(0, 'end')  
         e_num2.delete(0, 'end')   
         e_mail.delete(0, 'end')
         e_loc.delete (0, 'end')
         e_type.delete (0, 'end')
         
         show()
         messagebox.showinfo ("Create Status", "Created Successfully");
         con. close ();

def delete ():
     if (e_id.get () == ""):
         messagebox.showinfo ("Delete Status", "ID is compolsary for delete")
     else:
         con = mysql.connect (host="localhost", user="root", password="", database="hex")
         cursor = con.cursor ()
         cursor.execute ("delete from contact where id='"+ e_id.get() +" ' ")
         cursor.execute ("delete from department where id='"+ e_id.get() +" ' ")
         
         
         cursor.execute ("commit");
         
         e_id.delete(0, 'end')
         e_num1.delete(0, 'end')  
         e_num2.delete(0, 'end')   
         e_mail.delete(0, 'end')
         e_loc.delete (0, 'end')
         e_type.delete (0, 'end')
         
         show()
         messagebox.showinfo ("Delete status", "Deleted Successfully");
         con.close ();
         
def update (): 
    id = e_id.get()
    hotline_num = e_num1.get()
    mobile_num =e_num2.get()
    email = e_mail.get()
    dep_location = e_loc.get()
    dep_type = e_type.get()
    
    if (id==" " or  hotline_num=="" or mobile_num==""or dep_location==""or dep_type==""or email==""):
          messagebox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect (host="localhost", user="root", password="", database="hex")
        cursor = con.cursor()
        cursor.execute("update department set  dep_location='"+ dep_location +"', dep_type='"+ dep_type +"' where id='"+ id +"'") 
        cursor.execute("update contact set hotline_num='"+ hotline_num +"', mobile_num='"+ mobile_num +"', email='"+ email +"' where id='"+ id +"'") 
        cursor.execute ("commit");

        e_id.delete(0, 'end')
        e_num1.delete(0, 'end')  
        e_num2.delete(0, 'end')   
        e_mail.delete(0, 'end')
        e_loc.delete (0, 'end')
        e_type.delete (0, 'end')
        
        show()
        messagebox.showinfo("Update Status", "Updated Successfully");
        con.close();
        
def get():
    if(e_id.get() == ""):
        messagebox.showinfo("Fetch Status", "ID is compolsary for delete")
    else:
        con = mysql.connect (host="localhost", user="root", password="", database="hex")
        cursor = con.cursor()
       
        cursor.execute ("SELECT * FROM department JOIN contact USING (id) where id='"+ e_id.get() +"'")
        
        rows = cursor.fetchall()
        
        for row in rows:
            e_num1.insert (0, row[1])
            e_num2.insert(0, row[2]) 
            e_mail.insert(0, row[3]) 
            e_loc.insert(0, row[4]) 
            e_type.insert(0, row[4]) 
        con.close();

def show():
    con = mysql.connect (host="localhost", user="root", password="", database="HEX")
    cursor = con.cursor()
    cursor.execute ("SELECT * FROM department JOIN contact USING (id) ORDER BY id DESC")

    scrollbar = Scrollbar(frame2, orient = VERTICAL)
    scrollbar1 = Scrollbar(frame2, orient = HORIZONTAL)
    
    tree=ttk.Treeview(frame2,columns=4,show=["headings"])
    tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
    
    scrollbar.configure(command=tree.yview)
    scrollbar.place(relx=0.866,rely=0.475,width= 24, height = 349)
    
    scrollbar1.configure(command=tree.xview)
    scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 25)
    
    tree["columns"]=("id","dep_type","dep_location","hotline_num","mobile_num","email")
    
    tree.column("id", width=80, minwidth=100,anchor=tk.CENTER)
    tree.column("dep_type", width=100, minwidth=200,anchor=tk.CENTER)
    tree.column("dep_location", width=100, minwidth=200,anchor=tk.CENTER)
    tree.column("hotline_num", width=150, minwidth=200,anchor=tk.CENTER)
    tree.column("mobile_num", width=150, minwidth=200,anchor=tk.CENTER)
    tree.column("email", width=150, minwidth=200,anchor=tk.CENTER)
    
    tree.heading("id", text="ID",anchor=tk.CENTER)
    tree.heading("dep_type", text="DEPARTMENT",anchor=tk.CENTER)
    tree.heading("dep_location", text="DEPARTMENT LOCATION",anchor=tk.CENTER)
    tree.heading("hotline_num", text="HOTLINE NUMBER",anchor=tk.CENTER)
    tree.heading("mobile_num", text="MOBILE NUMBER",anchor=tk.CENTER) 
    tree.heading("email", text="EMAIL",anchor=tk.CENTER) 
     
    i = 0
    for ro in cursor:
        tree.insert("",i,values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i=i+i
        
    tree.place(x=150,y=390,height=350,width=850)   
  
    con.close();
#----------------------------------------TEXT & TEXTBOX
id = Label (frame2, text='Enter Department ID',font="arial 15 bold",bg="#071E22",fg="#4dccbd")
id.place(x=200,y=130)
e_id = Entry(frame2)
e_id.place (x=480, y=130,height=30,width=330)

hotline_num  = Label (frame2, text='Enter Hotline Number',font="arial 15 bold",bg="#071E22",fg="#4dccbd")
hotline_num .place (x=200,y=170)
e_num1 = Entry (frame2)
e_num1.place (x=480, y=170,height=30,width=330)

mobile_num = Label (frame2, text='Enter Mobile Number',font="arial 15 bold",bg="#071E22",fg="#4dccbd")
mobile_num.place (x=200,y=210);
e_num2 = Entry(frame2)
e_num2.place (x=480, y=210,height=30,width=330)

email = Label (frame2, text='Enter Department Email',font="arial 15 bold",bg="#071E22",fg="#4dccbd")
email.place (x=200,y=250);
e_mail = Entry(frame2)
e_mail.place (x=480, y=250,height=30,width=330)

dep_location = Label (frame2, text='Enter Department Location ',font="arial 15 bold",bg="#071E22",fg="#4dccbd")
dep_location.place (x=200,y=290);
e_loc = Entry(frame2)
e_loc.place (x=480, y=290,height=30,width=330)

dep_type = Label (frame2, text='Enter Department Type ',font="arial 15 bold",bg="#071E22",fg="#4dccbd")
dep_type.place (x=200,y=330);
e_type = Entry(frame2)
e_type.place (x=480, y=330,height=30,width=330)
#------------------------------------------COMMAND
insert=Button(frame2, text="CREATE",height=2,width=8,bd=1,font="arial 12 bold",bg="#4dccbd",fg="#071E22", command=insert)
insert.place(x=850,y=140,height=38,width=90)

delete=Button(frame2, text="DELETE",height=2,width=8,bd=1,font="arial 12 bold",bg="#4dccbd",fg="#071E22", command=delete)
delete.place(x=850,y=195,height=38,width=90) 

update=Button(frame2, text="UPDATE",height=2,width=8,bd=1,font="arial 12 bold",bg="#4dccbd",fg="#071E22", command=update)
update.place(x=850,y=250,height=38,width=90)

get=Button(frame2, text="GET",height=2,width=8,bd=1,font="arial 12 bold",bg="#4dccbd",fg="#071E22", command=get)
get.place(x=850,y=305, height=38,width=90)
list=Listbox(frame2)
show()

#============================================================================================================frame 3 code (GUEST)
frame3.configure(bg="#071E22")
Label(frame3,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(frame3, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame1)).place(x=40,y=40,height=40,width=90)
#----------------------------------------------search text box and button
Label (frame3, text='Find Department Location',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
search = Entry(frame3)
search.place(x=550,y=201,height=25,width=330)

search1 = Button(frame3, text = "SEARCH",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22", command = search_loc)
search1.place(x=900,y=195,height=40,width=90)

#--------------------------------------------------treeview
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute ("SELECT * FROM department JOIN contact USING (id) ORDER BY id DESC")

scrollbar = Scrollbar(frame3, orient = VERTICAL)
scrollbar1 = Scrollbar(frame3, orient = HORIZONTAL)
 
tree=ttk.Treeview(frame3,columns=5,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
 
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
 
tree["columns"]=("id","dep_type","dep_location","hotline_num","mobile_num","email")

tree.column("id", width=80, minwidth=100,anchor=tk.CENTER)
tree.column("dep_type", width=100, minwidth=200,anchor=tk.CENTER)
tree.column("dep_location", width=100, minwidth=200,anchor=tk.CENTER)
tree.column("hotline_num", width=150, minwidth=200,anchor=tk.CENTER)
tree.column("mobile_num", width=150, minwidth=200,anchor=tk.CENTER)
tree.column("email", width=150, minwidth=200,anchor=tk.CENTER)

tree.heading("id", text="ID",anchor=tk.CENTER)
tree.heading("dep_type", text="DEPARTMENT",anchor=tk.CENTER)
tree.heading("dep_location", text="DEPARTMENT LOCATION",anchor=tk.CENTER)
tree.heading("hotline_num", text="HOTLINE NUMBER",anchor=tk.CENTER)
tree.heading("mobile_num", text="MOBILE NUMBER",anchor=tk.CENTER) 
tree.heading("email", text="EMAIL",anchor=tk.CENTER) 
 
i = 0
for ro in conn:
    tree.insert("",i,values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
    i=i+i
tree.place(x=150,y=250,height=490,width=850)   
#----------------------------------------------------search bar function
def loc_frame():  
    tree["columns"]=("id","dep_type","dep_location","hotline_num","mobile_num","email")
    tree.column("id", width=80, minwidth=100,anchor=tk.CENTER)
    tree.column("dep_type", width=100, minwidth=200,anchor=tk.CENTER)
    tree.column("dep_location", width=100, minwidth=200,anchor=tk.CENTER)
    tree.column("hotline_num", width=150, minwidth=200,anchor=tk.CENTER)
    tree.column("mobile_num", width=150, minwidth=200,anchor=tk.CENTER)
    tree.column("email", width=150, minwidth=200,anchor=tk.CENTER)
  
    tree.heading("id", text="ID",anchor=tk.CENTER)
    tree.heading("dep_type", text="DEPARTMENT",anchor=tk.CENTER)
    tree.heading("dep_location", text="DEPARTMENT LOCATION",anchor=tk.CENTER)
    tree.heading("hotline_num", text="HOTLINE NUMBER",anchor=tk.CENTER)
    tree.heading("mobile_num", text="MOBILE NUMBER",anchor=tk.CENTER) 
    tree.heading("email", text="EMAIL",anchor=tk.CENTER) 
   
    i = 0
    for ro in conn:
        tree.insert("",i,values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i=i+i
    tree.place(x=150,y=250,height=490,width=850)  

#=================================================================================================IVC
IVC.configure(bg="#071E22")
Label(IVC,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(IVC, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(IVC,text='Department Location: IVC',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'IVC' ORDER BY id DESC ")
scrollbar = Scrollbar(IVC, orient = VERTICAL)
scrollbar1 = Scrollbar(IVC, orient = HORIZONTAL)
tree=ttk.Treeview(IVC,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()

#================================================================================================nangka
nangka.configure(bg="#071E22")
Label(nangka,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(nangka, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(nangka,text='Department Location: Nangka',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Nangka' ORDER BY id DESC ")
scrollbar = Scrollbar(nangka, orient = VERTICAL)   
scrollbar1 = Scrollbar(nangka, orient = HORIZONTAL) 
tree=ttk.Treeview(nangka,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================parang
parang.configure(bg="#071E22")
Label(parang,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(parang, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(parang,text='Department Location: Parang',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Parang' ORDER BY id DESC ")
scrollbar = Scrollbar(parang, orient = VERTICAL)   
scrollbar1 = Scrollbar(parang, orient = HORIZONTAL)  
tree=ttk.Treeview(parang,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================concepcion I
concepcion1.configure(bg="#071E22")
Label(concepcion1,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(concepcion1, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(concepcion1,text='Department Location: Concepcion I',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Concepcion I' ORDER BY id DESC ")
scrollbar = Scrollbar(concepcion1, orient = VERTICAL)   
scrollbar1 = Scrollbar(concepcion1, orient = HORIZONTAL)   
tree=ttk.Treeview(concepcion1,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================concepcion II
concepcion2.configure(bg="#071E22")
Label(concepcion2,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(concepcion2, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(concepcion2,text='Department Location: Concepcion II',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Concepcion II' ORDER BY id DESC ")
scrollbar = Scrollbar(concepcion2, orient = VERTICAL)   
scrollbar1 = Scrollbar(concepcion1, orient = HORIZONTAL)  
tree=ttk.Treeview(concepcion2,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================marikina heights
mh.configure(bg="#071E22")
Label(mh,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(mh, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(mh,text='Department Location: Marikina Heights',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Marikina Heights' ORDER BY id DESC ")
scrollbar = Scrollbar(mh, orient = VERTICAL)
scrollbar1 = Scrollbar(mh, orient = HORIZONTAL)
tree=ttk.Treeview(mh,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================san roque
sanroque.configure(bg="#071E22")
Label(sanroque,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(sanroque, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(sanroque,text='Department Location: San Roque',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'San Roque' ORDER BY id DESC ")
scrollbar = Scrollbar(sanroque, orient = VERTICAL)  
scrollbar1 = Scrollbar(sanroque, orient = HORIZONTAL)  
tree=ttk.Treeview(sanroque,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================sta elena
staelena.configure(bg="#071E22")
Label(staelena,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(staelena, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(staelena,text='Department Location: Sta. Elena',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Sta Elena' ORDER BY id DESC ")
scrollbar = Scrollbar(staelena, orient = VERTICAL)
scrollbar1 = Scrollbar(staelena, orient = HORIZONTAL)    
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================sto niño
stonino.configure(bg="#071E22")
Label(stonino,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(stonino, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(stonino,text='Department Location: Sto. Niño',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Sto Niño' ORDER BY id DESC ")
scrollbar = Scrollbar(stonino, orient = VERTICAL)
scrollbar1 = Scrollbar(stonino, orient = HORIZONTAL) 
tree=ttk.Treeview(stonino,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================tañong
tanong.configure(bg="#071E22")
Label(tanong,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(tanong, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(tanong,text='Department Location: Tañong',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Tañong' ORDER BY id DESC ")
scrollbar = Scrollbar(tanong, orient = VERTICAL)   
scrollbar1 = Scrollbar(tanong, orient = HORIZONTAL)  
tree=ttk.Treeview(tanong,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================barangka
barangka.configure(bg="#071E22")
Label(barangka,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(barangka, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(barangka,text='Department Location: Barangka',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Barangka' ORDER BY id DESC ")
scrollbar = Scrollbar(barangka, orient = VERTICAL)
scrollbar1 = Scrollbar(barangka, orient = HORIZONTAL) 
tree=ttk.Treeview(barangka,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================malanday
malanday.configure(bg="#071E22")
Label(malanday,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(malanday, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(malanday,text='Department Location: Malanday',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Malanday' ORDER BY id DESC ")
scrollbar = Scrollbar(malanday, orient = VERTICAL)
scrollbar1 = Scrollbar(malanday, orient = HORIZONTAL) 
tree=ttk.Treeview(malanday,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================Jesus Dela Peña
JDP.configure(bg="#071E22")
Label(JDP,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(JDP, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(JDP,text='Department Location: Jesus Dela Peña',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Jesus Dela Peña' ORDER BY id DESC ")
scrollbar = Scrollbar(JDP, orient = VERTICAL)
scrollbar1 = Scrollbar(JDP, orient = HORIZONTAL) 
tree=ttk.Treeview(JDP,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()
#================================================================================================Kalumpang
kalumpang.configure(bg="#071E22")
Label(kalumpang,text = "GUEST ACCOUNT",font="arial 33 bold",bg="#071E22",fg="#4dccbd").place (x=420,y=50)
backbutton = Button(kalumpang, text="BACK",height=2,width=8,bd=1,font="arial 13 bold",bg="#4dccbd",fg="#071E22",command = lambda:show_frame(frame3)).place(x=40,y=40,height=40,width=90)
Label1= Label(kalumpang,text='Department Location: Kalumpang',font="arial 20 bold",bg="#071E22",fg="#4dccbd").place (x=190,y=198)
con = mysql.connect (host="localhost", user="root", password="", database="hex")
conn = con.cursor()
conn.execute("SELECT * FROM department JOIN contact USING (id) WHERE dep_location = 'Kalumpang' ORDER BY id DESC ")
scrollbar = Scrollbar(kalumpang, orient = VERTICAL)
scrollbar1 = Scrollbar(kalumpang, orient = HORIZONTAL)  
tree=ttk.Treeview(kalumpang,columns=4,show=["headings"])
tree.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
scrollbar.configure(command=tree.yview)
scrollbar.place(relx=0.866,rely=0.305,width= 24, height = 489)
scrollbar1.configure(command=tree.xview)
scrollbar1.place(relx=0.130,rely=0.910,width= 850, height = 23)
loc_frame()


show_frame(frame1)

root.mainloop()
