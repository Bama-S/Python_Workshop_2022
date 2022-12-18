#find the sum of even integers between 1 to 100
total=0
for i in range(1,101):
    if(i%2 ==0):
        total=total+i  

print("The sum of even numbers between 1 and 100 ", total)
