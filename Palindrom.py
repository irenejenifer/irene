n=int(input())
temp=n
rev=0
while(n>0):
    d=n%10
    n=n//10
    rev=rev*10+d
if(temp==rev):
    print("yes")
else:
    print("no")

