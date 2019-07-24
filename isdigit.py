x=input()
if(x.isdigit()):
    print('Yes')
else:
    try:
        float(x)
        print ('Yes')
    except:
        print('No')
