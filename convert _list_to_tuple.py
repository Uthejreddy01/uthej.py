a=[]
n=int(input("emter the number of elements:"))
print("enter the elements:")
for i in range(0,n):
    num=int(input())
    a.append(num)
print("list :",a)
t=tuple(a)
print("tuple:",t)    