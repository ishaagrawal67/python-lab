a=int(input())
setA=set(map(int, input().split()))
b=int(input())
setB=set(map(int, input().split()))
f=setA.symmetric_difference(setB)
for i in sorted(f):
    print(i)