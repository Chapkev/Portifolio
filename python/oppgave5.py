import random

teller_rett = 0

for i in range(0, 10):
    # at the end of for i in range it does not have :
    riktig_tall = random.randint(1, 10)

    gjett = str(input("gjett et tall mellom 1 og 10: "))
# gjett = str I cannot find out how to get it to work or if it even is the right text.
#but I do know there is somthing wrong here
    if gjett == riktig_tall:
         print("Riktig!")
         # print does not have text within print does not have the " symble
         teller_rett = teller_rett + 1
    else:
         print("Feil! det riktige tallet var" (riktig_tall))

print("du klarte", (teller_rett), "rette på 10 forsøk")