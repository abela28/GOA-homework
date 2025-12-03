# 1
# int()- მონაცემი გადაყავს ინტეჯერად (მთელ რიცხვად)
# str()- მონაცემი გადაყავს სტრინგად (ტექსტურ მონაცემად)
# floot()-მონაცემი გადაყავს ფლოუთად(ათწილადად)

# 2
mother_age = int(input("დედის ასაკი:"))
father_age = int(input("მამის ასაკი:"))
sister1_age = int(input("დის ასაკი:"))
sister2_age = int(input("დის ასაკი:"))

print("25 წლის შემდეგ დედა იქნება", mother_age +25, "წლის")
print("25 წლის შემდეგ მამა იქნება", father_age +25, "წლის")
print("25 წლის შემდეგ და1 იქნება", sister1_age +25, "წლის")
print("25 წლის შემდეგ და2 იქნება", sister2_age +25, "წლის")

# 3
name = input("enter your name:")
print(type(name)) #ყოველთვის იქნება <class 'str'> რადგან input() რასაც ჩავწერთ ყველაფერი სტრინგოი გახდება

# 4
age = input("enter your age:") 
print(type(age)) #ისედაც სტრინგია მაგრამ მაინც გადავაქციოთ
print(str(age))
print(type(str(age)))

# 5
a = 10
b = 5

greater_than = a>b #true
less_than = a<b #false
greater_equal = a>=b #true
less_equal = a<=b #false
equal = a==b #false
not_equal = a!=b #true

print(greater_than,less_than,greater_equal,less_equal,equal,not_equal)
