n=input("enter the string")
v=d=s=c=0
for i in n:
    if(i=='a'or i=='e' or i=='o' or i=='u' or i=='i')or(i=='A' OR i=='I' or i=='O' or i=='U' OR i=='E'):
        v=v+1
    elif(i.isdigit()):
        d=d+1
    elif (i.isspace()):
        s=s+1
    else:
        c=c+1
print("number of vowels",v)
print("number of digits",d)
print("number of space",s)
print("number of consonants",c)

        
