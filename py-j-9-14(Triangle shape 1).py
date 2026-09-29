

for i in range(1,8):
    for j in range(1,5):
        if i==j or j==7 or j==1 or j==8-i :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
    
    
