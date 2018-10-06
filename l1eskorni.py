#author=Щилов Михаил
import math 
a=int(input("введи первое число A:"))
b=int(input("введи второе число B:"))
c=int(input("введи второе число C:"))
print("надо найти корни квадратного уравнения :",a,"*x2+",b,"*x+",c,"=0")
d=b*b-4*a*c
print(d)
if d<0:
    print("квадратное уравнение не имеет корней")
elif d==0:
    x=-b/(2*a)
    print("уравнение имеет один корень, x=",x)
else: 
    x1=(-b-math.sqrt(d))/2*a
    x2=(-b+math.sqrt(d))/2*a
    print("уравнение имеет 2 корня, x1=",x1,"x2:",x2)   
