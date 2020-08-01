# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d=OrderedDict()

 

n=input()
l=[]
for i in range(n):
    data=raw_input()
    l.append(data)
for a in l:
    w=a.split()
    if len(w)>2:
        x=w[0]+ " " + w[1]
        if x not in d.keys():
            d[x]=int(w[2])
        else:
            d[x]=d.get(x,0)+ int(w[2])
    else:
        x=w[0]
        if x not in d.keys():
            d[x]=int(w[1])
        else:
            d[x]=d.get(x,0)+ int(w[1])
    
for i,j in d.items():
    print i,j