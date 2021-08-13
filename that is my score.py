for i in range(int(input())):
    n=int(input())
    d={}
    for j in range(n):
        p, s=map(int, input().split())
        if p not in d.key():
            d[p]=s
        else:
            k=max(s, d[p])
            d[p]=k
    print(sum(d.values()))