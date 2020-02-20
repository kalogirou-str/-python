import re
a=[]
b=[]
file=str(input("give me the name of your file: "))
vowels=["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
for i in range(0,5):
    mx = 0
    word=""
    op = open(file, 'r')
    words = op.read().split()
    l = 0
    for i in words:
        words[l] = re.sub("[,.:/?()!;]", '', words[l])
        l = l + 1
    for i in words:
        if len(i) > mx and i not in a:
            mx = len(i)
            word = i
    k=word
    a.append(word)
    for x in k.lower():
        if x in vowels:
            k=k.replace(x,"")
    b.append(k)
b.reverse()
print(b)
