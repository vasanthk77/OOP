

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

## using self keyword  we can make connection between the attributes in class and object for accessing that instances



## object creation

student_details=student("Vasanth",23,"Data Sciecne")

print(student_details.Name)
print(student_details.age)
print(student_details.branch)

print(student_details.display_details())

