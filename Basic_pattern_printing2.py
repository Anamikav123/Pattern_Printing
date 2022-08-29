for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print("\r")
print("===============================================")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print("\r")
print("===============================================")
# -1 added for reverse printing
num = list(range(5, 0, -1))
print(num)
b = 0
for i in range(5, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end="")
    print("\r")
print("===============================================")
for i in range(5, 0, -1):
    for j in range(0, i):#same as 1,i+i=0,i
        print(5, end="")
    print("\r")
print("===============================================")
for i in range(5, 0, -1):
    for j in range(0, i):
        print(10, end="")
    print("\r")
