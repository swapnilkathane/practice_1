a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
m=0
l=[]
i=int(input('Enter the number to find less than that number in list'))
for p in a:
    if(p<i):
        l.insert(0,p)  #to print into list
        #print(p)      #to print one by one
        m+=1
if(m==0):
    ('Numbers not foudas per your request')
else:                 #to print into list
    print(l)