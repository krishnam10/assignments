class Student:
    def setName(self, name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber=rollNumber
    def getRollNumber(self):
        return self.__rollNumber
  

stu=Student()
stu.setName(name=str(input("type your name: ")))
stu.setRollNumber(rollNumber=int(input("type your roll number:")))

print("your name:", stu.getName())
print("your roll number:", stu.getRollNumber())
