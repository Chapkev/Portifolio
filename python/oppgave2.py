import random

Partall = []
oddetall = []

for tall in range(0,21):
    if tall%2 == 0:
        Partall.append(tall)
    else:
        oddetall.append(tall)
print(Partall)
print(oddetall)