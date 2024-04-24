s1=input("enter the string")
s2=input("enter the string")
if len(s1)==len(s2):
    if (sorted(s1)==sorted(s2)):
     print("they are  equal")
    else:
        print("not equal")
def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("they are anagrams")
    else:
        print("they are not anagrams")
    
check(s1,s2)    

         