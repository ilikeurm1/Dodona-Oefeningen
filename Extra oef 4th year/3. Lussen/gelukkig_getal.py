# https://dodona.be/nl/courses/107/series/1295/activities/707295345

Done = False

Numbers_In_Number = []



while not Done:
    number = int(input())
    if number <= 0:
        continue
    if number < 100:
        for x in str(number):
            Numbers_In_Number.append(int(x))
        for i in Numbers_In_Number:
            Numbers_In_Number[i]

    

    
    
