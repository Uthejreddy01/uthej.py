def getsum(n):
    sum=0
    for digit in str(n):
        sum=sum+int(digit)
    return sum
n=12356
print(getsum(n))

    