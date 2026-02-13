# 1
#  სია (list) არის მონაცემთა ტიპი, რომელიც გვაძლევს საშუალებას
#  ერთ ცვლადში შევინახოთ ბევრი მნიშვნელობა
#  სიას ვიყენებთ მაშინ, როცა გვინდა რამდენიმე მონაცემის ერთად შენახვა.

# 2
name = ["gio", "luka", "amiko", "zviadi", "petre"]
print(name[2])

# 3
nums = [3, 5, 6, 8, 9, 12, 14, 15, 18, 20]
for i in nums:
    if i % 3 == 0:
        print("divisible by 3")

# 4
random = "rice"
print(random[-3:])

# an da
random2 = "rice"
print(random2[-1]+random2[-2]+random2[-3])

# 5
names = ["Gio", "Nino", "Ana", "Gio", "Luka", "Gio"]

user_name = input("შეიყვანე სახელი: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count = count + 1

print(count)

# 6
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result=0

for i in nums:
    if i % 2 == 0:
        result = result + i
print(result)

# 7

names = ["gio", "nino", "giga", "ana", "guram"]

for i in names:
    if i[0] == "g":
        print(name, True)