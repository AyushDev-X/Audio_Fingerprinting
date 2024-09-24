import math

def  func(r):
    area = math.pi*r**2
    circumference = 2*math.pi*r
    
    return area,circumference

a,c = func(5)

cube = lambda x: x**3

print(round(a,2),c)
print(cube(3))

i=1
while i<5:
    print(i)
    i += 1

print('\n')

j=0
for j in 5:
    print(j) 