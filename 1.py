n=int(input("Enter any number :"))
l=[]

while ( n != 0):
    temp= n % 2
    l.append(temp)
    n = n//2
l.reverse()
s=""
for i in l:
    s=s+str(i)
print(s)
    
