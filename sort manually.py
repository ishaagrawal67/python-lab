L=[3, 8, 9, 4, 8, 5, 7, 1]
m=L[0]
for i in range(len(L)):
    for j in range(len(L)):
        if L[i]>L[j]:
            L[i], L[j]=L[j], L[i]
print(L)