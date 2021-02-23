#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import frontend.main
from tkinter import ttk

conn=mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='1234')
mycursor = conn.cursor()
mycursor.execute("SELECT Max(id) from inventory")
result = mycursor.fetchall()
for r in result:
    id=r[0]

class Database:
    def __init__(self,master):
         self.master=master
         self.master.geometry("1366x768+0+0")
         self.master.title("Add The Product")
         self.left = Frame(master, width=700, height=768, bg='light blue',relief="solid")
         self.left.pack(side=LEFT)

         self.right = Frame(master, width=666, height=768, bg='light green')
         self.right.pack(side=RIGHT)
         self.heading = Label(master, text="Add the product", font=('arial 40 bold'), \
                              fg='Lavender', bg='black')
         self.heading.place(x=210, y=0)

         self.heading=Label(master,text="Add the product",font=('arial 40 bold'), relief="solid",\
                            fg='Lavender', bg='black')
         self.heading.place(x=210,y=0)


#===========================================lables  for the window======================================================
         self.name_l=Label(master,text="Enter Product Name", \
                           bg='black', fg='lavender',relief="solid",font=('arial 18 bold'),)
         self.name_l.place(x=290,y=90)

         self.stock_l=Label(master,text="Enter Stocks", \
                            bg='black', fg='lavender',relief="solid", font=('arial 18 bold'))
         self.stock_l.place(x=320,y=200)

         self.cp_l = Label(master, text="Enter Cost Price ", \
                           bg='black', fg='lavender',relief="solid", font=('arial 18 bold'))
         self.cp_l.place(x=300, y=300)


#===============================================enteries for window=====================================================

         self.name_e=Entry(master,width=25,relief="solid",font=('arial 18 bold'))
         self.name_e.place(x=250,y=150)

         self.stock_e = Entry(master, width=25, relief="solid",font=('arial 18 bold'))
         self.stock_e.place(x=250, y=250)

         self.cp_e = Entry(master, width=25,relief="solid", font=('arial 18 bold'))
         self.cp_e.place(x=250, y=350)

#===================================button to add to the database=======================================================
         self.btn_add=Button(master,text='Add to Database',width=25,height=2, relief="solid",\
                             bg='orange',fg='white',command=self.get_items)
         self.btn_add.place(x=400,y=450)

         self.btn_clear=Button(master,text="Clear All Fields",width=18,height=2, relief="solid",\
                               bg='orange',fg='white',command=self.clear_all)
         self.btn_clear.place(x=250,y=450)

         self.btn_back = Button(master, text="Back", width=18, height=2, command=self.back, relief="solid", \
                                 bg='green', fg='white')
         self.btn_back.place(x=350, y=500)

          #text box for the log
         self.tbBox = Text(master, width=60, height=18)
         self.tbBox.place(x=750, y=70)
         self.tbBox.insert(END, "ID has reached up to:" + str(id))

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)



    def get_items(self):
    # get from entries
       self.name = self.name_e.get()
       self.stock = self.stock_e.get()
       self.cp = self.cp_e.get()

    # dynamic entries
       if self.name == '' or self.stock == '' or self.cp == '':
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
       else:
        mycursor.execute("INSERT INTO inventory (name, stock, price) VALUES(%s,%s,%s)",[self.name,self.stock,self.cp])
        conn.commit()
        #textbox insert
        self.tbBox.insert(END, "\n\nAdded " + str(self.name) + " product with the quantity of " + str(self.stock))
        tkinter.messagebox.showinfo("Success", "Successfully added")

    def clear_all(self):
       num = id + 1
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.cp_e.delete(0, END)

    def back(self):
        self.master.destroy()
        self.b = Tk()
        frontend.main.Application(self.b)

#root=Tk()
#obj=Database(root)
#root.mainloop()




