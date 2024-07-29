class person:
    def __init__(self,fname,lname):
        self.first = fname
        self.last = lname

    def printname(self):
        print(self.first, self.last)

class student(person):
    def __init__(self,fname,lname,year):
        self.year = year
        person.__init__(self,fname,lname)

    def pname(self):
        print(self.first, self.last, self.year)


Me = student("Jay","Jaria",2001)
Me.printname()
Me.pname()