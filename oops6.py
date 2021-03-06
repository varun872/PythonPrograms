# Single Inheritance
class Employee:

    no_of_leaves=9

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    @classmethod
    def change_leaves(cls,newleaves): #cls here is the class(Employee)
        cls.no_of_leaves=newleaves #uses the class to change the no of leaves

    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printfunc():
        return "This is a static method function"

class Programmer(Employee):
    def __init__(self,name,salary,role,languages):
        
    def printprog(self):
        return f"The Programmer's Name is {self.name}, his Salary is {self.salary} and his Role is {self.role}"

harry=Employee("Harry",450,"Manager")
larry=Employee("Larry",440,"Manager")
varun=Programmer("Varun",700,"Programmer")
raju=Programmer("Raju",750,"Programmer")
print(raju.printprog())
