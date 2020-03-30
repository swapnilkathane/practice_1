num=int(input('Enter the number to find divisers'))
x=2
while(x<num):
    if(num%x==0):
        print(x)
    x+=1
