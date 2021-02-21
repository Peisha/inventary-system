class searchBox:
    def linear_search(self,si,source):
        '''
        It will search the value from the database
        :param si: it will receive search item name
        :param source: it will receive tuple data from database
        :return: it returns tuple index number
        '''
        for i in source:
            if si in i:
                return int(source.index(i))
        return False