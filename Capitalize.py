# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(s):
        l=[]
        g=[]
        l.append(s.split(' '))
        
        
        for i in l[0][::]:
            c=i.capitalize()
            g.append(c)
        return " ".join(g)