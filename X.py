for i in range(7):
    for j in range(5):
        if ((i==0 or i==1 or i==5 or i==6) and (j==0 or j==4)) or ((i==2 or i==4)and (j==1 or j==3)) or (i==3 and j==2):
            print("*",end="")
        else:
            print(end=" ")
    print()

