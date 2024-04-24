list=[]
n=int(input("enter the number of elements:"))
print("enter the elements:")
for i in range(0,n):
    num=int(input())
    list.append(num)
print("the list of numbers are:",list) 
del list[4]
print(list)
list.remove(1)
print(list)
