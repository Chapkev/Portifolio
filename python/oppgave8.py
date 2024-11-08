import random

liste1 = ["griffin!"]

random_name = random.choice(liste1)


answer = input("Er du Modig?: ").strip()


if answer == '1':
    print(f"poeng til: {random_name} ")
elif answer == '2':
    print(f"poeng til: ingen!")
else:
    print("invalid list number: " + answer)
    


liste2 = ["Håsblås!"]

random_name2 = random.choice(liste2)


answer2 = input("Er du Tålmodig?: ").strip()


if answer2 == '1':
    print(f"poeng til: {random_name2} ")
elif answer2 == '2':
    print(f"poeng til: Smygard!")
else:
    print("invalid list number: " + answer2)




liste3 = ["Ravnklo!"]

random_name3 = random.choice(liste3)


answer3 = input("Er du Fokusert?: ").strip()


if answer3 == '1':
    print(f"poeng til: {random_name3} ")
elif answer3 == '2':
    print(f"poeng til: ingen!")
else:
    print("invalid list number: " + answer3 )


liste4 = ["Ravnklo!"]

random_name4 = random.choice(liste4)


answer4 = input("Er du Kreativ?: ").strip()


if answer4 == '1':
    print(f"poeng til: {random_name4} ")
elif answer4 == '2':
    print(f"poeng til: ingen!")
else:
    print("invalid list number: " + answer4 )



liste5 = ["griffin!"]

random_name5 = random.choice(liste1)


answer5 = input("Er du nysgjerrig?: ").strip()


if answer5 == '1':
    print(f"poeng til: {random_name5} ")
elif answer5 == '2':
    print(f"poeng til: ingen!")
else:
    print("invalid list number: " + answer5)



liste6 = ["Ravnklo!"]

random_name6 = random.choice(liste6)


answer6 = input("Er du organisert?: ").strip()


if answer6 == '1':
    print(f"poeng til: {random_name6} ")
elif answer6 == '2':
    print(f"poeng til: ingen!")
else:
    print("invalid list number: " + answer6 )




liste7 = ["griffin, Håsblås, Ravnklo!"]

random_name7 = random.choice(liste7)


answer7 = input("Er du snill?: ").strip()


if answer7 == '1':
    print(f"poeng til: {random_name7} ")
elif answer7 == '2':
    print(f"poeng til: ingen!")
else:
    print("invalid list number: " + answer7)


liste8 = ["griffin og Håsblås!"]

random_name8 = random.choice(liste8)


answer8 = input("Er du rettferdig?: ").strip()


if answer8 == '1':
    print(f"poeng til: {random_name8} ")
elif answer8 == '2':
    print(f"poeng til: Smygard!")
else:
    print("invalid list number: " + answer8)


liste9 = ["griffin og Ravnklo!"]

random_name9 = random.choice(liste9)


answer9 = input("Er du lojal?: ").strip()


if answer9 == '1':
    print(f"poeng til: {random_name9} ")
elif answer9 == '2':
    print(f"poeng til: Smygard!")
else:
    print("invalid list number: " + answer9)