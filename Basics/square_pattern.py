
# with '*'
row = int(input('Enter the dimension: '))
i = 0
while i<row:
    j=0
    while j<row:
        print("*",end='')
        j += 1
    print()
    i += 1

print()
# with 'i'
i=0
while i<row:
    j=0
    while j<row:
        print(i,end='')
        j+=1
    print()
    i+=1
    
print()
# with 'j'
i=0
while i<row:
    j=0
    while j<row:
        print(j,end='')
        j+=1
    print()
    i+=1
    
print()
# with 'j'
i=0
while i<row:
    j=0
    while j<row:
        print(row,end='')
        j+=1
    print()
    i+=1