#!/usr/bin/env python
# coding: utf-8

# In[18]:


print(" Simple Calculator")
a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
operation = float(input(" your choice operation\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division "))

if(operation==1):
    print("Addition is :",str(a+b))
elif(operation==2):
    print("Subtraction is :",str(a-b))
elif(operation==3):
    print("Multiplication is :",str(a*b))
elif(operation==4):
    print("Division is :",str(a/b))
else:
    print("choice is invalid")
        


# In[ ]:





# In[ ]:




