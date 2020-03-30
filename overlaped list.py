L1=[2,4,6,8,10,12,14,16,18,20]
L2=[4,8,12,16,20,24,28,32,36,40]
L3=[]
for x in L1:
    for y in L2:
        if x==y and y not in L3:
            L3.append(x)

print("The common number list is L3=",L3)
