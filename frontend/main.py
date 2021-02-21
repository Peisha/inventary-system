#import all the modules
from tkinter import *
from tkinter import messagebox
import frontend.add_to_db
import frontend.update

import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import datetime
import math

date=datetime.datetime.now().date()
#temporary list like sessions
products_list=[]
product_price=[]
product_quantity=[]
product_id=[]
r = []

class Application():
    def __init__(self,master):
        self.master=master
        self.master.geometry("1366x768+0+0")
        self.master.title("Inventory_Management_System")

        self.left=Frame(master,width=700,height=768,bg='light blue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg='light green')
        self.right.pack(side=RIGHT)


        #components
        self.heading=Label(self.left,text="NORIN_STORE", width=22,font=('arial 40 bold'), \
                           fg='black',bg='lavender', relief="solid")
        self.heading.place(x=0,y=0)

        self.date_l=Label(self.right,text="Today's Date: "+str(date),font=('arial 16 bold'), \
                          bg='lavender',fg='black',relief="solid")
        self.date_l.place(x=0,y=0)

        #table invoice=======================================================
        self.tproduct=Label(self.right,text="Number Of Products",font=('arial 18 bold'), \
                            bg='lavender',fg='black', relief="solid")
        self.tproduct.place(x=0,y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), \
                               bg='lavender', fg='black', relief="solid")
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'),\
                             bg='lavender', fg='black', relief="solid")
        self.tamount.place(x=500, y=60)

        #enter stuff
        self.enterid=Label(self.left,text="Product's ID No.",font=('arial 18 bold'),\
                           fg='black',bg='lavender', relief="solid")
        self.enterid.place(x=0,y=80)


        self.enteride=Entry(self.left,width=25,font=('arial 18 bold'),bg='lightblue', relief="solid")
        self.enteride.place(x=220,y=80)
        self.enteride.focus()



        #button
        self.search_btn=Button(self.left,text="Search",width=22,height=2,bg='green',relief="solid", command=self.ajax)
        self.search_btn.place(x=290,y=120)
        #fill it later by the fuction ajax

        self.productname=Label(self.left,text="",font=('arial 27 bold'),relief="solid", \
                               bg='lavender',fg='black')
        self.productname.place(x=0,y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'),relief="solid", \
                            bg='lavender', fg='black')
        self.pprice.place(x=0, y=290)

        #total label
        self.total_l=Label(self.right,text="",font=('arial 40 bold'), relief="solid",\
                           bg='lavender',fg='black')
        self.total_l.place(x=0,y=600)
    def ajax(self):
        self.conn = mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='1234')
        self.get_id=self.enteride.get()
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("SELECT * FROM inventory WHERE id= %s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        if self.pc:
          for self.r in self.pc:
            #self.get_id=self.r[0]
            self.get_name=self.r[1]
            self.get_price=self.r[3]
            self.get_stock=self.r[2]
          self.productname.configure(text="Product's_Name: " +str(self.get_name),fg='black',bg='lavender',relief="solid")
          self.pprice.configure(text="Price:RS. "+str(self.get_price),fg='black',bg='lavender',relief="solid")


        #craete the quantity and the discount label
          self.quantityl=Label(self.left,text="Enter_Quantity",font=('arial 18 bold'),\
                               fg='black',bg='lavender',relief="solid")
          self.quantityl.place(x=0,y=370)

          self.quantity_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='lavender',relief="solid")
          self.quantity_e.place(x=190,y=370)
          self.quantity_e.focus()

        #discount
          self.discount_l = Label(self.left, text="Enter_Discount", font=('arial 18 bold'),relief="solid",\
                                  fg='black',bg='lavender')
          self.discount_l.place(x=0, y=410)


          self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'),relief="solid", \
                                  bg='lavender')
          self.discount_e.place(x=190, y=410)
          self.discount_e.insert(END,0)


        #add to cart button
          self.add_to_cart_btn = Button(self.left, text="Add_To_Cart", width=22, height=2, bg='green',relief="solid",command=self.add_to_cart)
          self.add_to_cart_btn.place(x=270, y=450)

        #genrate bill and change
          self.change_l=Label(self.left,text="Given Amount",font=('arial 18 bold'),fg='black',bg='lavender',relief="solid")
          self.change_l.place(x=0,y=550)

          self.change_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='lavender',relief="solid")
          self.change_e.place(x=190,y=550)

          self.change_btn= Button(self.left, text="Calculate Change", width=22, height=2, bg='green',relief="solid",command=self.change_func)
          self.change_btn.place(x=270, y=590)

        #geneerate bill button
          self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='orange',fg='white',relief="solid",command=self.generate_bill)
          self.bill_btn.place(x=0, y=640)
        else:
             messagebox.showinfo("success", "Done everything smoothly")
        #generate add and update buttom
        self.bill_btn = Button(self.left, text="Add The Product", width=20, height=2, bg='lavender', fg='black',relief="solid",command=self.add_product)

        self.bill_btn.place(x=100, y=700)
        self.bill_btn = Button(self.left, text="Update", width=20, height=2, bg='lavender', fg='black', relief="solid",command=self.update_product)

        self.bill_btn.place(x=400, y=700)



    def add_to_cart(self,*args,**kwargs):
        self.quantity_value=int(self.quantity_e.get())

        if  self .quantity_value >int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Not that any products in our stock.")
        else:
            #calculate the price first
            self.final_price=(float(self.quantity_value) * float(self.get_price))-(float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in products_list:
                self.tempname=Label(self.right,text=str(products_list[self.counter]),font=('arial 18 bold'),relief="solid",\
                                    bg='lavender',fg='black')
                self.tempname.place(x=0,y=self.y_index)
                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), relief="solid",\
                                    bg='lavender', fg='black')
                self.tempqt.place(x=300, y=self.y_index)
                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), relief="solid",\
                                       bg='lavender', fg='black')
                self.tempprice.place(x=500, y=self.y_index)

                self.y_index+=40
                self.counter+=1


                #total confugure
                self.total_l.configure(text="Total : Rs. "+str(sum(product_price)),\
                                       bg='lavender',fg='black')
                #delete
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()
                #autofocus to the enter id
                self.enteride.focus()
                self.quantityl.focus()
                self.enteride.delete(0,END)

    def change_func(self):
        self.amount_given=float(self.change_e.get())
        self.our_total=float(sum(product_price))

        self.to_give=self.amount_given-self.our_total

        #label change
        self.c_amount=Label(self.left,text="Change: Rs. "+str(self.to_give),font=('arial 18 bold'), relief="solid",\
                            fg='orange',bg='black')
        self.c_amount.place(x=0 ,y=600)

    def generate_bill(self):
        self.mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        for r in self.pc:
            self.old_stock=r[2]
        for i in products_list:
            for r in self.pc:
                self.old_stock = r[2]
            self.new_stock=int(self.old_stock) - int(self.quantity_value)
            #updating the stock
            self.mycursor.execute("UPDATE inventory SET stock=%s WHERE id=%s",[self.new_stock,self.get_id])
            self.conn.commit()

            #inster into transcation
            self.mycursor.execute("INSERT INTO transaction (product_name,quantity,amount,date) VALUES(%s,%s,%s,%s)",[self.get_name,self.quantity_value,self.get_price,date])
            self.conn.commit()
            print("Decreased")

        tkinter.messagebox.showinfo("success","Done everything smoothly")
    def add_product(self):
        self.master.destroy()
        self.a = Tk()
        frontend.add_to_db.Database(self.a)
    def update_product(self):
        self.master.destroy()
        self.b = Tk()
        frontend.update.Database(self.b)









