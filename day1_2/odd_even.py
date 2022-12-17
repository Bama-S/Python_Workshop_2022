#This file is to determine whether the number is odd or even

num = int(input("enter the number "))
if num%2 == 0:#checking the remainder when divided by 2
    print("The given number", num,"is even")
else:
    print("The given number", num, "is odd")