#import all the modules
from tkinter import *

import backend
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
from tkinter import ttk
#root=Tk()
import frontend.main
4


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
         self.master.title("Update")

         self.left = Frame(master, width=700, height=768, bg='light blue')
         self.left.pack(side=LEFT)



         #self.right = Frame(master, width=666, height=768, bg='light green')
         #self.right.pack(side=RIGHT)

         self.right = Frame(master, width=666, height=768, bd=5, bg="light green", relief="solid")
         self.right.pack(side=RIGHT)

         self.rb = Frame(self.right, width=640, height=740, bd=5)
         self.rb.place(x=10, y=100)

         scroll_y = Scrollbar(self.rb, orient=VERTICAL)
         self.sales = ttk.Treeview(self.rb, height=25, columns=(
             "id", "name", "price", "stock"),
                                   yscrollcommand=scroll_y.set)
         scroll_y.pack(side=RIGHT, fill=Y)
         self.sales.heading("id", text="ID")
         self.sales.heading("name", text="Name")
         self.sales.heading("price", text="Price")
         self.sales.heading("stock", text="Stock")

         self.sales['show'] = 'headings'

         self.sales.column("id", width=150)
         self.sales.column("name", width=150)
         self.sales.column("price", width=150)
         self.sales.column("stock", width=150)
         self.sales.pack(fill=BOTH, expand=1)

         # self.rb= Frame(self.right, bg="green", bd=2, relief=RAISED)
         # self.rb.pack(side=BOTTOM)


         self.heading=Label(master,text="Update to the databse",font=('arial 40 bold'), relief="solid",\
                            fg='lavender',bg='black')
         self.heading.place(x=80,y=0)

         #label and entry for id
         self.id_le=Label(master,text="Enter ID", relief="solid",font=('arial 18 bold'))
         self.id_le.place(x=220,y=100)

         self.id_leb=Entry(master, relief="solid",font=('arial 18 bold'),width=10)
         self.id_leb.place(x=350,y=100)

         self.btn_search=Button(master,text="search",width=15,height=2,\
                                bg='orange',relief="solid",command=self.search)
         self.btn_search.place(x=270,y=150)

         #lables  for the window
         self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'),relief="solid")
         self.name_l.place(x=200,y=200)

         self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'),relief="solid")
         self.stock_l.place(x=230,y=300)

         self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold'),relief="solid")
         self.cp_l.place(x=220, y=400)


        #enteries for window

         self.name_e=Entry(master,width=25,font=('arial 18 bold'),relief="solid")
         self.name_e.place(x=150,y=250)

         self.stock_e = Entry(master, width=25, font=('arial 18 bold'),relief="solid")
         self.stock_e.place(x=150, y=350)

         self.cp_e = Entry(master, width=25, font=('arial 18 bold'),relief="solid")
         self.cp_e.place(x=150, y=450)
         self.product = Label(master, text="Search By:", relief="solid", \
                              bg='black', fg='lavender', font=('arial 18 bold'), )
         self.product.place(x=700, y=10)

         self.search_txt=StringVar()
         self.sort_by=StringVar()

         self.product = Entry(master,textvariable=self.search_txt, width=25, font=('arial 18 bold'))
         self.product.place(x=850, y=10)
         self.sort = Label(master, text="Sort By:", relief="solid", \
                              bg='black', fg='lavender', font=('arial 18 bold'), )
         self.sort.place(x=700, y=60)
         # self.sort = Entry(master, width=25, textvariable=self.sort_by, font=('arial 18 bold'))
         # self.sort.place(x=850, y=60)

         combo_sort = ttk.Combobox(master, font=('arial', 15, 'bold'), width=10, textvariable=self.sort_by,
                                   state='readonly')
         combo_sort['values'] = ("id","name","price","stock")
         combo_sort.place(x=850, y=60)

         #button to add to the database
         self.btn_add=Button(master,text='Update Database',width=25,height=2,\
                             bg='orange',relief="solid",fg='black',command=self.update)
         self.btn_add.place(x=220,y=500)
         self.btn_back = Button(master, text='Back', command=self.back, width=25, height=2, \
                               bg='orange',relief="solid", fg='black')
         self.btn_back.place(x=220, y=550)

         self.btn_search = Button(master, text='Search', width=20,command=self.search_click, height=2, relief="solid", \
                                  bg='green', fg='white')
         self.btn_search.place(x=1200, y=10)


         self.btn_sort = Button(master, text='Sort', command=self.sorting, width=20, height=2, relief="solid", \
                                  bg='green', fg='white')
         self.btn_sort.place(x=1200, y=55)
         self.btn_delete = Button(master, text='Delete',command=self.delete_click, width=30, height=2, relief="solid", \
                                  bg='orange', fg='white')
         self.btn_delete.place(x=770, y=680)

         self.btn_view = Button(master, text='View All', command=self.show, width=30, height=2, relief="solid", \
                                bg='orange', fg='white')
         self.btn_view.place(x=1100, y=680)



         #text box for the log
         #self.tbBox=Text(master,width=70,height=40)
         #self.tbBox.place(x=750,y=70)
         #self.tbBox.insert(END,"ID has reached up to:"+str(id))



    def search(self):
         mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.id_leb.get()])
         result = mycursor.fetchall()
         for r in result:
              self.n1 = r[1]  # name
              self.n2 = r[2]  # stock
              self.n3 = r[3]  # cp
         conn.commit()

          #inster into the enteries to update
         self.name_e.delete(0,END)
         self.name_e.insert(0, str(self.n1))

         self.stock_e.delete(0, END)
         self.stock_e.insert(0, str(self.n2))

         self.cp_e.delete(0, END)
         self.cp_e.insert(0, str(self.n3))

    def update(self):
          self.u1=self.name_e.get()
          self.u2 = self.stock_e.get()
          self.u3 = self.cp_e.get()


          mycursor.execute("UPDATE  inventory SET name=%s,stock=%s,price=%s WHERE id=%s",[self.u1,self.u2,self.u3,self.id_leb.get()])
          conn.commit()
          #tkinter.messagebox.showinfo("Success","Update successfully")

    def back(self):
        self.master.destroy()
        self.b = Tk()
        frontend.main.Application(self.b)
