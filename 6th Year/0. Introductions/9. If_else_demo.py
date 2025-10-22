aga = int(input("How fucking old are you unc: "))
genda = input("Genda (m/f/x): ")
male = False
female = False
unc = False

if aga >= 18:
    unc = True
    print("You are an unc")

if genda == "m":
    male = True
elif genda == "f":
    female = True

if unc:
    if male:
        print("mista")
    elif female:
        print("misis")
    else:
        print("faking attack vlyat")
else:
    if male:
        print("dawg")
    elif female:
        print("leidaaaa")
    else:
        print("faking attack vlyat")
