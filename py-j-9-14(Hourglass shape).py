

for i in range(1,8):
    for j in range(1,8):
        if i+j==8 or i==j or i==7 or i==1 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
    