

# class  creation

class student:
    ## intilizatio of parameters using init method like constrctor
    def __init__(self,Name,age,branch):
        self.Name=Name
        self.age=age
        self.branch=branch
    
    ## own user defined functions in class
    def display_details(self):
        return f"Name: {self.Name}\nAge: {self.age}\nBranch: {self.branch}"
    
student_details=student("Vasanth",23,"Data Sciecne")


## inheritance is something inheriting something from parent class and child class\
## single inheritance



class Marks(student):
    def __init__(self,Name,age,branch,cgpa):
         #use in single ihheritance to avoid error in multi #super().__init__(Name,age,branch,Father_Name)  ## using super keyword we can inherit directly form parent class
        super().__init__(Name,age,branch)
        self.cgpa=cgpa
    
   # def display_details(self):
    #   return f"Name: {self.Name}\nAge: {self.age}\nBranch: {self.branch}\nGrade: {self.cgpa}"



## Polymorphism  - Overriding display_details in child class

    def display_details(self):
       parent_details = super().display_details()
       return f"{parent_details}\nGrade: {self.cgpa}"



grade=Marks("Vasanthk",23,"ML engineer",7.6)

print(student_details.display_details())
print(grade.display_details())






#father_details = Father_details.display_details(self)
#F#ather_details.display_details(self):
#his explicitly calls the display_details() method of the Father_details class.
#Since we are working with multiple inheritance, super() would only call the next class in MRO, and if we want to directly invoke a method from a specific parent class (in this case, Father_details), we call it explicitly as Father_details.display_details(self).
#Here, we are calling the display_details() method in the Father_details class to get the father's name.
#Why Not Use super() for Both?
#In the case of the Marks class inheriting from both student and Father_details, super() would follow the MRO (method resolution order) to determine which method to call next.

#When you use super(student, self), you are explicitly telling Python to call the next class in the method resolution order after student, which is Father_details. But since both student and Father_details are parent classes of Marks, it’s better to directly call the display_details() method of Father_details to avoid any confusion
