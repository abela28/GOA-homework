# 1
# input არის მონაცემი, რომელსაც მომხმარებელი პროგრამაში შეჰყავს კლავიატურით.
# output არის შედეგი, რომელსაც პროგრამა აჩვენებს ეკრანზე.

# 2
print(input("enter your name:"))
print(input("enter your age"))


# 3
food = input("შეიყვანე შენი საყვარელი საჭმელი: ")
print(food)

# 4
name = input("შენი სახელი: ")
print("Hello " + name)

# 5
num = "5"                
user_num = input("შეიყვანე რაიმე რიცხვი: ")

numbers = int(num) + int(user_num)
print(numbers)

# 6
# ამ კოდს ერორი გამოაქვს იმიტომ, რომ input() ყველაფერს სტრინგავს,
# ხოლო 3 არის რიცხვი (int). ტექსტს + რიცხვს ერთამანეთს ვერ ვუმატებთ.
# რომ იმუშაოს, საჭიროა სტრინგის რიცხვად გადაქცევა: int(var)

# 7
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
print(num1//num2)