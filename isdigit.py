x=input()
if(x.isdigit()):
    print('yes')
else:
    try:
        float(x)
        print ('yes')
    except:
        print('no')
