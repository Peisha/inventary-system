import backend.dbconnection

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