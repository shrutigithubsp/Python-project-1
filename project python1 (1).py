#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class StudentDataSystem:
    pass


# In[8]:


class StudentDataSystem:
    def __init__(self,name,rollno,marks1,marks2):
        self.rollno=rollno
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        
        
    def display(self):
        print("Name:",self.name)
        print("Roll Number:",self.rollno)
        print("Marks1 :",self.marks1)
        print("marks2 :",self.marks2)
        
        
        
     
       


class StudentDataSystem:
    def __init__(self):
        self.students=[]
        
    def add_student(self,student):
        self.students.append(student)
        
    def search_student(self,rollno):
        for student in self.students:
            if student.rollno == rollno:
                return student
            return None
        
             
           
        

    
    def delete_student(self,rollno):
        student = self.search_student(rollno) 
        if student:
            self.students.remove(student)
            print("student data deleted successfully")
        else:
            print("student data not found")
            
    def update_student(self,rollno,name,marks1,marks2):       
        student = self.search_student(rollno)
        if student:
            student.name = name
            student.marks1 = marks1
            student.marks2 = marks2
            print("Student data updated successfully.")
        else:
            print("Student not found")
            
            
#creating a student data system object
data_system = StudentDataSystem()
#creating object
student1 = Student("Aman",1,2,95)
student2 = Student("Amit",2,85,88)
student3 = Student("Suraj",3,72,78)
student4 = Student("Naincy",4,60,64)
student5 = Student("Daisy",5,54,52)

#Adding students to the datasystem
data_system.add_student(student1)
data_system.add_student(student2)              
data_system.add_student(student3)        
data_system.add_student(student4)         
data_system.add_student(student5)            
            
                
# displaying the student data
student1.display()
print()
student2.display()
print()
student3.display()
print()
student4.display()
print()
student5.display()
print()
    


#searching for a student    
roll_no=6
found_student=data_system.search_student(roll_no)
if found_student:
    print("student found")
    found_student.display()
else:
    print("student not found")
print()    
       
        
#to delete student data
rollno=8
data_system.delete_student(rollno)
print()

#Updating a student's information
rollno =10
name="Rupa"
marks1=80
marks2=75
data_system.update_student(rollno,name,marks1,marks2)
    

                     
                   
    


# In[ ]:




