# Tien Nguyen
# Section #
# 1/17/2022
# Tienn@email.sc.edu
# lab 03 grade calculator
test1 = int(input("Enter test 1 grade: "))
test2 = int(input("Enter test 2 grade: "))
lab_avg = int(input("Enter lab average: "))
project = int(input("Enter project grade: "))
quiz = int(input("Enter quiz grade: "))
final_grade = (test1*0.15)+(test2*0.15)+(lab_avg*0.45)+(project*0.10)+(quiz*0.15)
if final_grade >= 90 and final_grade <= 100:
    print('Congratulations! Your grade is a A {}'.format(final_grade))
elif final_grade >= 80 and final_grade < 90:
    print('Congratulations! Your grade is a B {}'.format(final_grade))
elif final_grade >= 70 and final_grade < 80:
    print('Congratulations! Your grade is a C {}'.format(final_grade))
elif final_grade >= 60 and final_grade < 70:
    print('Congratulations! Your grade is a D {}'.format(final_grade))
else:
    print('Sorry! Your grade is a F {}'.format(final_grade))
