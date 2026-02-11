Exams = [int(input()), int(input()) , int(input())]

if Exams[2] < Exams[1] or Exams[1] < Exams[0] or Exams[2] < Exams[0]:
    print('invalid input')
elif Exams[0] >= 50 and Exams[1] >= 50 and Exams[2] >= 50:
    print('pass')
elif Exams[0] < 50 and Exams[1] < 50:
    print('fail')
elif Exams[0] < 50 and Exams[2] < 50:
    print('fail')
elif Exams[1] < 50 and Exams[2] < 50:
    print('fail')
elif sum(Exams) >= 150 and Exams[0] >= 40 and Exams[1] >= 40 and Exams[2]>= 40:
    print('deliberated')
else:
    print('fail')

# Exam1 = int(input('Exam test 1: '))
# Exam2 = int(input('Exam test 2: '))
# Exam3 = int(input('Exam test 3: '))

# Exams = [Exam1, Exam2 , Exam3]

# if Exam3 < Exam2 or Exam2 < Exam1 or Exam3 < Exam1:
#     print('invalid input')
# elif Exam1 >= 50 and Exam2 >= 50 and Exam3 >= 50:
#     print('pass')
# elif Exam1 < 50 and Exam2 < 50:
#     print('fail')
# elif Exam1 < 50 and Exam3 < 50:
#     print('fail')
# elif Exam2 < 50 and Exam3 < 50:
#     print('fail')
# elif sum(Exams) >= 150 and Exam1 >= 40 and Exam2 >= 40 and Exam3>= 40:
#     print('deliberated')
# else:
#     print('fail')