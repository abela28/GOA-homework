# 1
numbers = [3, 12, 7, 25, 10, 18, 5]

for num in numbers:
    if num > 10:
     print(num)

# 2
item = [10 , "GIORGI", True, 3.5, False, 'luka', 9]

for i in item:
   print(type(i))

# 3
number = [10,9,8,7,6,5,4,3,2,1]
sum = 0

for i in number:
   sum += i
print(sum)

# 4
items = ["a", "b", "c", "d"]

for index in range(len(items)):
    print(index, items[index])

# 5
items = ["a", "b", "c", "d","i", "x", "f", "k"]

for index in range(len(items)):
    if index % 2 ==0:
        print(index, items[index])

# 6
numbers = [5, -3, 0, 7, -1, 0, 4]

positive = 0
negative = 0
zero = 0

for i in numbers:
    if i > 0:
        positive += i
    elif i < 0:
        negative += 1
    else:
        print("zero")
        zero += 1

print("დადებითი რიცხვების ჯამი:", positive)
print("უარყოფითი რიცხვების რაოდენობა:", negative)
print("ნულების რაოდენობა:", zero)
