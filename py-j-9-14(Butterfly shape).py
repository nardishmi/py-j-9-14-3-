

for i in range(1,8):
    for j in range(1,8):
        if i+j==8 or i==j or j==1 or j==7 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
    