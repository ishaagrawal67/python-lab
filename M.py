for i in range(7):
    for j in range(7):
        if j==0 or j==6 or ((i==0)and(j==1 or j==5)) or ((i==1)and(j==2 or j==4))or (i==2 and j==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
