for i in range(6):
    for j in range(6):
        if j==0 or ((i==0 or i==6) and (j==4)) or ((i==1 or i==5) and j==3) or ((i==2 or i==4) and j==2) or (i==3 and j==1):
            print("*",end="")
        else:
            print(end=" ")
    print()

