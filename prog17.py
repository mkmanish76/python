n = 5

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end=" ")
    
    for j in range(1, i + 1):
        if i == n:
            print(1, end="  ")
        else:
            if j == 1 or j == i:
                print(1, end="  ")
            else:
                print(2, end="  ")
    print()