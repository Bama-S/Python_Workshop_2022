# Python program to display all the prime numbers between 1 and 100



for x in range(1, 100 + 1):
# least prime number is 2, thus all prime numbers are greater than 1
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(x)
