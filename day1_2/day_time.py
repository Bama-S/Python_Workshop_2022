#This file is demonstration of if else if statements
#Ask from the user whether the day is mon to fri
#If mon, wed, fri, then print "class starts at 8.30", if tues,thurs, class starts at 9.30 and sat, sun, holiday

day = input("Enter the day ")
print("The entered day is ", day)
if (day == "mon" or day == "wed" or day == "fri"):
    print("The class starts by 8.30 a.m.")
elif (day == "tues" or day == "thurs"):
    print("The class starts by 9.30 a.m.")
elif (day == "sat" or day == "sun"):
    print("It is a holiday")
else:
    print("You have entered a wrong day. Please enter mon or tues or wed or thurs or fri or sat or sun")

#Take two values from the user and print the largest from those two numbers

num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2"))
if num1>num2:
    print(num1, "is larger than", num2)
else:
    print(num2, "is larger than", num1)
