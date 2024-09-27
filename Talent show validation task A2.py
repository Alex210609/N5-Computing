#Talent show

name = input("whats ur name")
age = int(input("How old r u"))

while age <11 or age > 18:
    print("U shouldnt be in the show")
    age = int(input("IF u typed wrong plz try agen"))

print(" HI", name," Welcome to the talent show")
