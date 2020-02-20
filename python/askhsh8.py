import random
x=input("do you want to start my project? yes/no : ")
i=1
while x=="yes":
    if i>1:
        x=input("do you want to continue? yes/no : ")
    if x=="no":
        break
    if i==1:
            f1 =random.randint(10,100)
            f2 =random.randint(10,100)
            f3 =random.randint(10,100)


    def perissotero(f1, f2, f3):
        a=[]
        if f1 > f2 and f1 > f3:
            pras = f1
            k1=f2
            k2=f3
        elif f2 > f1 and f2 > f3:
            pras=f2
            k1=f1
            k2=f3
        elif f3>f1 and f3>f2:
            pras=f3
            k1=f1
            k2=f2
        elif f1==f2 and f1==f3:
            a.append(f1)
            a.append(f2)
            a.append(f3)
            pras=random.choice(a)
            k1=f1
            k2=f2
        elif f1 == f2:
            a.append(f1)
            a.append(f2)
            k1=f1
            k2=f3
            pras = random.choice(a)
        elif f1 == f3:
            a.append(f1)
            a.append(f3)
            k1=f1
            k2=f2
            pras = random.choice(a)
        elif f2==f3:
            a.append(f2)
            a.append(f3)
            pras=random.choice(a)
            k1=f2
            k2=f2
        return (pras, k1, k2)
        print (pras,k1, k2, f1, f2, f3)
    green=random.randint(5, 10)
    red1=random.randint(0,5)
    red2=random.randint(0,5)
    if i==1:
        (pras, k1, k2) = perissotero(f1, f2, f3)
        print("sto prwto anama to prasino exei", pras,"amaxia kai feugoun", green," to ena kokkino exei", k1,"kai erxontai", red1,"kai to allo kokkino", k2,"kai erxontai", red2)
    if i!=1:
        print("sto", i,"o anama to prsino exei", pras," amaxia kai feygoun ", green," to ena kokkino exei", k1," kai erxontai", red1," enw to allo kokkino exei", k2," kai erxontai", red2)
    pras=pras-green
    k1=k1+red1
    k2=k2+red2
    if pras<0 or k1<0 or k2<0:
        if pras<0:
            pras=0
        if k1<0:
            k1=0
        if k2<0:
            k2=0
    (pras, k1, k2) = perissotero(pras, k1, k2)
    i=i+1