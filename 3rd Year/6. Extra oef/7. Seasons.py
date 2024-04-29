Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Day = int(input())
Month = input()
indexM = Months.index(Month)

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
