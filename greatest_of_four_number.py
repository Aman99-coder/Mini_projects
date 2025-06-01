# A python program to find greatest of four numbers entered by user.

num1=input("Enter no.1:")
num2=input("Enter no.2:")
num3=input("Enter no.3:")
num4=input("Enter no.4:")
greatest=num1
if num2>greatest:
   greatest=num2
if num3>greatest:
    greatest=num3
if num4>greatest:
    greatest=num4
print("greatest number is:",greatest)
    

#succed with gpt


#greatest using function
num1=input("Enter no.1:")
num2=input("Enter no.2:")
num3=input("Enter no.3:")
num4=input("Enter no.4:")
answer=max(num1,num2,num3,num4)
print("greatest no is:",answer)
