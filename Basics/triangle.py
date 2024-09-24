###### with numbers #######

row = int(input('Enter the dimension: '))

i=1
while i<row:
    j=1
    while j<=i:
        print(j,end='')
        j += 1
    print()
    i += 1 
    
print()
i=1
while i<row:
    j=1
    p=i
    while j<=i:
        print(p,end='')
        j += 1
        p += 1
    print()
    i += 1 
    
print()
i=1
p=i
while i<row:
    j=1
    while j<=i:
        print(p,end='')
        j += 1
        p += 1
    print()
    i += 1 
    
print()
i=1
while i<row:
    j=0
    while j<i:
        print(i-j,end='')
        j += 1
    print()
    i += 1 
    
####### with characters #######

print()
i=1
while i<=row:
    j=1
    while j<=i:
        print(chr(ord('A')+i-1),end='')
        j+=1
    print()
    i+=1
    
    
print()
i=1
while i<=row:
    j=1
    p=chr(ord('A')+i-1)
    while j<=i:
        print(chr(ord(p)+j-1),end='')
        j+=1
        
    print()
    i+=1
    
    
print()
    
i = 1
while i <= row:
    j = row
    p = ord('A') + j + 1
    while j >= row - i + 1:
        print(chr(p), end='')
        j -= 1
    print()
    i += 1

########## inverted ######

row = int(input('Enter the dimension: '))

i=row
while i>0:
    j=1
    while j<=i:
        print('*',end='')
        j += 1
    print()
    i -= 1 
print()

p=row
i=1
while i<= row:
    j=1
    while j<=row-i+1:
        print(p,end='')
        j+=1
    print()
    p-=1
    i+=1
    
###### mirrored ########
i=1
while i<=row:
    s=1
    j=1
    while s<=row-i:
        print(' ',end='')
        s+=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1
       
print() 

i=1
while i<=row:
    s=1
    j=1
    while s<=row-i:
        print(' ',end='')
        s+=1
    while j<=i:
        print(j,end='')
        j+=1
    
    print()
    i+=1
    
print() 

i=1
while i<=row:
    s=1
    j=1
    p=1
    while s<=row-i:
        print(' ',end='')
        s+=1
    while j<=i:
        print(p,end='')
        j+=1
        p+=1
    j=i-1
    while p>=1:
        print(p,end='')
        p-=1
    print()
    i+=1
        