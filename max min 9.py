n=input("enter the string")
shortest = min(n.split(),key=len)
largest=max(n.split(),key=len)
print("largest word is: ",largest)
print("and its length is: ",len(largest))
print("shortest word is: ",shortest)
print("and its length is: ",len(shortest))
