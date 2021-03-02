import unittest
import backend.dbconnection
import frontend.update
import Model.searching
import Model.sorting


class Test_Database(unittest.TestCase):
    def setUp(self):
        '''
        This method is used for setting up the testing
        '''
        self.db=backend.dbconnection.DbConnection()
        self.b=Model.searching.searchBox()
        self.c=Model.sorting.Sort()

    def test_fetch(self):
        '''
        It test the fetch value of database
        '''
        query = "select * from inventory"
        row = self.db.fetch1(query)
        self.assertEqual((1, 'soap', '30', '46'),
                         row)

    def test_searching(self):
        '''
        It will test searching.
        '''
        query = "select * from  inventory"
        a = self.db.view(query)
        b = self.b.linear_search('dbdrqwcd', a)
        self.assertEqual(2, b)

    def test_sorting(self):
        '''
        It test the sorting of database fetch value in alphabetic order
        '''
        query = "select * from  inventory"
        a = (self.db.view(query))
        b = self.c.sort_tuple(a)
        self.assertEqual(
            [(5, 'dbdrqwcd', '255', '535'), (8, 'gghy', '567', '56'), (11, 'ggii', '567', '56'),
             (12, 'ggtftc', '567', '56'), (10, 'ggyy', '567', '56')],b)

    def test_add(self):
        '''
        It tests the add method of database
        '''
        query = 'insert into  inventory values(2,"soap", "46", "30")'
        i = self.db.registration(query)
        self.assertIsNot(False, i)

    def test_update(self):
        '''
        It tests the update function of database
        '''
        query = "update inventory set name=%s where id=%s"
        value = ("Shyam1", 1212)
        u = self.db.update(query, value)
        query2 = "select * from inventory where name=%s"
        value2 = ("Shyam1",)
        u = self.db.select(query2, value2)
        self.assertIsNotNone(u)

    def test_del(self):
        '''
        It tests the delete value of database
        :return: it checks whether the values got deleted or not
        '''
        query = "delete from inventory where name=%s"
        values = ("Shyam1",)
        b = self.db.delete(query, values)
        if b:
            print("Success")
        else:
            return False
        self.assertEqual(True, b)





