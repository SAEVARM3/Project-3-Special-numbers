#Dæmi númer 1 - [Pósítívar tveggja stafa tölur sem eru þannig að annað veldi af summu einstakra tölustafa er jafnt tölunni sjálfri]
for i in range(10, 100):
    if ((i // 10) + (i % 10)) ** 2 == i:
        print (i)


#Dæmi númer 2 - [Tölur < 100 sem eiga sér nákvæmlega 10 deila]
for i in range (1, 100):
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 10:
        print(i)