import tkinter
from tkinter import*
from tkinter import messagebox
import backend.UserModel
import backend.dbconnection
import frontend.main


import mysql.connector
from mysql.connector import Error

class Login_System:
    def __init__(self,root):
        self.root=root
        root.title("Welcome to Login_Page")
        self.root.title=("Login_System")
        self.root.geometry("700x750")

        self.title=Label(self.root,text="Login",font=("time new roman","40","bold"))
        self.title.pack()
        self.l1=Label(self.root,text="First_Name:",font=("time new roman","20","bold"), fg='black', bg='lavender').place(x=140,y=140)
        self.e1=Entry(self.root)
        self.e1.place(x=400,y=140,width="250",height="35")
        self.l1 = Label(self.root, text="Last_Name:", font=("time new roman", "20", "bold"), fg='black', bg='lavender').place(x=140, y=220)
        self.e2 = Entry(self.root)
        self.e2.place(x=400, y=220, width="250", height="35")
        self.l2 = Label(self.root, text="Password:", font=("time new roman", "20", "bold"),width="10", fg='black', bg='lavender').place(x=130, y=300)
        self.e3 = Entry(self.root,show="*")
        self.e3.place(x=400, y=300, width="250", height="35")
        self.b1=Button(self.root,text="login",font=("time new roman","20","bold"),width="5",command=self.logpage, fg='black', bg='light green').place(x=220,y=400)
        self.b2=Button(self.root, text="Exit",font=("time new roman","20","bold"),width="5",command=self.exit, fg='black', bg='light green').place(x=510,y=400)
        self.b3 = Button(self.root, text="Register", font=("time new roman", "20", "bold"), width="10",
                         command=self.register, fg='black', bg='yellow').place(x=320, y=470)


    def exit(self):
        exit()

    def regisertUser(self):

        print("sedsaf")


    def register(self):
        window = Tk()
        window.title("Welcome to Registration_Page")
        window.geometry("500x600")
        l1 = Label(window, text="User Register", font=("time new roman", "25", "bold"))
        l1.pack()
        Label(window, text="First_Name:", relief="solid",textvariable='v_first_name', font=("arial", 12, "bold")).place(x=30, y=100)
        self.entry_first_name = Entry(window)
        self.entry_first_name.place(x=200, y=100)
        Label(window, text="Last_Name:", relief="solid", font=("arial", 12, "bold")).place(x=30, y=130)
        self.entry_last_name = Entry(window)
        self.entry_last_name.place(x=200, y=130)
        Label(window, text="Address:", relief="solid", font=("arial", 12, "bold")).place(x=30, y=160)
        self.entry_address = Entry(window)
        self.entry_address.place(x=200, y=160)
        Label(window, text="Contact:", relief="solid", font=("arial", 12, "bold")).place(x=30, y=190)
        self.entry_contact = Entry(window)
        self.entry_contact.place(x=200, y=190)
        Label(window, text="Email:", relief="solid", font=("arial", 12, "bold")).place(x=30, y=220)
        self.entry_email = Entry(window)
        self.entry_email.place(x=200, y=220)
        Label(window, text="Password:", relief="solid", font=("arial", 12, "bold")).place(x=30, y=250)
        self.entry_password = Entry(window)
        self.entry_password.place(x=200, y=250)

        b3 = Button(window, text="Register", font=("time new roman", "20", "bold"), width="10",
                    command =self.registration)
        b3.place(x=150, y=300)




    def registration(self):
        f_name=self.entry_first_name.get()
        lastname=self.entry_last_name.get()
        address=self.entry_address.get()
        contact=self.entry_contact.get()
        email=self.entry_email.get()
        password=self.entry_email.get()

        if f_name=='' or lastname=='' or address=='' or contact=='' or email=='' or password=='':
            messagebox.showerror('error', 'Please enter all the information')
        else:
            query='insert into registration(First_Name,Last_Name,Address,Contact,Email,Password) values(%s,%s,%s,%s,%s,%s)'
            a=backend.UserModel.UserModel(f_name,lastname,address,contact,email,password)
            values=a.getf_name(),a.getlastname(),a.getaddress(),a.getcontact(),a.getemail(),a.getpassword()
            print(values)
            b=backend.dbconnection.DbConnection().registration(query,values)
            print(b)


    def logpage(self):
        f_name = self.e1.get()
        lastname = self.e2.get()
        password = self.e3.get()
        if f_name=='' or lastname=='' or password=='':
            messagebox.showerror('error', 'Please enter all the information')
        else:
            a=backend.UserModel.UserModel()
            a.setf_name(f_name)
            a.setlastname(lastname)
            a.setpassword(password)
            query='select * from registration where First_Name=%s and Last_Name=%s and Password=%s '
            values=a.getf_name(), a.getlastname(), a.getpassword()
            b=backend.dbconnection.DbConnection()


            rows=b.login(query,values)
            c=[]
            if len(rows)!=0:
                for row in rows:
                    c.append(row[0])
                    c.append(row[1])

                    c.append(row[5])
                    if f_name==c[0] and lastname==c[1] and password==c[2]:
                        messagebox.showinfo('Successful', 'You Have Login')
                        self.root.destroy()
                        self.a=Tk()
                        frontend.main.Application(self.a)

                    else:
                        messagebox.showerror('Error', 'Unsuccessful')

root=Tk()
obj=Login_System(root)
root.mainloop()
