# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n=int(input())
b=[]
sum=0

for i in range(n):
    b.append(input())
    
a=Counter(b)
print(len(a.keys()))
for c in a.values():
    print(c,end=' ')