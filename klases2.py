# import math
# class Student:
#     def __init__(self, name, grade):
#         self.grade = grade
#         self.name = name


#     def info(self):
#         print(f"Name: {self.name}, Grade: {self.grade}")

#     def avarage_grade(self, grade2):
#        A = (self.grade + grade2) / 2
#        print(f"Vidējā atzīm ir: {A}")
# Student1 = Student("Jānis", 8)
# Student1.info()
# Student1.avarage_grade(7)

class Student:
    
    def __init__(self, vards, atzimes):
        self.vards = vards
        self.atzimes = atzimes

    def max_grade(self):
        return max(self.atzimes)
        
    
    def calculate_avarage(self):
        return sum(self.atzimes) / len(self.atzimes)
    
    def izcils(self):
        min_avg = 4
        if self.calculate_avarage() >= min_avg:
            print(f"{self.vards} ir izcils skolēns")
        else:
            print(f"{self.vards} nav izcils skolēns")
        


student1 = Student("Anna", [3,4,6,8])
print(f"Augstākā atzīme ir {student1.max_grade()}")
print(f"Vidējā atzīme ir {student1.calculate_avarage()}")
student1.izcils()
 
    