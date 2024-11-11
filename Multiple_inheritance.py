class student:

    def __init__(self,Name,age,branch):
        self.Name=Name
        self.age=age
        self.branch=branch
    
    def display_details(self):
        return f"Name: {self.Name}\nAge: {self.age}\nBranch: {self.branch}"
    

class Father_details:
    def __init__(self, Father_Name):
        self.Father_Name = Father_Name
    
    def display_details(self):
        return f"Father's Name: {self.Father_Name}"
    



class Marks(student, Father_details):
    def __init__(self, Name, age, branch, Father_Name, cgpa):
        # Initialize both parent classes
        super().__init__(Name, age, branch)  # Calls __init__ of the student class
        Father_details.__init__(self, Father_Name)  # Calls __init__ of the Father_details class
        self.cgpa = cgpa
    


    def display_details(self):
        # Get details from both parent classes
        parent_details = super(student, self).display_details()  # Calls display_details of student
        father_details = Father_details.display_details(self)  # Calls display_details of Father_details
        return f"{parent_details}\n{father_details}\nGrade: {self.cgpa}"



# Create an instance of Marks class
grade = Marks("Vasanthk", 23, "ML engineer", "Ramana", 7.6)

# Print the details
print(grade.display_details())



#Key Points:
#Simpler and more intuitive: Since you have only one parent class, the behavior is more predictable.
#Method Resolution Order (MRO): In single inheritance, the MRO is straightforward: the child class calls methods from the parent class (using super()).
#No ambiguity: There is no ambiguity in which class method to call because there's only one parent.





I#n this case, super() will resolve to Parent1's display()
#method because Parent1 comes before Parent2 in the MRO. If you want to call Parent2's method, you can do so explicitly: Parent2.display(self).