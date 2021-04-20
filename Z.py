for i in range(7):
    for j in range(7):
        if i==0 or i==6 or(i==1 and j==5) or (i==2 and j==4) or (i==3 and j==3) or (i==4 and j==2) or(i==5 and j==1) :
            print("*",end="")
        else:
            print(end=" ")
    print()

