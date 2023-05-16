import json
class State_Capital:
    def __init__(self):
        self.st_cap={}
    def creat_JSON(self):
        for i in range(7):
            s_name = input("Enter state name: ")
            c_name = input("Enter capital name: ")
            print("-------------------")
            SC_dict={s_name:c_name}
            self.st_cap.update(SC_dict)
        with open("state_capital.json",'w') as f:
            json.dump(self.st_cap,f)

    def print_JSON(self):
        with open("state_capital.json",'r') as f:  
            data = json.load(f)
        for i,j in data.items():
            print('State:'+ i + '  Capital:'+ j)    


x = State_Capital()
x.creat_JSON()
x.print_JSON()    
