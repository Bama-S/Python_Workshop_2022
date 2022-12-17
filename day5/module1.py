#write functions to find the square and cube of a given list
def actual(l1):
    return l1

def square(l1):
    s = []
    for i in l1:
        sqr = i*i
        s = s+[sqr]
    return s
    
def cube(l1):
    c = []
    for i in l1:
        cub = i*i*i
        c = c+[cub]
    return c
