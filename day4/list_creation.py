##write a function to take  5 numbers in a list and double those.
num_range=[]
for i in range(1,6):
    n = int(input("enter the number "))
    num_range = num_range+[n]
print("The num_range list ", num_range)

double_num = []
for i in num_range:
    double = 2*i
    double_num = double_num+[double]
print("The list double of num_range", double_num)

#list_num = get_input()