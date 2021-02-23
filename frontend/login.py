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
        self.root.title=("Login_System")
        self.root.geometry("650x700")

        self.l = Frame(root, width=700, height=768, bg='light blue')
        self.l.pack()
        self.heading = Label(root, text="Welcome to Login_Page", font=('arial 40 bold'), \
                             fg='lavender', bg='black', width=21)
        self.heading.place(x=0, y=0)
#================================================Label login System===================================================================================================================================

        self.title=Label(self.root,text="Login",font=("time new roman","40","bold"))
        self.title.pack()
        self.l1=Label(self.root,text="First_Name:",relief="solid",font=("time new roman","20","bold"), fg='black', bg='lavender').place(x=10,y=140)
        self.e1=Entry(self.root)
        self.e1.place(x=200,y=140,width="280",height="35")
        self.l1 = Label(self.root, text="Last_Name:", relief="solid", font=("time new roman", "20", "bold"), fg='black', bg='lavender').place(x=10, y=220)
        self.e2 = Entry(self.root)
        self.e2.place(x=200, y=220, width="280", height="35")
        self.l2 = Label(self.root, text="Password:", relief="solid",font=("time new roman", "20", "bold"),width="10", fg='black', bg='lavender').place(x=10, y=300)
        self.e3 = Entry(self.root,show="*")
        self.e3.place(x=200, y=300, width="280", height="35")
        self.b1=Button(self.root,text="login", relief="solid",font=("time new roman","20","bold"),width="7",command=self.logpage, fg='black', bg='light green').place(x=100,y=400)
        self.b2=Button(self.root, text="Exit", relief="solid",font=("time new roman","20","bold"),width="7",command=self.exit, fg='black', bg='light green').place(x=380,y=400)
        self.b3 = Button(self.root, text="Register", relief="solid",font=("time new roman", "20", "bold"), width="10",
                         command=self.register, fg='black', bg='yellow').place(x=0, y=470, width=650)


    def exit(self):
        exit()

    def regisertUser(self):

        print("sedsaf")


    def register(self):
        window = Tk()
        window.title("Welcome to Registration_Page")
        window.geometry("700x700")

        self.l = Frame(window, width=700, height=750, bg='light blue')
        self.l.pack()
        self.heading = Label(window, text="Welcome to Registration_Page", font=('arial 35 bold'), \
                             fg='lavender', bg='black', width=24)
        self.heading.place(x=0, y=0)


#=========================================Label for Window============================================================================================================================================
        Label(window, text="First_Name:", relief="solid",textvariable='v_first_name', font=("arial", 20, "bold"), fg='black', bg='lavender').place(x=30, y=100)
        self.entry_first_name = Entry(window)
        self.entry_first_name.place(x=250, y=100,width=250, height=35)
        Label(window, text="Last_Name:", relief="solid", font=("arial", 20, "bold"), fg='black', bg='lavender').place(x=30, y=150)
        self.entry_last_name = Entry(window)
        self.entry_last_name.place(x=250, y=150, width=250, height=35)
        Label(window, text="Address:", relief="solid", font=("arial", 20, "bold"), fg='black', bg='lavender').place(x=30, y=200)
        self.entry_address = Entry(window)
        self.entry_address.place(x=250, y=200, width=250, height=35)
        Label(window, text="Contact:", relief="solid", font=("arial", 20, "bold"), fg='black', bg='lavender').place(x=30, y=250)
        self.entry_contact = Entry(window)
        self.entry_contact.place(x=250, y=250, width=250, height=35)
        Label(window, text="Email:", relief="solid", font=("arial", 20, "bold"), fg='black', bg='lavender').place(x=30, y=300)
        self.entry_email = Entry(window)
        self.entry_email.place(x=250, y=300, width=250, height=35)
        Label(window, text="Password:", relief="solid", font=("arial", 20, "bold"), fg='black', bg='lavender').place(x=30, y=350)
        self.entry_password = Entry(window)
        self.entry_password.place(x=250, y=350, width=250, height=35)
#=======================================Button==========================================================================
        b3 = Button(window, text="Register", font=("time new roman", "20", "bold"), width="10",relief="solid",
                    command =self.registration, fg='black', bg='yellow')
        b3.place(x=0, y=450, width=750)


#========================================Registration===================================================================

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
