class point:
    def __init__(self):
        self.x = x
        self.y = y
        self.z = z

    def sqsum(self):
        return ((self.x **2), (self.y **2), (self.z **2))

    def sum(self):
        return ((self.x **2) + (self.y **2) + (self.z **2))

x = int(input("Enter the first number:"))
y = int(input("Enter the second number :"))
z = int(input("Enter the third number:"))

a = point()

print("square of the number are:",a.sqsum())
print("sum of the square are :",a.sum())
