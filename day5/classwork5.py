#1) კარგი პრაქტიკები ნიშნავს სწორი და გასაგები კოდის წერის წესებს, რომლებიც პროგრამას უფრო მარტივად წასაკითხს და გასაგებს ხდის.
# მაგალითი: ცვლადების სახელები უნდა იყოს გასაგები 
user_age = 22  # კარგი პრაქტიკა
x = 22         # ცუდი პრაქტიკა, რადგან გაურკვეველია რას ნიშნავს x

# 2)
age = 13
age = 14
print(age)

# 3)
# პითონი არის case sensitive, ანუ დიდი და პატარა ასოები განსხვავებულად აღიქმება.
# ეს ნიშნავს, რომ name, Name და NAME სხვადასხვა ცვლადებია.
name = "giorgi"
Name = "vano"
NAME = "nika"

# 4)
print(name)  # გამოიტანს giorgi
print(Name)  # გამოიტანს vano
print(NAME)  # გამოიტანს nika

# 5)
a = 6
b = 4
product = a * b
print(product)

# 6)
print(7634 % 4)   # 2
print(982 % 3)    # 2
print(12345 % 3)  # 0 

name = "giorgi"
print(name)
name = "vano"
Name = "nika"
NAME = "saba"
print(Name)
# ეს კოდი გამოიტანს ჯერ giorgi ს და შემდეგ nika ს


# 7)
age = 23
print(age)   # "Age" შეცვლილია სწორად "age"-ით

num = 34
print(num + 5)    # ცვლადი უნდა იყოს რიცხვი, არა ტექსტი

print("5"*3)   # მგონი სწორია უბრალოდ 5 დაიწერება 3ჯერ 
