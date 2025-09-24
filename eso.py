import random

szamok=[]

# 100 db elmü lista feltötése 1-99 közt


for i in range(100):

#..... szam generalas 
   
    rszam = random.randint(1, 100)

# szam elhelyezése 
   
    szamok.append(rszam)
    
print(szamok)

jatek_szam=0
nemndb=0

kszam = szamok[random.randint(0, len(szamok))]

tip= input("kerek egy egesz szamot")

while(not tip.isdecimal()):
    print("egesz zam")
    tip= input("kerek egesz szam [1-100]")

tip=int(tip)

if (tip < kszam):
    print("big")
elif (tip > kszam):
    print("smol")

while(tip != kszam):
    tip= input("kerek egesz szam [1-100]")
    
    while(not tip.isdecimal()):
        print("egesz zam")
    tip= input("kerek egesz szam [1-100]")

    tip=int(tip)
   
    if(tip<kszam):
        print("nagyob")
    elif (tip>kszam):
        print("kisebb")

print("jo vagy fiam")