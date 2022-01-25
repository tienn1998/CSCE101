# Tien Nguyen
# Section #
# 1/12/2022
# Tienn@email.sc.edu
# lab 02 get input from user and deal with math operators
usr_tmp = 0
converted_tmp = 0
usr_tmp = int(input("Enter temperature to be converted to Fahrenheit:"))
converted_tmp = (usr_tmp * (9/5)) + 32
print("The temperature {} degrees Celsius is {} degrees Fahrenheit".format(usr_tmp, converted_tmp))
usr_tmp = int(input("Enter temperature to be converted to Celsius:"))
converted_tmp = (usr_tmp - 32) * (5/9)
print("The temperature {} degrees Fahrenheit is {} degrees Celsius".format(usr_tmp, converted_tmp))
print("Thank you from Tien Nguyen")
