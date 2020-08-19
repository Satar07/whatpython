a = 0
while a < 100:
    a += 1
    if a % 7 == 0:
        continue
    elif (a + 3) % 10 == 0:
        continue
    elif (a + 30) % 100 <10:
        continue
    else:
        print (a)