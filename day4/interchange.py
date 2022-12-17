#[2,3,5,6,8,100] interchange the first and last element

list1 = [2,3,5,6,8,100]

n = list1[0]
m = list1[-1]
list1[0]=m
list1[-1]=n
print(list1)