#D�mi n�mer 1 - [P�s�t�var tveggja stafa t�lur sem eru �annig a� anna� veldi af summu einstakra t�lustafa er jafnt t�lunni sj�lfri]
for i in range(10, 100):
    if ((i // 10) + (i % 10)) ** 2 == i:
        print (i)


#D�mi n�mer 2 - [T�lur < 100 sem eiga s�r n�kv�mlega 10 deila]
for i in range (1, 100):
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 10:
        print(i)