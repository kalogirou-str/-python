import re
file=str(input("give me the name of your file: "))
op=open(file,"r")
x=op.read().split()
l=0
for i in x:
    x[l]=re.sub("[,.:/?()!;]", '', x[l])
    l=l+1
l=-1
for i in x:
    l=l+1
    if len(i)>3:
        print(x[l][1:]+x[l][0]+"ay")