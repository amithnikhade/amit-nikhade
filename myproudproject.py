from tkinter import *
import sqlite3
from PIL import Image, ImageTk, ImageEnhance
from tkinter import messagebox


top = Tk()
top.title("amit's messenger")

Username=StringVar()

Password=IntVar()



username=StringVar()
password=IntVar()

# confirmpassword=StringVar()
Email=StringVar()



def new_window():
    root=Tk()
    root.geometry('500x500')
    root.title("Registration")

   
    label_1 = Label(root, text="username",width=20,font=("bold", 12))
    label_1.place(x=80,y=150)

    entry_1 = Entry(root,textvar=username)
    entry_1.place(x=240,y=150)

    label_2 = Label(root, text="password",width=20,font=("bold", 12))
    label_2.place(x=80,y=200)

    entry_2 = Entry(root,textvar=password)
    entry_2.place(x=240,y=200)

    label_3 = Label(root, text="email",width=20,font=("bold", 12))
    label_3.place(x=80,y=250)

    entry_2 = Entry(root,textvar=Email)
    entry_2.place(x=240,y=255)

    Button(root, text='Submit',width=20,bg='#1C86EE',fg='white',command=database1,border="0").place(x=180,y=350)
    # button.pack()
    label_1 = Label(root, text="SignUp",width=20,font=("bold", 20),fg="white", bg="#00C957")
    label_1.place(x=97,y=400)



def database1():
   u=username.get()
   p=password.get()
   e=Email.get()

   
   conn = sqlite3.connect('iii.db')
   with conn:
      c=conn.cursor()
   c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT,password TEXT,Email TEXT)')
   c.execute('INSERT INTO users (username,password,Email) VALUES(?,?,?)',(u,p,e,))
#     c.close()
   conn.commit()
   conn.close

def database():
   Username1=Username.get()
   Password1=Password.get()
   
   conn = sqlite3.connect('signin.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Username TEXT,Password TEXT)')
   cursor.execute('insert into Student (Username,Password) VALUES(?,?)',(Username1,Password1,))
#    cursor.close()
   conn.commit()
   conn.close()


C = Canvas(top, bg="white", height=5500, width=8000)
filename = PhotoImage(file = "E:\p.png")
filename=filename.subsample(6,4)

filename2 = PhotoImage(file= "E:\yt.png")

# def newcommand():
#     filemenu.add_command(label="Quit", command=exit)

    
filemenu = Menu(top,bg='blue')
filemenu.add_command(label="Quit")
top.config( background='red',menu=filemenu)
submenu= Menu(filemenu)
filemenu.add_cascade(label="file", menu=submenu)

background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Entry2=Entry(top, textvar=Password)
Entry2.place(x=530, y=500,relheight=0.02,relwidth=0.2 )
Entry2.config(font='bold'*5)

# Entry2=Entry(top, text="search")
# Entry2.place(x=530, y=600,relheight=0.02,relwidth=0.2 )
# Entry.config(font='bold'*5)

E1 = Entry(top, textvar=Username)
E1.place(x=530, y=450,relheight=0.02,relwidth=0.2 )
E1.config(font='bold'*5)
#E1.pack()

button1=Button(top, text= "Login", background="#1C86EE", fg="white",command=database)
button1.place(x=530, y=550,relheight=0.04,relwidth=0.2)
button1.config(state="normal", relief="raised", borderwidth=0)

label1= Label(top, text="Crafted By : Amit Nikhade", fg="grey", bg="black")
label1.place(x=593, y=605)

label2= Label(top, text="Password:", fg="grey", bg="White")
label2.place(x=400, y=500,relheight=0.02,relwidth=0.1)

label3= Label(top, text="Username:", fg="grey", bg="White")
label3.place(x=400, y=450,relheight=0.02,relwidth=0.1)

# label3= Label(top, text="Password:", fg="grey", bg="White")
# label3.place(x=400, y=450,relheight=0.02,relwidth=0.1)

button1=Button(top, text= "SignUp", bg="#1C86EE", fg= 'white', command=new_window)
button1.place(x=593, y=700,relheight=0.03,relwidth=0.1)
button1.config(state="normal", relief="raised", borderwidth=0)

# def access():

#     connection = sqlite3.connect("signup.db")

# cursor = connection.cursor()

# cursor.execute("SELECT * FROM username") 
# print("fetchall:")
# result = cursor.fetchall() 
# for r in result:
#     print(r)
# cursor.execute("SELECT * FROM username") 
# print("\nfetch one:")
# res = cursor.fetchone() 
# print(res)


   

#buttonAdministrator=Button(top, text= "administrator",bg= )



C.pack()
top.mainloop()