# ---> imports <---

import math #not even in use lmao

# ---> Variables <---

Exam1 = int(input('Exam test 1: '))
Exam2 = int(input('Exam test 2: '))
Exam3 = int(input('Exam test 3: '))

Exams = [Exam1, Exam2 , Exam3]

# ---> Calculations <---

if Exam3 < Exam2 or Exam2 < Exam1 or Exam3 < Exam1:
    print('invalid input')
elif Exam1 >= 50 and Exam2 >= 50 and Exam3 >= 50:
    print('pass')
elif Exam1 < 50 and Exam2 < 50:
    print('fail')
elif Exam1 < 50 and Exam3 < 50:
    print('fail')
elif Exam2 < 50 and Exam3 < 50:
    print('fail')
elif sum(Exams) >= 150 and Exam1 >= 40 and Exam2 >= 40 and Exam3>= 40:
    print('deliberated')
else:
    print('fail')