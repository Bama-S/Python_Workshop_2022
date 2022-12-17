#slicing of list elements
#list1 = ["red","blue","green","yellow","orange"]
#print(list1[0:3])
#print(list1[:3])
#print(list1[3:])
#print (list1[:])
#nested list
list4 = [[1,2,3],[4,5,6]]
print(list4[0][1])#to get 2
#get the position of 5. Multiply the element by 10 and replace in the list
n = list4[1][1]*10
list4[1][1] = n
print(list4)