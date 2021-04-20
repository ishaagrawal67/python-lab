for i in range(6):
    for j in range(6):
        if(i==0) or (j==3) or ((i==5) and (j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
