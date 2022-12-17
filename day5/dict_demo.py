#demo of dictionary - {}, list - [], tuple - ()
dict1 = {1:["a","d","e"],2:"b",3:"c"}#key,value
print(type(dict1))

for key in dict1:
    print(key)

for key,value in dict1.items():
    print (key,value)

print (dict1[3])

print(dict1[1][1])