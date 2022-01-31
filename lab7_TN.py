# Tien Nguyen
# Section #
# 01/26/2022
# tienn@email.sc.edu
# lab 7 file io
num = []
file = open('lab07_python.txt')
line = file.readlines()
large = 0
small = 10000
for f in line:
    if large < int(f):
        large = int(f)
    if small > int(f):
        small = int(f)
    num.append(int(f))
file.close()
total = 0
for i in range(len(num)):
    total += num[i]
print("smallest value: {}".format(small))
print("largest value: {}".format(large))
print("total values: {}".format(total))
print("Thank you from Tien Nguyen")
