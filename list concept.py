x=[1,2,3,4,5,6,7,8,9]
print(x)
#print(type(x))
#print(len(x))
#i=int(input('Enter the number to find greater then that number in list  '))
i=int(input('Enter the number to find lesser then that number in list  '))
#if i in x:
    #print('number found in list')
    #print(i)
#else:
    #print('opps not found')
m=0
for p in x:
    #if(p>i):
    if(p<i):
        print(p)
        m+=1
if(m==0):
    print('no number as per given condition')

