import csv

class Book:
    def __init__(self,id,name,author,year,genre,count):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.count = count

    def AddBook(self):
        with open('bookData.csv','a',newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow([self.id,self.name,self.author,self.year,self.genre,self.count])

    def IssueBook(self):
        pass

class Member:
    def __init__(self,id,name,books,status):
        self.id = id
        self.name = name
        self.books = books
        self.status = status

    def AddMember(self):
        with open('memberData.csv','a',newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow([self.id,self.name,self.books,self.status])

    def UpdateMemberShipStatus(self):
        pass


class Library(Book,Member):
    def __init__(BookList,MemberList,IssueList):
        self.BookList = BookList
        self.MemberList = MemberList
        self.IssueList = IssueList

ds = Book(1,"ds","robin",2019,"cs",5)
db = Book(2,"db","robin",2014,"cs",2)
ee = Book(3,"ee","robin",2017,"ee",3)

ds.AddBook()
db.AddBook()
ee.AddBook()

ratz = Member(1,"Ratnankur","","y")
munz = Member(2,"Munish","","y")
paaji = Member(3,"Rajvinder","","y")

ratz.AddMember()
munz.AddMember()
paaji.AddMember()
