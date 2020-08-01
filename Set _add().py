# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
y=list(set(l))
print(len(y))