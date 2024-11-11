

# class  creation

class student:
    ## intilizatio of parameters using init method like constrctor
    def __init__(self,Name,age,branch):
        self.Name=Name
        self.age=age
        self.branch=branch
    
    ## own user defined functions in class
    def display_details(self):
        return f"{self.Name}  {self.branch}"
    
student_details=student("Vasanth",23,"Data Sciecne")

## inheritance is something inheriting something from parent class and child class\

class Marks(student):
    def __init__(self,Name,age,branch,cgpa):
        super().__init__(Name,age,branch)  ## using super keyword we can inherit directly form parent class
        self.cgpa=cgpa
    
    def all_details(self):
        return f"{self.Name} {self.age} {self.branch} {self.cgpa}"

grade=Marks("Vasanthk",23,"ML engineer",7.6)

print()





#print(student_details.display_details())

