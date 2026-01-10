# 1
# Conditional statements გამოიყენება იმისთვის, რომ პროგრამამ მიიღოს გადაწყვეტილება პირობის მიხედვით.

#2

age = 16

if age>18:
    print("adult")
elif age >= 13 and age <= 18:
    print("teen")
else:
    print("child")

#3
name = "gio"
age = "17"

if name == "giorgi":
    if age > 18:
        print("adult giorgi")
    else:
        print("not adult giorgi")
else:
    print("not gio")

# 4
a = 10
b = 5
if a % b == 0:
    print("true")
else:
    print("false")

# 5
film = input("enter your favorite film")
name = input("enter your name")

if name == "avto":
    print("you are avto")
elif name == "levani" and film == "titaniki":
    print("levani loves titaniki")
else:
    print("someone likes other film")