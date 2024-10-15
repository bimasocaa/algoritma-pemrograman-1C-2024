    

size = int(input("masukkan size:"))

for i in range (size):
    if i == 0 or i == size -1:
        print("x" * size)
    else:
        print("x     x")
    
print()

for i in range (size):
    if i == 0 or i == size -1:
        print("a" * size)
    elif i == 3:
        print("a" * size)
    else:
        print("       a")

print()

for i in range (size):
    if i == 0 or i == size -1:
        print("x" * size)
    else:
        print("x     x")


    


