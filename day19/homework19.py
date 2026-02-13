# # 1
# num = [10, 5, 34, 54, 1, 92, 2, 23, 9, 12]
# for i in num:
#     if i >= 10:
#         print(i)
# # 2
# U_name = input("enter your name:")
# print("პირველი ასოა:" ,U_name[0])
# print("ბოლო ასოა:",U_name[-1])

# # 3
# list = ["luka", "gio", "sandro", "amiko"]
# back_list = list[::-1]
# print(back_list)

# # 4
# Lname = input("enter your last name:")
# ok = Lname[0:5]
# yes = ok[::-1]
# print("პირველი 5 ასო შეტრიალებული:",yes)

# 5
number = [10,20,30,40,50,60,70,80,90,100]
while True:
    n = int(input("შეიყვანე რიცხვი 1-5 დიაპაზონში:  "))
    if 1 <= n >=5:
        print(number[n-1::n])
    else:
        print("შეცდომა! შეიყვანე რიცხვი 1-5 დიაპაზონში")
    numbers = [1, 2, 3, 4, 5, 6]
