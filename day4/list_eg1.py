#demo of list
#Accessing a list, modifying, deleting
#lists are mutable
def funList(l1):
    print (l1)
    print ("The first element in the list ", l1[0])
    print(l1[-1])#last element is -1
    print(l1[-2])#second to last element
    print("The original list ", l1)
    #to change 8 to 85
    l1[3] = 85#mutable
    print("The modified list", l1)
    #delete an element
    del l1[0]
    print("List after deleting 1st element ", l1)

list1 = [5,4,10,8,12]
funList(list1)