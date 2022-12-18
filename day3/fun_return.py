#example with return statements

def cal_area(len,br):
    global x
    x = 10
    a = len*br
    return a


length = 25
breadth = 10
area = cal_area(length, breadth)
print (x)
print("area of the rectangle", area)
