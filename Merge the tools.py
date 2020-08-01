# Enter your code here. Read input from STDIN. Print output to STDOUT
def merge_the_tools(string, k):
    # your code goes here
    from textwrap import wrap
    a=len(string)
    b=int(a/k)
    
    #c=wrap(string,b)
    c=[string[i:i+k] for i in range(0, len(string), k)]
    for i in c:
        newstr=''
        for j in i:     
            if j not in newstr:
                newstr=newstr+j
        print(newstr)  