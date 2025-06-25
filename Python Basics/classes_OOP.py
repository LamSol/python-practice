# Learning about Classes
# Constructors
# Lets start with constructor

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

Book1 = Book("Atomic Habits","James Clear", 2018)
print(Book1.title, "By -" , Book1.author,)

# Another Example
class Bank_Ac:
    def __init__(self,balance):
        if balance < 0:
            self.balance = 0
        else:
            self.balance = balance

acc = Bank_Ac(100)
print(acc.balance)

# Inheritance
class vehicle:
    def wheel(self):
        print("Wheels spin")
class car(vehicle):
    def rims(self):
        print("Rims are cool")

c = car()
c.wheel()
c.rims()


# Difference between Function and Method
# Function: Doesn’t belong to a class; defined with def outside any class.
# Method: Defined inside a class; always has self as the first parameter (for instance methods).
# In Simple Terms:
# Term	        Belongs To	                Called On	        First Parameter
# Function	    Independent block of code	Called directly	    None required
# Method	    Belongs to a class/object	Called on object	self (usually)