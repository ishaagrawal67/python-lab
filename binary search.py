pos=-1
def search(lst, n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=(l+u)//2
        if lst[mid]==n:
            globals()["pos"]=mid
            return True
        else:
            if lst[mid]<n:
                l=mid
            else:
                u=mid
    return False

lst=[1,2,3,5,8]
n=6
if search(lst, n):
    print("found", pos+1)
else:
    print("Not found")