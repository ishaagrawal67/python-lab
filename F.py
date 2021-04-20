for i in range(5):
    for j in range(4):
        if(j==0) or (i==0 or i==2):
            print("*",end="")
        else:
            print(end=" ")
    print()
