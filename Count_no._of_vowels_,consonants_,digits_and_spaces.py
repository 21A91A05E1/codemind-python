str=input()
c=0
c1=0
c2=0
c3=0
for i in str:
    if i in 'aeiouAEIOU':
        c+=1
    elif i in '0123456789':
        c1+=1
    elif i in ' ':
        c2+=1
    else:
        c3+=1
print("Vowels: %d"%c)
print("Consonants: %d"%c3)
print("Digits: %d"%c1)
print("White spaces: %d"%c2)
        