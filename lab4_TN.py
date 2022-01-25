# Tien Nguyen
# Section #
# 1/21/2022
# Tienn@email.sc.edu
# lab 4 playing with function
import random
def C_to_F():
    usr_tmp = int(input("Enter temeperature:"))
    tmp = (usr_tmp * (9/5)) + 32
    print("The temperature {} degrees Celsius is {} degrees Fahrenheit".format(usr_tmp, tmp))
def F_to_C():
    usr_tmp = int(input("Enter temeperature:"))
    tmp = (usr_tmp - 32) * (5/9)
    print("The temperature {} degrees Fahrenheit is {} degrees Celsius".format(usr_tmp, tmp))
def ran(x):
    if(x < 0):
        print("invalid input")
        return
    for i in range(x):
        a = random.randint(1,100)
        print("#{} = {}".format(i+1, a))
C_to_F()
F_to_C()
key = int(input("Enter number of random generate number you want: "))
ran(key)
print("Thank you from Tien Nguyen")
