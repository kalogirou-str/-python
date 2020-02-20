x=int(input("give a number: "))
sum=1
while x>9:
    x=x*3+1
    sum=0
    while x>0:
        k=x%10
        sum=sum+k
        x=int(x/10)
    x=sum
print(sum) 