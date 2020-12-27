class Employees: 
       
    def __init__(self, name, age): 
        self.name = name 
        self.age=age
       
    
    def printName(self): 
        return f' The person : {self.name}, has: {self.age} ages, and his position is: '  
   
 
class Worker(Employees): 
    def position(self): 
        return "radnik"

class Menager(Employees): 
    def position(self): 
        return "menadzer"
   

emp = Menager("Geek1",24)   
print(emp.printName(), emp.position()) 
   
emp = Worker("Geek2",23)  
print(emp.printName(), emp.position()) 
