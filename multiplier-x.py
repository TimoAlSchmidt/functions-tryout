def tafel(nummer:int=1):
    print("++++",nummer,"+++++")
    for i in range(1, 10):
        print(i*nummer)


getal = int(input("Van welk getal wilt u de tafel zien?\n"))

tafel(getal)