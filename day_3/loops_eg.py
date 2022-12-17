#break,pass and continue

for i in range(1,10):
    print(i)
    if i == 8:
        break
        print("hello")
print("-------------------------------")
for i in range(1,10):
    print(i)
    if i == 8:
        continue
        print("hello")
print("--------------------------------")
for i in range(1,10):
    print(i)
    if i == 8:
        pass
        print("hello")