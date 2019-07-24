x=int(input())
y=input()
y=list(map(int,y.split()))
o=[]
sf=0
for i in range (0,x):
	count=1
	if(y[i]>0):
		sf=1
	else:
		sf=0
	for j in range (i+1,x):
		if(sf==1):
			if(y[j]<0):
				sf=0
				count+=1
			else:
				break
		else:
			if(y[j]>0):
				sf=1
				count+=1
			else:
				break
	o.append(count)
print(*o)
