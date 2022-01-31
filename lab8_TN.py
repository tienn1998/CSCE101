# Tien Nguyen
# Section #
# 01/29/2022
# tienn@email.sc.edu
# lab 8 file io
file = open('lab08_python.txt')
newfile = open('tien.txt', 'w')
line = file.readlines()
for l in line:
    newfile.write(l)
file.close()
newfile.close()
print("Thank you from Tien Nguyen")
