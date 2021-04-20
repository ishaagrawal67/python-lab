for i in range(6):
    for j in range(5):
        if(i==0 or i==5) or j==2:
            print("*",end="")
        else:
            print(end=" ")
    print()
