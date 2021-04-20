for i in range(7):
    for j in range(7):
        if ((j==0 or j==6)and(i>1 and i<5)) or ((i==0 or i==6) and(j>1 and j<5)) or ((i==1 or i==5) and (j==1 or j==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