#=======================================================================================================================

    def show(self):
        query="select * from inventory"
        db=backend.dbconnection.DbConnection()
        rows=db.view(query)
        if len(rows)!=0:
            self.sales.delete(*self.sales.get_children())
            for row in rows:
                self.sales.insert("", END, values=row)

#=======================================================================================================================
    def delete_click(self):
        # id = self.__id.get()
        # name = self.name.get()
        # price = self.price.get()
        # stock = self.stock.get()

        # u=backend.UserModel(id,name,price,stock)
        if id=='':
            tkinter.messagebox.showerror(" Inventory Management System", "Please fill all empty box")
        else:

            query=("delete from inventory where id="+self.id_leb.get())
            db=backend.dbconnection.DbConnection()
            r=backend.dbconnection.DbConnection()
            r.delete(query)
            tkinter.messagebox.showinfo("Successful", "1 row data deleted successfully")
            self.show()

#======================================Searching========================================================================
    def mergesort(self, alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            self.mergesort(lefthalf)
            self.mergesort(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist

    def binary_primary(self, list, item):
        if list == []:
            return ValueError
        self.list = list
        self.item = item
        max = len(list) - 1
        min = 0
        while min <= max:
            mid = (min + max) // 2
            if self.list[mid] == self.item:
                return mid
            elif self.list[mid] > self.item:
                max = mid - 1
            else:
                min = mid + 1
        return -1


    def search_click(self):
        db = backend.dbconnection.DbConnection()
        query = "select * from inventory"
        rows = db.search(query)
        myStack = []
        for row in rows:
            myStack.append(row[0])
        self.sorted = self.mergesort(myStack)
        item = int(self.search_txt.get())
        sorted = self.sorted
        index = self.binary_primary(sorted, item)
        for row in rows:
            if sorted[index] == row[0]:
                self.sales.delete(*self.sales.get_children())
                self.sales.insert('', END, value=row)
#===================================Sorting=============================================================================

    def sorting(self):
        db = backend.dbconnection.DbConnection()
        query = "select * from inventory"
        rows = db.search(query)
        myStack = []
        if len(rows) != 0:
            self.sales.delete(*self.sales.get_children())
            if self.sort_by.get() == "id":
                for row in rows:
                    myStack.append(row[0])
                self.sorted = self.mergesort(myStack)
                # print(self.sorted)
                # print(rows)
                for i in self.sorted:
                    for row in rows:
                        if i == row[0]:
                            self.sales.insert('', END, value=row)
            elif self.sort_by.get() == "name":
                for row in rows:
                    myStack.append(row[1])
                self.sorted = self.mergesort(myStack)
                # print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[1]:
                            self.sales.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by.get() == "price":
                for row in rows:
                    myStack.append(row[2])
                self.sorted = self.mergesort(myStack)
                # print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[2]:
                            self.sales.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by.get() == "stock":
                for row in rows:
                    myStack.append(row[3])
                self.sorted = self.mergesort(myStack)
                # print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[3]:
                            self.sales.insert('', END, value=row)
                            rows.remove(row)
#root=Tk()
#b=Database(root)
#root.mainloop()


