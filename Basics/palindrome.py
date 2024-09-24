
s = "Sameeksha"
m = len(s)//2
flag = False

if s == s[::-1]:
    flag = True

print(flag)           

######## with loop

for i in range(0,m):
    if s[i] != s[len(s)-i-1]:
        flag = False
        break
    else:
        flag=True
        continue
    
print(flag)