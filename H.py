for i in range(7):
    for j in range(6):
        if(j==0 or j==5) or (i==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
