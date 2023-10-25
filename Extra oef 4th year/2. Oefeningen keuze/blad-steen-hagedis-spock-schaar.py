# https://dodona.be/nl/courses/107/series/1244/activities/1647887074

Hands = ["blad", "steen", "hagedis", "Spock", "schaar"]

plr1 = input()
plr2 = input()

plr1_chose = Hands.index(plr1)
plr2_chose = Hands.index(plr2)

if plr1 == plr2:
    print('gelijkspel')
elif plr1_chose == 0:
    if plr2_chose == 1 or plr2_chose == 3:
        print('speler1 wint')
    else:
        print('speler2 wint')
elif plr1_chose == 1:
    if plr2_chose == 2 or plr2_chose == 4:
        print('speler1 wint')
    else:
        print('speler2 wint')
elif plr1_chose == 2:
    if plr2_chose == 0 or plr2_chose == 3:
        print('speler1 wint')
    else:
        print('speler2 wint')
elif plr1_chose == 3:
    if plr2_chose == 1 or plr2_chose == 4:
        print('speler1 wint')
    else:
        print('speler2 wint')
elif plr1_chose == 4:
    if plr2_chose == 0 or plr2_chose == 2:
        print('speler1 wint')
    else:
        print('speler2 wint')
