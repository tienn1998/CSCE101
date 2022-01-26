# Tien Nguyen
# Section #
# 01/25/2022
# tienn@email.sc.edu
# lab 5 different function
def makeList(x):
    numList = []
    for i in range(x):
        numList.append(i)
    print(numList)
def makeList2(x, y):
    numList2 = []
    num = y
    for i in range(x):
        numList2.append(num)
        num+=y
    print(numList2)
def makeList3(x):
    numList3 = []
    for i in range(x):
        numList3.append(i)
    print("first list")
    print(numList3)
    num = x
    while len(numList3) > 1:
        del numList3[0]
        print(numList3)
    print("last list")

key = int(input("Enter a value greater than 0:"))
makeList(key)
key = int(input("Enter a value greater than 0:"))
key2 = int(input("Enter a value greater than 0:"))
makeList2(key,key2)
key = int(input("Enter a value greater than 0:"))
makeList3(key)
print("Thank you from Tien Nguyen")
