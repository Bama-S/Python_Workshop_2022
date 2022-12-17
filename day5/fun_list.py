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
def line():
    print("-----------------")
print("Actual list")
list1 = [1,2,3,4,5]
given = actual(list1)
print(given)
line()
print("Square of the list ")
sq = square(list1)
print(sq)
line()
print("Cube of the list")
cb = cube(list1)
print(cb)
line()