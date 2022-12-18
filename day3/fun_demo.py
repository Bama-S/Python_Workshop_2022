#example of a function
#function part
def add(n1,n2):
    print(n1)
    print(n2)
    total = n1+n2
    return total
    
def sub(n1,n2):
    subtraction = n1-n2
    return subtraction
    
#-----------------------------------------------------
#main program
x =100
y=10
addition = add(x,y)
print("total of two numbers", addition)
diff = sub(x,y)
print("difference of two numbers ", diff)

