#demo of tuple
num_list = [100,200,300,400,500,100,100]#list
print(type(num_list))
num_tuple = (10,20,30,40,50)#immutable - cannot be changed
print(type(num_tuple))
print (num_tuple[3])
num_list[3]="a"#modification
print(num_list)

print(set(num_list))#unique elements in the list