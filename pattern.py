N = int(input("Enter the number of N: "))
for i in range(N):
    for j in range(0, i + 1):
        print("121", end=" ")
        print( )
        for i in range(1,N):
            for j in range(i,N):
                print("121", end =" ")
                print()  
