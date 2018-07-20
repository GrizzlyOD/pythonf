from math import sqrt
for n in range(99,81,-1):#不包括81
    root=sqrt(n)
    if root==int(root):
        print(n)
        break
else:
    print("don't find it")
