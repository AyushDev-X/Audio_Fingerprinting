row = int(input('Enter the dimension: '))
i = 0
while i<row:
    j=1
    while j<=row:
        print(chr(ord('A')+j-1),end='')
        j += 1
    print()
    i += 1

print()
i = 1
while i<=row:
    j=1
    p=chr(ord('A')+i-1)
    while j<=row:
        print(chr(ord(p)+j-1),end='')
        j += 1
      
    print()
    i += 1
