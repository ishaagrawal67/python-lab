for i in range(8):
    for j in range(7):
        if ((j==0 or j==6) and (i<4)) or (i==5 and (j==1 or j==5)) or (i==6 and (j==2 or j==4)) or (i==7 and j==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

