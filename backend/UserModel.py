class UserModel :

    def __init__(self,f_name=None,lastname=None,address=None,contact=None,email=None,password=None,id=None, name=None, price=None, stock=None):
        self.__f_name=f_name
        self.__lastname=lastname
        self.__address=address
        self.__contact=contact
        self.__email=email
        self.__password=password
        self.__id=id
        self.__name = name
        self.__price = price
        self.__stock=stock

    def setid(self,id):
        self.__id=id
    def getid(self):
        return self.__id
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def setstock(self,stock):
        self.__stock=stock
    def getstock(self):
        return self.__stock


    def setf_name(self,f_name):
        self.__f_name=f_name
    def getf_name(self):
        return self.__f_name
    def setlastname(self,lastname):
        self.__lastname=lastname
    def getlastname(self):
        return self.__lastname
    def setaddress(self,address):
        self.__address=address
    def getaddress(self):
        return self.__address
    def setcontact(self,contact):
        self.__contact=contact
    def getcontact(self):
        return self.__contact
    def setemail(self,email):
        self.__email=email

    def getemail(self):
        return self.__email
    def setpassword(self,password):
        self.__password=password
    def getpassword(self):
        return self.__password




