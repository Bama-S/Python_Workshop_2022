#count the number of digits
num = int(input("enter any integer value "))
print ("The entered number is ", num)
count = 0
total = 0
while num !=0:
    print("number in loop ", count+1, num)
    count = count+1
    rem = num%10
    total = total+rem
    num = num//10    
print("number of digits ", count)
print("sum of digits ", total)
# sum of digits
# reversing a number
# cube of digits of a number   
