# https://dodona.be/nl/courses/107/series/1295/activities/1898834779
 
import math

Code_1 = []
Code_2 = []
Code_3 = []
Code_4 = []
Counter = 0

while True:
    n = input()
    if n == 'stop':
        break
    if Counter <= 10:
        Code_1.append(int(n))
    elif Counter <= 20:
        Code_2.append(int(n))
    Counter += 1

if Code_1[-1] == Code_1[0] + 2 * Code_1[1] + 3 * Code_1[2] + 4 * Code_1[3] + 5 * Code_1[4] + 6 * Code_1[5] + 7 * Code_1[6] + 8 * Code_1[7] + 9 * Code_1[8]:
    print('OK')
else:
    print('FOUT')
if Code_2[-1] == Code_2[0] + 2 * Code_2[1] + 3 * Code_2[2] + 4 * Code_2[3] + 5 * Code_2[4] + 6 * Code_2[5] + 7 * Code_2[6] + 8 * Code_2[7] + 9 * Code_2[8]:
    print('OK')
else:
    print('FOUT')

