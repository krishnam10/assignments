#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().set_next_input('Write a program to find all pairs of an integer array whose sum is equal to a given number');get_ipython().run_line_magic('pinfo', 'number')


# In[ ]:


Write a program to find all pairs of an integer array whose sum is equal to a given number


# In[1]:


def getPairsCount(arr, n, sum):
 
    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))


# In[ ]:


Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


# In[2]:


def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[ ]:


get_ipython().set_next_input('Write a program to check if two strings are a rotation of each other');get_ipython().run_line_magic('pinfo', 'other')


# In[3]:


def checkString(s1, s2, indexFound, Size):
    for i in range(Size):
 
        if(s1[i] != s2[(indexFound + i) % Size]):
            return False
    return True
s1 = "abcd"
s2 = "cdab"
 
if(len(s1) != len(s2)):
    print("s2 is not a rotation on s1")
 
else:
 
    indexes = [] 
    Size = len(s1)
    firstChar = s1[0]
    for i in range(Size):
        if(s2[i] == firstChar):
            indexes.append(i)
 
    isRotation = False
 
 
    for idx in indexes:
 
        isRotation = checkString(s1, s2, idx, Size)
 
        if(isRotation):
            break
 
    if(isRotation):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")


# In[ ]:


get_ipython().set_next_input('Write a program to print the first non-repeated character from a string');get_ipython().run_line_magic('pinfo', 'string')


# In[6]:


string = "edyoda"
index = -1
fnc = ""
 
if len(string) == 0 :
  print("EMTPY STRING");
 
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is", fnc)


# In[ ]:


Read about the Tower of Hanoi algorithm. Write a program to implement it.


# In[7]:


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  

N = 3
  

TowerOfHanoi(N, 'A', 'C', 'B')# A, C, B are the name of rods


# In[ ]:


Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.


# In[8]:


def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
 
    
    length = len(post_exp)
 

    for i in range(length):
 
      
        if (isOperator(post_exp[i])):
 
           
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
         
            temp = post_exp[i] + op2 + op1
 
           
            s.append(temp)
 
        else:
 
         
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 

if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    print("Prefix : ", postToPre(post_exp))


# In[9]:


Write a program to convert prefix expression to infix expression.


# In[10]:


def prefixToInfix(prefix):
    stack = []
     
   
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            
            stack.append(prefix[i])
            i -= 1
        else:
           
          
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# In[ ]:


Write a program to check if all the brackets are closed in a given code snippet.


# In[11]:


def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# In[ ]:


Write a program to reverse a stack.


# In[12]:


class Stack:
 
  
    def __init__(self):
        self.Elements = []
         
    
    def push(self, value):
        self.Elements.append(value)
       
   
    def pop(self):
        return self.Elements.pop()
     
  
    def empty(self):
        return self.Elements == []
     
   
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 

def BottomInsert(s, value):
   
   
    if s.empty():
         
     
        s.push(value)
         
   
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 

stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[ ]:


Write a program to find the smallest number using a stack.


# In[13]:


class Node:
   
    def __init__(self, value):
        self.value = value
        self.next = None
 
    
    def __str__(self):
        return "Node({})".format(self.value)
 
 
    __repr__ = __str__
 
 
class Stack:
   
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
 
  
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top, out))
 
   
    __repr__ = __str__
 
   
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
 

 
    def isEmpty(self):
     
        if self.top == None:
            return True
        else:
           
            return False
 
   
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count
 
   
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
 
   
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
 
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))
 
  
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ((2 * self.minimum) - removedNode)
            else:
                print("Top Most Element Removed : {}" .format(removedNode))
 
 

if __name__ == '__main__':
   
  stack = Stack()
   
  # Function calls
  stack.push(3)
  stack.push(5)
  stack.getMin()
  stack.push(2)
  stack.push(1)
  stack.getMin()
  stack.pop()
  stack.getMin()
  stack.pop()
  stack.peek()


# In[ ]:




