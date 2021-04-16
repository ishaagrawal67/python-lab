n=input("enter the string")
print("duplicate character in a given string: ")
for i in range (0,len(n)):
    c=1
    for j in range(i+1,len(n)):
        if(n[i]==n[j] and n[i]!=' '):
            c=c+1
            n=n[:j]+'0'+n[j+1:]
    if(c>1 and n[i]!='0'):
        print(n[i])
