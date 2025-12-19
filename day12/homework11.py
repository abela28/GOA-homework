# 1
or1 = True or True
or2 = True or False
or3 = False or False
or4 = False or True

and1 = True and True
and2 = True and False
and3 = False and False
and4 = False and True

# 2
name = input("enter your name: ")
age = int(input("enter your age: "))
height = float(input("enter your height:"))

register = name == "giorgi" and age > 18 and height > 180
print(register)

# 4
num1 = int(input("enter random number1: "))
num2 = int(input("enter random number2: "))
result = num1 % num2 
print( "ნაშთი არის: " ,result)
# 5
age3 = int(input("enter your age: "))
is_even = age3 % 2 ==0
print(is_even)