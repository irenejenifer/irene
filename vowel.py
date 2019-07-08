c = input()
if(c>='a' and c<='z') or (c>='A' and c<='Z'):
    if(c=='A' or c=='a' or c=='E' or c=='e' or c=='I'
     or c=='i' or c=='O' or c=='o' or c=='U' or c=='u'):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid')
