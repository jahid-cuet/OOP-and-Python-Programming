a=list(map(str,input()))
c_L=0
c_R=0
cnt=0
b=[]
for i in a:

    if i=='L':
        c_L+=1
    else:
        c_R+=1
    if c_L==c_R:
        cnt+=1
        b.append(''.join((a[:c_L+c_R])))
        a=a[c_L + c_R:]
        c_L=0
        c_R=0
print(cnt)       
for s in b:
    print(s) 

      
