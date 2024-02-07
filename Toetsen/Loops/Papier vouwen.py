mm, Limit = input().split('/') # get input

mm = float(mm) # convert to correct type
Limit = int(Limit) # convert to correct type

mm /= 1000 # set meter to mm
folds = 0 # set folds to 0

while mm < Limit:
    folds += 1 # add 1 fold
    mm += mm # Dubble thickness
    print(f'na {folds}x vouwen heb je een dikte van {mm} meter') # print

print(f'De gewenste hoogte is bereikt na {folds}x vouwen') # print
