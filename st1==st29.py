n=input("enter the string")
m=input("enter the string 2")
p=''
for i in n:
    if i not in m:
        p=p+1
print(f"string after filter{p})
