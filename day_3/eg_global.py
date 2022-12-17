#demo of local and global variables
def add(a,b):
    global addition
    addition = a+b #addition is a global variable
    

x = 100
y = 20
add(x,y)
print(addition)