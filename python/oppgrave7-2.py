import random

liste1 = ["Risa", "Livai", "Skitar", "Limma"]
liste2 = ["revhale", "Elgpels", "isbjørnhjerte", "slangetunge"]

random_name = random.choice(liste1)
random_name2 = random.choice(liste2)


answer = input("which list?: ").strip()


if answer == '1':
    print(f"The random name selected is: {random_name} {random_name2}")
else:
    print("invalid list number: " + answer)