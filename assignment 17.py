# Create a JSON file (employee.json) containing employee information of minimum
# 5 employees. Each employee information consists of Name, DOB, Height, City, State.
# Write a python program that reads this information from the JSON file and saves 
# the information into a list of objects of Employee class. Finally print the list 
# of the Employee objects.

# For creating a json file of 5 employees and print objects of Employee class in list-->
import json
class Employee:
    def __init__(self):
        self.emp_dic={}
    def creat_JSON(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input('Enter your DOB: ')
            height = input('Enter your height: ')
            city = input('Enter your city: ')
            state = input('Enter your state: ')
            emp={'name':name,'dob':dob,'height':height,'city':city,'state':state}
            emp_id = len(self.emp_dic)+1
            self.emp_dic[emp_id]=emp
        with open("emps.json",'w') as f:
            json.dump(self.emp_dic,f)

    def data_print(self):
        with open("emps.json","r") as f:
            data = json.load(f)
        for i in data.values():
            l1 = []
            l1.append(i)
            print(l1)   

x =Employee()            
x.creat_JSON()
print("--------------------------------------------------")
x.data_print()  
