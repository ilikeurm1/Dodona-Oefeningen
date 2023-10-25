# https://dodona.be/nl/courses/107/series/1244/activities/1800551125

# ---> Imports <---

import math # I always just import this cuz I might use it ... maybe ... sometimes

# ---> Variables <---

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
Seasons = ['spring', 'summer', 'autumn', 'winter'] # also pretty useless xD
Worked = None

# ---> Inputs <---

Day = int(input('Which day is it: '))
Month = input('Which month is it: ')
indexM = Months.index(Month)
indexD = Days.index(Day) # prob not gonna be used.

# ---> Calculations <---

if Day in Days and Month in Months:
    Worked = True
    if (Day >= 21 and indexM == 11) or (indexM < 2):
        print(f'It is winter on {Month} {Day}.') # winter
    elif indexM == 2 and Day <= 20:
        print(f'It is winter on {Month} {Day}.') # winter
    

    elif (Day >= 21 and indexM == 2) or (indexM < 5):
        print(f'It is spring on {Month} {Day}.') # spring
    elif indexM == 5 and Day <= 20:
        print(f'It is spring on {Month} {Day}.') # spring


    elif (Day >= 21 and indexM == 5) or (indexM < 8):
        print(f'It is summer on {Month} {Day}.') # summer
    elif indexM == 8 and Day <= 22:
        print(f'It is summer on {Month} {Day}.') # summer
            

    else:
        print(f'It is autumn on {Month} {Day}.') # autumn

else:
    Worked = False
    print(Worked)
