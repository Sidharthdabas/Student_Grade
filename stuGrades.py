class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def total(self):
        return sum(self.marks)
    
    def average(self):
        return self.total()/len(self.marks)
     
    def display_result(self):
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.total()}")
        print(f"Average marks:{self.average()}")

student1=student("Aditya",[56,78,95])
student1.display_result()
print(student1.total())
print(student1.average())


        

    
    
    

    