#author=Щилов Михаил
a=str(input("введи целое число"))
b=len(a)
i=0
y=0
while i<=(b-1):	
    x=int(a[i])
    if x>y:
        y=x
    i+=1
print(y)