a=int(input())
b=list(map(int,input().split()))
o=[]
sf=0
for i in range (0,a):
	count=1
	if(b[i]>0):
		sf=1
	else:
		sf=0
	for j in range (i+1,a):
		if(sf==1):
			if(b[j]<0):
				sf=0
				count+=1
			else:
				break
		else:
			if(b[j]>0):
				sf=1
				count+=1
			else:
				break
	o.append(count)
print(*o)
