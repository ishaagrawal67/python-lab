h=10
r=5
f=10
t=int(input("enter the time in minute"))
Vtank=3.14*r**2*h
Vwater=f*t
if Vwater>Vtank:
    print("over flow")
    print("volume of",Vwater-Vtank)
elif Vwater==Vtank:
    print("tank full")
else:
    print("under flow condition")
    ht=Vwater/3.14*r**2
    hr=h-ht
    print(f"filled height{ht}\nremaining height{hr}")