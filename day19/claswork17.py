# 1
#  Slicing არის მეთოდი რომლის დახმარებითაც შეგვიძლია სიის ან სტრინგის კონკრეტული ნაწილის ამოჭრა.

# 2

list = ("nika", "giorgi", "luka", "sandro", "vanp")
print(list[2:])

# 3
name = input("enter name:")
print(name[1:4])

# 4
Lname = input("enter your last name:")
if Lname[:5] == "abela":
    print("almost same")
else:
    print("Bye")

# 5
random = ("nika", "giorgi", "luka", "sandro", "vanp", "maka","qeti")
random[2] = "random"
print(random[:4])