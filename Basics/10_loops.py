##  Loops

num = 0

while num < 101:
    if num % 2 == 0:
        print(num)
    else:
        print("Es un numero impar")

    num += 1

my_list = [13, 17, 25, 44, 22]

print("\n\n")
for i in my_list:
    print(i)

my_tuple = ("Pablo", "Garcia", 37, 1.65)

print("\n\n")
for i in my_tuple:
    print(i)

my_set = {"Sebastian", "Pissinis", 41, 1.75}

print("\n\n")
for i in my_set:
    print(i)

my_dict ={"Name": "Pablo", "Surname": "Garcia", "Age": 37, "Height": 1.65}

print("\n\n")
for i in my_dict:
    print(i)

print("\n\n")
for i in my_dict.values():
    print(i)
